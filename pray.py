import itertools
import argparse

def get_alphabet(language):
    alphabets = {
    'english': 'abcdefghijklmnopqrstuvwxyz',
    'french': 'abcdefghijklmnopqrstuvwxyz',
    'spanish': 'abcdefghijklmnñopqrstuvwxyz',
    'italian': 'abcdefghilmnopqrstuvz',
    'russian': 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя',
    'arabic': 'ابتثجحخدذرزسشصضطظعغفقكلمنهوي',
    'hebrew': 'אבגדהוזחטיכלמנסעפצקרשת',
    'german': 'abcdefghijklmnopqrstuvwxyzäöüß',
    'greek': 'αβγδεζηθικλμνξοπρστυφχψω',
    'japanese': 'あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん',
    'korean': 'ㄱㄴㄷㄹㅁㅂㅅㅇㅈㅊㅋㅌㅍㅎㅏㅑㅓㅕㅗㅛㅜㅠㅡㅣ',
    }

    return ''.join([char for char in alphabets.get(language.lower(), '')])

def generate_god_name(alphabet, max_length):
    for length in range(1, max_length + 1):
        for combination in itertools.product(alphabet, repeat=length):
            yield ''.join(combination)

def pray(name):
    prayer = f"""O {name}, source of all light and life, master of the universe,

I humbly express my profound gratitude for the boundless gifts bestowed upon me — the beauty of nature, the warmth of community, and the spark of life itself.

In this moment of reflection, I seek your guidance and wisdom. Illuminate my path with compassion and understanding, that I may walk in harmony with all beings.

Grant me the strength to face challenges with courage and the capacity to recognize the light within myself and others.

May I be a vessel of love, peace, and healing in the world, acting with kindness and respect towards all creation.

Bless me with the vision to see beyond humanity’s differences, finding unity in our shared humanity.

In seeking connection with the divine, let me be mindful of the mysteries that lie beyond my understanding, approaching life with wonder and reverence.

Amen.
"""
    print(prayer)

def main():
    parser = argparse.ArgumentParser(description="Generate prayers for names based on language alphabets.")
    parser.add_argument("--language", type=str, help="Specify the language for the alphabet.")
    args = parser.parse_args()

    # Simulate fetching the alphabet for the specified language and excluding vowels and symbols
    alphabet = get_alphabet(args.language)

    for name in generate_god_name(alphabet, 8):
        pray(name)

if __name__ == "__main__":
    main()
