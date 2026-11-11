# NaijaABSA Annotation Guidelines

Prepared by **Juliet Chinenye Duru** · November 2026

These guidelines explain how to label Nigerian app reviews for the NaijaABSA research dataset. Read them fully before you start, and keep them open while you work. A printable version is in [`NaijaABSA_Annotation_Guidelines.pdf`](NaijaABSA_Annotation_Guidelines.pdf).

## 1. Purpose

You will read Google Play reviews of Nigerian apps (telecoms, banking, electricity and online shopping) and record **what each writer gives an opinion about** and **whether that opinion is positive, negative or neutral**. Many reviews are in Nigerian Pidgin or mix English with Pidgin, Igbo, Yoruba or Hausa.

Your labels become the correct answers that AI models learn from and are tested against. Careful, consistent labels matter more than speed.

**What you need:** a phone or laptop with internet, access to your own Google Sheet (shared with you by the researcher), and about 30–60 seconds per review.

## 2. How to annotate one review

Work on the **Annotate** tab. Fill only the yellow cells; never change the green example rows or the review text.

1. **Read the whole review** in column C, once for meaning and once for detail.
2. **Decide whether it gives any opinion** about the product or service. If not, write `no opinion` in **Notes** and move on (Section 6).
3. **Find each aspect**: each thing the writer judges (Section 3). For up to three aspects:
   - type the aspect's **exact words** from the review in *Aspect 1*, *2* or *3*;
   - choose its **Category** from the dropdown (Section 4);
   - choose its **Polarity** from the dropdown (Section 5).
4. **If the writer judges something they never name in words**, fill *Implied aspect category* and *Implied aspect polarity* instead.
5. **Choose yes or no** for *Sarcastic?* and *Cultural reference?* (Section 5).
6. **Choose the Language** (Section 6).
7. **Use Notes** for anything unclear, so the researcher can review it. Never leave a review half done.

## 3. Aspects

An **aspect** is the specific thing the writer has an opinion about: a feature, a service, a part of the experience. *Transfer*, *data*, *network*, *customer care*, *token*, *delivery* and *app* are typical aspects.

**Rules for explicit aspects (named in words)**

- Copy the words **exactly as written**, including Pidgin spelling (*netwok*, *custmer care*).
- Mark the **shortest phrase** that names it: *battery*, not *the battery of this phone*; *customer care*, not *their customer care people*.
- If the same aspect is mentioned twice, mark it **once**.
- If the writer judges the app or service as a whole (*"This app sweet"*, *"Worst bank"*), the aspect is that word (*app*, *bank*) and the category is **product overall**.
- Do **not** mark words that carry no opinion: in *"I used the app to buy data and it failed"*, the opinion is about the **data** purchase failing, not about *app*.
- If there are more than three aspects, mark the **three with the clearest opinion**, and write "more aspects" in Notes.

**Implied aspects (not named in words)**

Sometimes the writer clearly judges something without naming it. *"Na so una dey do every time, abeg do better"* on an electricity app is a complaint about **power supply**, but no word says so. Leave the Aspect columns empty and fill *Implied aspect category* and *Implied aspect polarity*. Only do this when you are confident what is being judged; if you are guessing, write your thought in Notes instead.

## 4. Categories

Choose the **one category** that best describes each aspect. If two seem to fit, pick the more specific one (*transfers and payments* rather than *app performance* for a failed transfer).

| Category | Use it for | Example |
| --- | --- | --- |
| product overall | The app, bank, network or company as a whole | *"Best bank app for Naija"* |
| price | How expensive or cheap something is | *"Their data plan too cost"* |
| network or coverage | Signal, calls dropping, no service | *"Network no dey for my area"* |
| data and airtime | Data bundles, airtime, data finishing fast | *"Data dey finish like water"* |
| customer service | Support staff, call centre, replies, complaints handling | *"Custmer care no dey pick call"* |
| app performance | Crashes, slowness, bugs, updates, design | *"App dey hang since update"* |
| login and security | Login, OTP, PIN, account blocked, fraud | *"OTP no dey come"* |
| transfers and payments | Sending, receiving, paying bills, failed or pending transactions | *"Transfer pending since yesterday"* |
| fees and charges | Bank charges, deductions, hidden fees | *"Dem dey remove money anyhow"* |
| power supply | Electricity availability, outages, "light" | *"No light for two days"* |
| billing and metering | Electricity bills, estimated billing, meters | *"Dem dey give us crazy bill"* |
| token and recharge | Buying electricity units, tokens not arriving or not loading | *"Token no load for my meter"* |
| delivery | Shipping, delivery time, riders | *"Delivery fast, I like am"* |
| product quality | The quality of goods bought | *"The phone dem send na fake"* |
| seller trust | Honesty of sellers, scams, fake listings (mostly Jiji) | *"Na scammers full this app"* |
| refunds | Getting money back, reversals | *"Dem never reverse my money"* |

If none fits, choose the closest one and write a better name in Notes. The researcher will review these after the pilot.

