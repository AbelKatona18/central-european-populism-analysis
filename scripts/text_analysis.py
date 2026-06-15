import os
import re

def parse_and_clean_corpus(file_path):
    if not os.path.exists(file_path):
        return []
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    if "METADATA_END" in content:
        speech_body = content.split("METADATA_END")[-1]
    else:
        speech_body = content
    speech_body = speech_body.lower()
    return re.findall(r'\b\w+\b', speech_body)

def run_epistemic_metrics(words, file_name):
    total_words = len(words)
    if total_words == 0:
        return None
        
    absolute_markers = {
        'always', 'never', 'eternal', 'cosmic', 'divine', 'empire', 
        'siege', 'betrayer', 'sacrilege', 'blasphemy', 'absolute', 
        'all', 'sovereignty', 'sacred', 'historical'
    }
    
    empirical_markers = {
        'data', 'percent', 'numbers', 'facts', 'audit', 'contract', 
        'procurement', 'court', 'billion', 'forint', 'ministry', 'laws', 
        'judiciary', 'institutions', 'accountable', 'referendum'
    }
    
    abs_count = sum(1 for w in words if w in absolute_markers)
    emp_count = sum(1 for w in words if w in empirical_markers)
    
    abs_density = (abs_count / total_words) * 100
    emp_density = (emp_count / total_words) * 100
    
    print(f"| {file_name:<35} | {total_words:<12} | {abs_density:<12.3f}% | {emp_density:<12.3f}% |")
    return abs_density, emp_density

def process_survey_data(csv_path):
    if not os.path.exists(csv_path):
        print(f"\n[ERROR]: Survey file not found at {csv_path}")
        return
        
    with open(csv_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()[1:]
        
    hu_gov, hu_eu, hu_jud, hu_med, hu_dem, hu_ele = [], [], [], [] ,[], []
    int_gov, int_eu, int_jud, int_med, int_dem, int_ele = [], [], [], [], [], []
    
    for line in lines:
        parts = line.strip().split(',')
        if len(parts) >= 10:
            country = parts[1]
            # Standardize variations in input formatting
            is_hu = "hungary" in country.lower()
            
            # Map parameters safely, defaulting missing trailing values
            gov = int(parts[3])
            jud = int(parts[4])
            med = int(parts[6])
            eu  = int(parts[7])
            dem = int(parts[8]) if parts[8].isdigit() else 3
            ele = int(parts[9]) if parts[9].isdigit() else 3
            
            if is_hu:
                hu_gov.append(gov)
                hu_eu.append(eu)
                hu_jud.append(jud)
                hu_med.append(med)
                hu_dem.append(dem)
                hu_ele.append(ele)
            else:
                int_gov.append(gov)
                int_eu.append(eu)
                int_jud.append(jud)
                int_med.append(med)
                int_dem.append(dem)
                int_ele.append(ele)
                
    n_hu = len(hu_gov)
    n_int = len(int_gov)
    
    print("\n" + "="*65)
    print(f"SOCIOLOGICAL LOCALIZED ADOLESCENT SURVEY ANALYSIS (N={n_hu + n_int} TOTAL)")
    print("="*65)
    print(f"--> HUNGARIAN CLUSTER TARGET (N={n_hu} Participants - Eastern Region)")
    print(f"    Mean Trust in National Government (1-5 Scale): {sum(hu_gov)/n_hu:.2f} / 5.0")
    print(f"    Mean Trust in European Union (1-5 Scale):       {sum(hu_eu)/n_hu:.2f} / 5.0")
    print(f"    Mean Trust in Regional Judiciary (1-5 Scale):   {sum(hu_jud)/n_hu:.2f} / 5.0")
    print(f"    Mean Trust in State-Run News Media (1-5 Scale): {sum(hu_med)/n_hu:.2f} / 5.0")
    print(f"    Perceived Democratic Reality Score (1-5 Scale): {sum(hu_dem)/n_hu:.2f} / 5.0")
    print(f"    Perceived Fair Election Score (1-5 Scale):      {sum(hu_ele)/n_hu:.2f} / 5.0")
    print("-"*65)
    print(f"--> INTERNATIONAL CONTROL GROUP (N={n_int} Participants - Global Node)")
    print(f"    Mean Trust in Local Government (1-5 Scale):     {sum(int_gov)/n_int:.2f} / 5.0")
    print(f"    Mean Trust in European Union (1-5 Scale):       {sum(int_eu)/n_int:.2f} / 5.0")
    print(f"    Perceived Democratic Reality Score (1-5 Scale): {sum(int_dem)/n_int:.2f} / 5.0")
    print("="*65)

if __name__ == "__main__":
    orban_speeches = [
        "data_raw/orban/orban_2014_balvanyos.txt",
        "data_raw/orban/orban_2023_state_of_the_nation.txt",
        "data_raw/orban/orban_2025_state_of_the_nation.txt"
    ]
    magyar_speeches = [
        "data_raw/magyar/magyar_2024_march_rally.txt",
        "data_raw/magyar/magyar_2026_march_rally.txt",
        "data_raw/magyar/magyar_2026_victory_speech.txt"
    ]
    
    print("\n" + "="*82)
    print(f"{'File Name':<37} | {'Word Count':<12} | {'Absolute Den':<12} | {'Empirical Den':<12} |")
    print("="*82)
    
    print("\n[THESIS: VIKTOR ORBAN CORPUS]")
    for path in orban_speeches:
        tokens = parse_and_clean_corpus(path)
        run_epistemic_metrics(tokens, os.path.basename(path))
        
    print("\n[SYNTHESIS: PETER MAGYAR CORPUS]")
    for path in magyar_speeches:
        tokens = parse_and_clean_corpus(path)
        run_epistemic_metrics(tokens, os.path.basename(path))
        
    process_survey_data("data_survey/raw_responses.csv")
