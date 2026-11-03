# MediBot v2

RAG assistant over medical PDFs. Answers with source and page, and says "not found in sources" when the documents do not contain the answer. Main goal: measure retrieval and answer quality with a 30-question test set.

> Educational only, not medical advice.

## Scope
TODO: topics covered (fill after Step 2)

## Example questions
TODO: 4-5 questions that work

## Sources (PDFs are NOT in this repo)
| Name | Publisher | Licence | Link |
|---|---|---|---|
| MSF Clinical Guidelines (Oct 2023 PDF) | MSF | All rights reserved | https://medicalguidelines.msf.org/en/node/170 |
| MSF Essential Drugs (2024) | MSF | All rights reserved | https://medicalguidelines.msf.org/en/node/339 |
| WHO Hypertension Guideline 2021 | WHO | CC BY-NC-SA 3.0 IGO | https://www.who.int/publications-detail-redirect/9789240033986 |
| Where There Is No Doctor (2009 ed.) | Hesperian | Non-commercial copying with credit, see Hesperian open copyright | https://www.pseau.org/outils/ouvrages/hesperian_where_there_is_no_doctor.pdf |

Documents are indexed for retrieval. The model is not trained on them.

## Setup
1. Download the 4 PDFs into `data/`
2. Create `.env` with `GROQ_API_KEY`
3. Run the ingest script (TODO)

## Results
TODO: before/after table (Step 10)

## Limitations
TODO