# 🌍 Global Warming and Ocean Impact Analysis

Exploratory Data Analysis (EDA) on global warming trends — analyzing land temperature changes from 1750-2015 and their relationship with ocean temperature, using real historical climate data.

## 📊 Project Overview

This project analyzes the **Berkeley Earth Surface Temperature dataset** to understand:
- How global land temperatures have changed over 265 years
- Which decades saw the sharpest temperature increases
- Which countries have warmed the most
- Seasonal temperature patterns
- The relationship between land and ocean temperature trends

## 🔑 Key Findings

- **Overall Trend:** Global land temperature has risen significantly since 1750, with a sharp, steady increase visible from ~1975 onwards — consistent with modern climate change.
- **Sharpest Decadal Rise (Land):** The 1820s showed the sharpest increase (+0.93°C), though early data has higher uncertainty.
- **Sharpest Decadal Rise (Land+Ocean):** The 2000s decade shows the highest combined land-ocean temperature on record.
- **Top Warming Countries:** Using decade-averaged comparisons (first 10 years vs last 10 years), **Uzbekistan (+13.9°C)** and **Turkmenistan (+12.2°C)** show the highest warming, followed by China, Egypt, and UAE — predominantly arid/continental climates.
- **Seasonal Pattern:** Global temperatures peak in **July** (~14.3°C) and are lowest in **January** (~2.3°C), reflecting the dominance of Northern Hemisphere land mass.
- **Historical Anomaly:** A notable temperature dip around 1810-1820 aligns with the Mount Tambora volcanic eruption (1815), which caused global cooling.

## 🛠️ Tech Stack

- **Python** - Core language
- **Pandas & NumPy** - Data loading, cleaning, analysis
- **Matplotlib** - Static visualizations
- **Plotly** - Interactive visualizations
- **Seaborn** - Statistical visualizations
- **Kaggle API** - Automated dataset download

## 📂 Project Structure
Global-Warming-And-Ocean-Impact-Analysis/

├── analysis/

│   ├── data_loader.py      # Loads and cleans raw data

│   ├── eda.py               # Exploratory data analysis

│   └── visualizations.py    # Interactive & static charts

├── data/                     # Dataset (downloaded, not in repo)

├── download_data.py          # Auto-downloads dataset via Kaggle API

├── requirements.txt           # Python dependencies

└── README.md

## 🚀 Setup & Usage

1. **Clone the repository**
```bash
git clone https://github.com/anshikaraj-hub/Global-Warming-And-Ocean-Impact-Analysis.git
cd Global-Warming-And-Ocean-Impact-Analysis
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Set up Kaggle API**
   - Go to Kaggle → Settings → API → Create New Token
   - Place `kaggle.json` in `~/.kaggle/` (or `C:\Users\<you>\.kaggle\` on Windows)

4. **Download the dataset**
```bash
python download_data.py
```

5. **Run the analysis**
```bash
cd analysis
python data_loader.py    # Load & clean data
python eda.py             # Run exploratory analysis
python visualizations.py  # Generate charts
```

## 📈 Data Source

[Climate Change: Earth Surface Temperature Data](https://www.kaggle.com/datasets/berkeleyearth/climate-change-earth-surface-temperature-data) by Berkeley Earth (Kaggle)

## 📝 Notes

- This project initially assumed data covered 1750-2013, but validation showed the actual range is **1750-2015**.
- Ocean temperature data is only available from ~1850 onwards due to historical measurement limitations.
- Country-level warming was calculated by comparing decade-averaged temperatures (first 10 years vs last 10 years) to avoid seasonal bias from single-point comparisons.

## 📄 License

MIT License

## 📓 Interactive Notebook

View the full analysis with interactive Plotly charts on Kaggle:
[🌍 Global Warming and Ocean Impact Analysis (1750-2015)]
((https://www.kaggle.com/code/anshikarajhub/global-warming-and-ocean-impact-analysis-1750-201))
