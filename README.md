# Knowledge Graph-Enhanced Aspect-Based Sentiment Analysis for Nigerian Pidgin and Code-Switched App Reviews

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JulietChinenyeDuru/KG-SentIF-Knowledge-Graph-Enhanced-Sentiment-Analysis-for-Nigerian-Social-Media-Text/blob/main/notebooks/naijaabsa_collect_10_sectors.ipynb)
![Status](https://img.shields.io/badge/status-annotation%20in%20progress-orange)

**KG-SentIF** (Knowledge Graph-Enhanced Sentiment Intelligence Framework) studies whether structured local knowledge helps sentiment models understand Nigerian app reviews, where English, Nigerian Pidgin, Igbo, Yoruba and Hausa are mixed in a single post.

> *"This app sweet well well, but the transfer no dey go at all."*
> Positive about the app, negative about transfers. A single star rating hides this; aspect-based sentiment analysis captures both.

## Aims

1. Build **NaijaABSA**, an aspect-level sentiment dataset of Nigerian Pidgin and code-switched **Google Play app reviews** across ten service sectors.
2. Measure how well **Wikidata** and **ConceptNet** cover the brands, services and expressions in these reviews, and build a verified **local lexicon** for what they miss.
3. Compare fine-tuned multilingual encoders (XLM-R, AfroXLMR), **open-weight LLMs** with and without knowledge-graph retrieval, and **KG-SentIF**, a graph-attention model that fuses text with retrieved knowledge.
4. Release the annotations, guidelines and code openly.

## Data

| Step | Reviews |
|---|---|
| Public Google Play reviews collected from 32 Nigerian apps | 407,246 |
| Reviews containing Nigerian Pidgin markers | 2,526 |
| After removing foreign-language reviews (mainly Spanish) | **2,351** |

**Reviews per sector**

| Sector | Apps | Reviews |
|---|---|---|
| Banking and fintech | FirstMobile, GTWorld, Access More, UBA, Moniepoint, OPay, Kuda, PalmPay | 1,147 |
| Telecoms | myMTN NG, Glo Cafe, My Airtel | 562 |
| Government services | NIMC MWS | 191 |
| E-commerce | Jumia, Konga, Jiji | 162 |
| Pay-TV and streaming | MyDStv, MyGOtv, GOtv Stream, DStv Stream | 123 |
| Electricity | Ikeja Electric, BuyPower, Powerlight (plus electricity complaints on banking and telecoms apps) | 49 |
| Food delivery | Chowdeck, Glovo | 49 |
| Ride-hailing | Bolt, inDrive, Uber | 36 |
| Travel | Air Peace, GIG Mobility, Wakanow | 24 |
| Education | uLesson | 8 |
| **Total** | | **2,351** |

Reviews date from 2014 to November 2026, most from 2021 onwards.

## Annotation

Each review is labelled for every aspect the writer judges: the aspect words, one of **12 categories** (product overall, core service, price and fees, payments and transactions, refunds and reversals, delivery and timing, staff and drivers, product and content quality, customer service, app performance, login and account, trust and safety) and a polarity (positive, negative, neutral). Reviews are also tagged for sarcasm, cultural reference and language.

- A first batch of 100 reviews is labelled by two annotators to test the guidelines.
- A shared set of 200 reviews is labelled by all five annotators to measure agreement.
- The remaining reviews are each labelled by one annotator.

Full rules: [guidelines/README.md](guidelines/README.md) · [PDF](guidelines/NaijaABSA_Annotation_Guidelines.pdf)

## Status

| Stage | Status |
|---|---|
| Review collection and cleaning | Done |
| Annotation guidelines | Done |
| First-batch annotation | In progress |
| Main annotation | Planned |
| Knowledge-coverage analysis | Planned |
| Baselines and KG-SentIF experiments | Planned |
| Paper | In preparation |

## Repository structure

```text
notebooks/   naijaabsa_collect_10_sectors.ipynb  - collect, filter and clean the reviews
annotation/  make_annotation_sheet.py            - builds annotation sheets with dropdowns
             NaijaABSA_annotation_template.xlsx  - empty template with worked examples
guidelines/  README.md and PDF                   - annotation guidelines
data/        review_ids.csv                      - review IDs, app, sector and date (no text)
scripts/     rehydrate_reviews.py                - re-downloads review text from the IDs
```

## Getting the review text

To respect reviewers' ownership of their words, this repository publishes **review IDs only**. To rebuild the texts:

```bash
pip install -r requirements.txt
python scripts/rehydrate_reviews.py data/review_ids.csv naijaabsa_reviews_rehydrated.csv
```

Reviews deleted by their authors since collection cannot be recovered.

## Data and ethics

- Only public Google Play reviews are used. **Reviewer names are never stored**; phone numbers, emails, ID numbers, handles and links are removed before annotation.
- Annotation is carried out by volunteer native speakers who gave informed consent, under institutional ethics review.

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

- Code: MIT (see [LICENSE](LICENSE))
- Annotations and guidelines: CC BY 4.0

## Author

**Juliet Chinenye Duru** · ORCID [0009-0002-0530-8082](https://orcid.org/0009-0002-0530-8082)