## 5. Polarity, sarcasm and cultural references

**Polarity** is the writer's feeling about that one aspect:

- **positive**: pleased, praising, recommending (*"Transfer dey enter sharp sharp"*)
- **negative**: complaining, angry, disappointed (*"Transfer don hang since morning"*)
- **neutral**: an aspect is mentioned with no clear feeling, or a plain question or request (*"How I go take change my PIN?"*)

Judge each aspect **separately**. One review can be positive about the app and negative about charges. Ignore the star rating; judge only the words.

**Sarcastic? = yes** when the words say one thing but the writer means the opposite. *"Thank you MTN for the data wey finish in one hour"* sounds grateful but is a complaint. For sarcastic reviews, the polarity is the **intended** meaning, so this one is **negative**. Laughing emojis (😂) and words like *"well done"* or *"thank you o"* at a failure are common signals.

**Cultural reference? = yes** when someone without Nigerian knowledge would misunderstand the review. Examples: *NEPA* or *"light"* meaning electricity, *"una"* addressing the company, references to local events, places, public figures or slang such as *"japa"* or *"wahala"*. If any Nigerian adult would understand it but a foreign reader might not, choose **yes**.

## 6. Language and reviews with no opinion

**Language** describes the whole review:

- **English**: standard or Nigerian English with no Pidgin grammar (*"The app keeps crashing after the update"*)
- **Pidgin**: mainly Nigerian Pidgin (*"Dis app no dey work at all"*)
- **Code-switched**: a clear mix of English, Pidgin, Igbo, Yoruba or Hausa (*"The app is fine sha, but customer care no dey respond, biko"*). Write the languages involved in Notes, for example "English + Igbo".

A single Pidgin word in an otherwise English sentence (*"The app is good sha"*) counts as **Code-switched**.

**No opinion.** Write `no opinion` in Notes and leave the other columns empty when the review:

- only asks a question or describes an action with no judgement;
- is spam, an advert or a random message;
- is not about the app or its service at all;
- is too unclear to understand.

Still choose the **Language** for these reviews.

## 7. Worked examples

These examples were written to illustrate the rules; they are not real reviews.

| Review | Aspects (category, polarity) | Sarcastic? | Cultural ref.? | Language |
| --- | --- | --- | --- | --- |
| This app sweet well well, but the transfer no dey go at all | *app* (product overall, positive); *transfer* (transfers and payments, negative) | no | no | Pidgin |
| Thank you MTN for the data wey finish in one hour 😂 | *data* (data and airtime, negative) | yes | no | Pidgin |
| I don buy token since morning, nothing show for my meter | *token* (token and recharge, negative) | no | no | Pidgin |
| Na so una dey do every time, abeg do better | implied: power supply, negative | no | yes | Pidgin |
| Delivery was fast and the rider polite, but the shoe na fake | *Delivery* (delivery, positive); *rider* (delivery, positive); *shoe* (product quality, negative) | no | no | Code-switched |
| Well done Glo, three days no network, una try 👏 | *network* (network or coverage, negative) | yes | no | Pidgin |
| How I go take reset my PIN? | none: write `no opinion` | no | no | Pidgin |
| Dem dey remove ₦50 every time I transfer, wetin be this? | implied: fees and charges, negative | no | no | Pidgin |
| Good app, but customer care slow die | *app* (product overall, positive); *customer care* (customer service, negative) | no | no | Code-switched |
| Since this app come, NEPA wahala don reduce for my house | *app* (product overall, positive) | no | yes | Pidgin |

**Hard cases**

- *"Dem dey remove ₦50…"* has no single aspect word, so use the **implied** columns.
- In *"Delivery was fast and the rider polite"*, *Delivery* and *rider* are separate aspects in the same category; mark both.
- In the last example, *NEPA wahala* explains **why** the app is good; the writer is not judging NEPA, so NEPA is not an aspect.

## 8. Rules of conduct, privacy and checklist

**Work independently.** Do not discuss reviews with the other annotator, and do not look at their sheet. Disagreements between you are useful: they show where the rules need to be clearer.

**Do not use AI tools** (ChatGPT, Gemini or similar) to label reviews. The study needs human judgement.

**Privacy.** Reviews are public, but treat them carefully. Do not copy, share or post them anywhere. If a review contains a person's name, phone number or other personal detail, write "personal detail" in Notes; do not edit the review text.

**Breaks.** Label in sessions of 30–45 minutes. Accuracy drops when you are tired. You may skip any review you find offensive; write "skipped" in Notes.

**Questions.** Write your question in Notes and carry on. Contact the researcher, Juliet Chinenye Duru, for anything urgent.

**Quick checklist for every review**

- [ ] I read the whole review.
- [ ] Each aspect is copied with its exact words, or I used the implied columns.
- [ ] Each aspect has one category and one polarity.
- [ ] For sarcasm, I chose the **intended** polarity.
- [ ] Sarcastic?, Cultural reference? and Language are filled.
- [ ] Anything unclear is explained in Notes.
