## How to generate the datasets

### 1. Get ids for each category 
```
python3 get_ids_from_twitter_pro_pt.py
```
```
python3 get_ids_from_twitter_pro_en.py
```
```
python3 get_ids_from_twitter_anti_pt.py
```
```
python3 get_ids_from_twitter_anti_en.py
```

### 2. Hydrate tweet ids
Twarc's hydrate command will read a file of tweet identifiers and write out the tweet JSON for them using Twitter's status/lookup API.

```
twarc hydrate ids_pro_pt.csv > tweets_pro_pt.jsonl
```
```
twarc hydrate ids_pro_en.csv > tweets_pro_en.jsonl
```
```
twarc hydrate ids_anti_pt.csv > tweets_anti_pt.jsonl
```
```
twarc hydrate ids_anti_en.csv > tweets_anti_en.jsonl
```

### 3. Label the data (pro-vaccine/anti-vaccine), predict demographics (age, gender, race) and normalize users' locations
```
python3 training_test_pro_pt.py
```
```
python3 training_test_pro_en.py
```
```
python3 training_test_anti_pt.py
```
```
python3 training_test_anti_en.py
```
