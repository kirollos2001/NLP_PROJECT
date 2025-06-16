"""
Cleaning & Preprocessing utilities
"""

def clean_arabic_transcript(file_path: str) -> str:
    """
    Simple and effective Arabic transcript cleaner
    """

    # Read the file
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # 1. Structure by speakers
    lines = text.strip().split('\n')
    cleaned_lines = []

    for line in lines:
        line = line.strip()
        if not line:
            continue

        # Replace speaker labels with clear names
        if line.startswith('[SPEAKER_00]:'):
            line = line.replace('[SPEAKER_00]:', '**المحاور:**')
        elif line.startswith('[SPEAKER_01]:'):
            line = line.replace('[SPEAKER_01]:', '**د. أشرف إبراهيم:**')

        # Skip subscription calls
        if 'اشتركوا في القناة' in line:
            continue

        cleaned_lines.append(line)

    text = '\n'.join(cleaned_lines)

    # 2. Fix common transcription errors
    fixes = {
        'المخبل الاقتصادي': 'المخبر الاقتصادي',
        'أشوف إبراهيم': 'أشرف إبراهيم',
        'معاي': 'معي',
        'كده': 'هكذا',
        'دلوقتي': 'الآن',
        'إيه': 'ما',
        'إزاي': 'كيف',
        'ليه': 'لماذا',
        'حاجة': 'شيء',
        'علشان': 'لأن'
    }

    for old, new in fixes.items():
        text = text.replace(old, new)

    # 3. Clean up excessive filler words
    text = re.sub(r'\s+يعني\s+', ' ', text)  # Remove excessive "يعني"
    text = re.sub(r'\s+بقى\s+', ' ', text)   # Remove "بقى"

    # 4. Fix spacing and formatting
    text = re.sub(r'\s+', ' ', text)  # Multiple spaces to single
    text = re.sub(r'\n+', '\n', text)  # Multiple newlines to single
    text = re.sub(r'\*\*([^*]+)\*\*\s*', r'\n\n**\1**\n', text)  # Format speaker names

    # 5. Add context header
    header = """## مقابلة مع د. أشرف إبراهيم - المخبر الاقتصادي

**الموضوع:** صناعة المحتوى الاقتصادي على المنصات الرقمية وفرض الضرائب على اليوتيوبرز
**السنة:** 2021

---

"""

    return header + text.strip()

# Quick usage
def process_your_file():
    input_path = "/content/audio.txt"

    try:
        cleaned_text = clean_arabic_transcript(input_path)

        # Save cleaned version
        with open("/content/cleaned_audio.txt", 'w', encoding='utf-8') as f:
            f.write(cleaned_text)

        print("✅ File cleaned successfully!")
        print(f"📄 Cleaned text length: {len(cleaned_text)} characters")

        # Show preview
        print("\n📋 Preview:")
        print(cleaned_text[:300] + "..." if len(cleaned_text) > 300 else cleaned_text)

        return cleaned_text

    except Exception as e:
        print(f"❌ Error: {e}")
        return ""

# Run the cleaning
if __name__ == "__main__":
    cleaned_text = process_your_file()import google.generativeai as genai

genai.configure(api_key="AIzaSyAppgKucqySxNQFIIVEWi0RyOlepaA9qe4")

model = genai.GenerativeModel(model_name="models/gemini-2-flash")

# Read the input Arabic text
file_path = "/content/cleaned_audio.txt"
with open(file_path, 'r', encoding='utf-8') as file:
    arabic_text = file.read()

# Prompt Gemini to summarize in Egyptian Arabic
prompt = f"""
عايزك تلخصلي الكلام الجاي ده باللهجة المصرية، وخلي الأسلوب بسيط وسهل:

{arabic_text}

الملخص باللهجة المصرية:"""

# Generate the summary
response = model.generate_content(prompt)

# Extract the text output
summary = response.text

# Save the summary to summary.txt
output_path = "/content/summary.txt"
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(summary)

# Print confirmation and preview
print("✅ Summary saved to summary.txt\n")
print("📄 Preview of the summary:")
print(summary[:500])  # Print the first 500 charactersfrom huggingface_hub import snapshot_download
snapshot_download(repo_id="OmarSamir/EGTTS-V0.1", local_dir="/content/EGTTS-V0.1")from IPython.display import Audio, display
import torch
