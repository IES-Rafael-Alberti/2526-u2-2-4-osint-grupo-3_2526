import requests
from bs4 import BeautifulSoup
import json
import time
import sys

def scrape_hospital_doctors(base_url="https://www.hospitalespascual.com/cuadro-medico/?hospital=hospital-san-rafael", 
                             hospital_filter="hospital-san-rafael"):
    """
    Scrapes doctor profiles from Hospitales Pascual with pagination support.
    
    Args:
        base_url: Base URL of the cuadro médico page
        hospital_filter: Hospital code to filter (e.g., 'hospital-san-rafael')
    """
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    }

    all_doctors = []
    page = 1
    max_pages = 50  # Safety limit to avoid infinite loops
    
    print(f"[*] Starting scrape for {hospital_filter}...")
    
    while page <= max_pages:
        # Build URL with hospital filter and page number
        if page == 1:
            url = f"{base_url}?hospital={hospital_filter}"
        else:
            url = f"{base_url}?hospital={hospital_filter}&pagina={page}"
        
        print(f"[*] Fetching page {page}: {url}")
        
        try:
            response = requests.get(url, headers=headers, timeout=30)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Find all doctor profile cards
            doctor_cards = soup.select('.doctor-column .doctor-profile')
            
            if not doctor_cards:
                print(f"[!] No more doctors found on page {page}. Stopping.")
                break
            
            print(f"[*] Found {len(doctor_cards)} doctors on page {page}")
            
            for card in doctor_cards:
                doctor = {}
                
                # Extract image
                img_tag = card.select_one('.image-container img')
                if img_tag:
                    doctor['image_url'] = img_tag.get('src', '')
                else:
                    doctor['image_url'] = None
                
                # Extract position/role
                position_tag = card.select_one('.position')
                if position_tag:
                    doctor['position'] = position_tag.get_text(strip=True)
                else:
                    doctor['position'] = None
                
                # Extract name
                name_tag = card.select_one('.name')
                if name_tag:
                    doctor['name'] = name_tag.get_text(strip=True)
                else:
                    doctor['name'] = None
                
                # Extract specialty
                specialty_tag = card.select_one('.specialty')
                if specialty_tag:
                    doctor['specialty'] = specialty_tag.get_text(strip=True)
                else:
                    doctor['specialty'] = None
                
                # Extract hospital
                hospital_tag = card.select_one('.hospital')
                if hospital_tag:
                    doctor['hospital'] = hospital_tag.get_text(strip=True)
                else:
                    doctor['hospital'] = None
                
                # Extract location/address
                location_tag = card.select_one('.location')
                if location_tag:
                    doctor['location'] = location_tag.get_text(strip=True)
                else:
                    doctor['location'] = None
                
                # Only add if we have at least a name
                if doctor.get('name'):
                    all_doctors.append(doctor)
            
            # Check if there are more pages by looking for pagination buttons
            # The pagination likely has numbered buttons or a "next" button
            pagination = soup.select('.pagination-button')
            if not pagination or len(doctor_cards) == 0:
                print(f"[*] No pagination found or empty page. Stopping.")
                break
            
            page += 1
            
            # Be polite - add a small delay between requests
            time.sleep(1)
            
        except requests.exceptions.RequestException as e:
            print(f"[!] Error fetching page {page}: {e}")
            break
        except Exception as e:
            print(f"[!] Error parsing page {page}: {e}")
            break
    
    # Save results
    print(f"\n[*] Total doctors scraped: {len(all_doctors)}")
    
    # Output to JSON file
    output_file = f"hospital_doctors_{hospital_filter}_present.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(all_doctors, f, indent=4, ensure_ascii=False)
    
    print(f"[*] Data saved to {output_file}")
    
    # Also print to console for immediate view
    print("\n" + "="*60)
    print("SCRAPED DATA:")
    print("="*60)
    print(json.dumps(all_doctors, indent=2, ensure_ascii=False))
    
    return all_doctors

if __name__ == "__main__":
    # You can change the hospital here
    hospital = "hospital-san-rafael"  # Options: hospital-santa-maria-del-puerto, hospital-virgen-de-la-bella, etc.
    
    if len(sys.argv) > 1:
        hospital = sys.argv[1]
    
    scrape_hospital_doctors(hospital_filter=hospital)
