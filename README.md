## Analiza danych -projektu w Python 

Ten projekt pokazuje:
- prace z danymi (pandas),
- czyszczenie danych,
- analize statystyczną,
- wizualizacje (matplotlib),
- strukture projektu data science.
 
## Struktura projektu

movie_analysis/
├── data/
│   └── raw/              # surowe dane
├── notebooks/            # notatniki Jupyter
├── reports/
│   └── figures/          # wykresy
├── src/
│   ├── load_data.py
│   ├── clean_data.py
│   ├── analyze.py
│   └── visualize.py
├── main.py
└── requirements.txt

## Technologie 

- Python 3.9+
- pandas
- numpy
- matplotlib
- seaborn
- Jupyter Notebook
- Visual Studio Code

## Funkcjolaności

- wczytywanie danych z pliku CSV
- czyszczenie danych (usuwanie braków, filtrowanie)
- podstawowa analiza statystyczna
- generowanie wykresów
- uporządkowana struktura projektu data science 

## Uruchomienie 

```bash
python3 -m venv venv
source venv/bin/activate
pip instal -r requirements.txt
python main.py


