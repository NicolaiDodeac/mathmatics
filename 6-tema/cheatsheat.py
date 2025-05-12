from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        self.set_font("DejaVu", 'B', 14)
        self.cell(0, 10, "Підсумки з теорії ймовірностей", ln=True, align="C")

# Створення PDF
pdf = PDF()
pdf.add_font("DejaVu", "", "DejaVuSans.ttf", uni=True)
pdf.add_font("DejaVu", "B", "DejaVuSans-Bold.ttf", uni=True)
pdf.set_font("DejaVu", size=11)
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)

# Додай шрифт DejaVu Sans (його треба завантажити в проєкт)


lines = [
    "1. Навіщо потрібна теорія ймовірностей:",
    "- Допомагає приймати рішення в умовах невизначеності.",
    "- Використовується в аналітиці, фінансах, медицині, машинному навчанні.",
    "",
    "2. Основні поняття:",
    "- Випадкова подія — те, що може статись або не статись.",
    "- Простір подій Ω — усі можливі результати експерименту.",
    "- Ймовірність події — число від 0 до 1.",
    "- Випадкова величина — числове значення результату події.",
    "",
    "3. Комбінаторика:",
    "- Перестановки — порядок важливий, використовуються всі елементи.",
    "- Комбінації — порядок неважливий, використовуються не всі.",
    "- Розміщення — порядок важливий, використовуються не всі.",
    "",
    "4. Основні правила ймовірності:",
    "- Сума: P(A ∪ B) = P(A) + P(B) – P(A ∩ B)",
    "- Добуток: P(A ∩ B) = P(A) · P(B | A)",
    "- Протилежна подія: P(¬A) = 1 – P(A)",
    "",
    "5. Формула Байєса:",
    "P(A|B) = [P(B|A) * P(A)] / P(B)",
    "",
    "6. Розподіли випадкових величин:",
    "- Біноміальний — кількість успіхів у серії спроб.",
    "- Геометричний — кількість спроб до першого успіху.",
    "- Рівномірний — всі значення однаково ймовірні.",
    "- Нормальний — симетричний, має форму дзвону.",
    "- Експоненційний — час до настання події.",
    "",
    "7. Числові характеристики:",
    "- Математичне сподівання: E(X) = Σ xᵢ·P(xᵢ)",
    "- Дисперсія: D(X) = E[(X – E(X))²]",
    "- Середнє квадратичне відхилення: σ = √D(X)",
    "",
    "8. Приклад в Python:",
    "- Вибірки: np.random.binomial(), normal()",
    "- Графіки: matplotlib, seaborn",
    "- Статистика: mean(), std(), describe()",
    "- Перевірка розподілу: chisquare(), normaltest()",
    "",
    "Застосування:",
    "- Дані: аналіз трендів, перевірка гіпотез.",
    "- IT/ML: робота з ймовірностями.",
    "- Медицина: дослідження ефективності."
]

for line in lines:
    pdf.multi_cell(0, 8, line)

pdf.output("Pidsumky_Ymovirnostei_UKR.pdf")


# from fpdf import FPDF

# # Створюємо PDF, уникаючи символів не з latin-1
# def clean_text(text):
#     return text.encode('latin-1', 'ignore').decode('latin-1')

# class PDF(FPDF):
#     def header(self):
#         self.set_font("Arial", 'B', 14)
#         self.cell(0, 10, "Pidsumky z teorii ymovirnostei", ln=True, align="C")

# pdf = PDF()
# pdf.add_page()
# pdf.set_auto_page_break(auto=True, margin=15)
# pdf.set_font("Arial", size=11)

# lines = [
#     "1. Navishcho potribna teoriya ymovirnostei:",
#     "- Dopomahaie pryimaty rishennya v umovakh nevyznachenosti.",
#     "- Vikorystovuietsia v analitytsi, finansakh, medytsyni, ML ta IT.",
#     "",
#     "2. Osnovni ponyattya:",
#     "- Vypadkova podiya — shchos', shcho mozhe statys' abo ni.",
#     "- Prostir podii Ω — vsi mozhlyvi rezultaty.",
#     "- Ymovirnist' podii — chyslo vid 0 do 1.",
#     "- Vypadkova velychyna — chyslove znachennya podii.",
#     "",
#     "3. Kombinatoryka:",
#     "- Perestanovky — vazhlyvyi poryadok usikh elementiv.",
#     "- Kombinatsii — vazhlyvo lyshe, yaki obrani, ne yikh poryadok.",
#     "- Rozmishchennia — poryadok vazhlyvyi, berutsia ne vsi.",
#     "",
#     "4. Pravila ymovirnosti:",
#     "- Suma: P(A ∪ B) = P(A) + P(B) – P(A ∩ B)",
#     "- Dobutok: P(A ∩ B) = P(A) · P(B | A)",
#     "- Protylezhna podiya: P(¬A) = 1 – P(A)",
#     "",
#     "5. Formula Bayesa:",
#     "P(A|B) = [P(B|A) * P(A)] / P(B)",
#     "",
#     "6. Rozpodily vypadkovykh velychyn:",
#     "- Binomialnyi — kilkist' uspikhiv u serii sprobu.",
#     "- Heometrychnyi — sproby do pershoho uspikhu.",
#     "- Rivnomirnyi — vsi znachennia odnakovo ymovirni.",
#     "- Normalnyi — symetrychnyi, dzvinopodibnyi.",
#     "- Eksponentsialnyi — chas do podii.",
#     "",
#     "7. Chyslovi kharakterystyky:",
#     "- Matematychne ochikuvannia: E(X) = Σ xᵢ·P(xᵢ)",
#     "- Dispersiia: D(X) = E[(X – E(X))²]",
#     "- Seredn'okvadratychne vidkhylennia: σ = √D(X)",
#     "",
#     "8. Praktyka v Python:",
#     "- Vypadkovi vybirky: np.random.binomial(), normal()",
#     "- Vizualizatsiia: matplotlib, seaborn",
#     "- Statystyka: mean(), std(), describe()",
#     "- Perevirka rozpodilu: chisquare(), normaltest()",
#     "",
#     "Zastosuvannia:",
#     "- Dani: analiz trendiv, perevirka hipotez.",
#     "- IT/ML: robota z ymovirnostiamy.",
#     "- Medytsyna: doslidzhennia efektyvnosti."
# ]

# for line in lines:
#     pdf.multi_cell(0, 8, clean_text(line))

# # Збереження PDF
# pdf_output_path = "Pidsumky_Ymovirnostei.pdf"
# pdf.output(pdf_output_path)
