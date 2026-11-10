# Knowledge Graph-Enhanced Aspect-Based Sentiment Analysis for Nigerian Pidgin and Code-Switched App Reviews

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JulietChinenyeDuru/KG-SentIF-Knowledge-Graph-Enhanced-Sentiment-Analysis-for-Nigerian-Social-Media-Text/blob/main/notebooks/google_play_reviews.ipynb)
![Status](https://img.shields.io/badge/status-in%20progress-orange)

**KG-SentIF** (Knowledge Graph-Enhanced Sentiment Intelligence Framework) studies whether structured local knowledge helps sentiment models understand Nigerian user reviews, where English, Nigerian Pidgin, Igbo, Yoruba and Hausa are mixed in a single post.

> *"This app sweet well well, but the transfer no dey go at all."*
> Positive about the app, negative about transfers. A single star rating hides this; aspect-based sentiment analysis captures both.

## Aims

1. Build **NaijaABSA**, an aspect-level sentiment corpus of Nigerian Pidgin and code-switched **Google Play app reviews** in four domains: telecoms, banking, electricity and e-commerce.
2. Measure how well **Wikidata** and **ConceptNet** cover the brands, services and expressions in these reviews, and build a verified **local lexicon** for what they miss.
3. Compare fine-tuned multilingual encoders (XLM-R, AfroXLMR), **open-weight LLMs** with and without knowledge-graph retrieval, and **KG-SentIF**, a graph-attention model that fuses text with retrieved knowledge.
4. Release the annotations, guidelines and code openly.

## Data source

Reviews are collected from the public Google Play pages of these Nigerian apps, for Nigerian users (`country="ng"`):

| Domain | Apps |
|---|---|
| Telecoms | myMTN NG, Glo Cafe Nigeria |
| Banking and fintech | FirstMobile (First Bank), Moniepoint Business |
| Electricity | Ikeja Electric, BuyPower, Powerlight |
| E-commerce | Jumia, Jiji Nigeria |

Collection uses the open-source [google-play-scraper](https://pypi.org/project/google-play-scraper/) library. No login or API key is needed.

## Status

| Stage | Status |
|---|---|
| Google Play review collection | In progress |
| Pidgin filtering and sampling | Planned |
| Annotation guidelines and pilot annotation | Planned |
| Knowledge-coverage analysis | Planned |
| Baselines and KG-SentIF experiments | Planned |
| Paper | In preparation |

## Repository structure

```text
KG-SentIF-Knowledge-Graph-Enhanced-Sentiment-Analysis-for-Nigerian-Social-Media-Text/
  notebooks/        # Colab notebooks (google_play_reviews.ipynb ...)
  src/              # one script per step: parse.py, 04_agreement.py, 05_wikidata.py ...
  kg/               # knowledge-graph links and the local lexicon
  guidelines/       # annotation guidelines (PDF)
  data/             # annotations only (review IDs + labels); raw review text is not stored here
  results/          # model predictions and scores
  requirements.txt
```

## Getting started

Open the collection notebook in Google Colab with the badge above, or run it locally:

```bash
git clone https://github.com/JulietChinenyeDuru/KG-SentIF-Knowledge-Graph-Enhanced-Sentiment-Analysis-for-Nigerian-Social-Media-Text.git
cd KG-SentIF-Knowledge-Graph-Enhanced-Sentiment-Analysis-for-Nigerian-Social-Media-Text
pip install -r requirements.txt
```

All tools and models used are free and open source.

## Data and ethics

- Reviews come from public Google Play pages. **Reviewer names are never stored**; phone numbers, emails, handles and personal names are removed before annotation.
- Review text belongs to its authors, so this repository releases **review IDs and annotations only**, with a script to re-download the text.
- Annotation is carried out by paid, consenting native speakers under institutional ethics approval.

## Citation

A citation will be added when the paper is published. Until then, please cite this repository:

```bibtex
@misc{duru2026kgsentif,
  author = {Duru, Juliet Chinenye},
  title  = {Knowledge Graph-Enhanced Aspect-Based Sentiment Analysis for Nigerian Pidgin and Code-Switched App Reviews},
  year   = {2026},
  url    = {https://github.com/JulietChinenyeDuru/KG-SentIF-Knowledge-Graph-Enhanced-Sentiment-Analysis-for-Nigerian-Social-Media-Text}
}
```

## Licence

- Code: MIT
- Annotations and guidelines: CC BY 4.0 (CC BY-SA 4.0 for any lexicon entries derived from ConceptNet)

## Author

**Juliet Chinenye Duru** · ORCID [0009-0002-0530-8082](https://orcid.org/0009-0002-0530-8082)
