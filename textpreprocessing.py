import re
import pandas as pd

stop_words = {
    'i','me','my','myself','we','our','ours','ourselves','you','your','yours','yourself',
    'yourselves','he','him','his','himself','she','her','hers','herself','it','its','itself',
    'they','them','their','theirs','themselves','what','which','who','whom','this','that',
    'these','those','am','is','are','was','were','be','been','being','have','has','had',
    'having','do','does','did','doing','a','an','the','and','but','if','or','because','as',
    'until','while','of','at','by','for','with','about','against','between','into','through',
    'during','before','after','above','below','to','from','up','down','in','out','on','off',
    'over','under','again','further','then','once','here','there','when','where','why','how',
    'all','any','both','each','few','more','most','other','some','such','no','nor','not',
    'only','own','same','so','than','too','very','s','t','can','will','just','don','should',
    'now'
}

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'[^a-z\s]', '', text)
    words = text.split()
    words = [w for w in words if w not in stop_words]
    return " ".join(words)

df = pd.read_csv('/kaggle/working/cleaned_mixeddata.csv')
df['clean_review'] = df['review'].apply(clean_text)
df.to_csv('/kaggle/working/cleaned_mixeddata.csv', index=False)
df[['review', 'clean_review']].head()
