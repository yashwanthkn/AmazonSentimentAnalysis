import streamlit as st
# NLP Pkgs
from textblob import TextBlob
import pandas as pd 
from sklearn.ensemble import AdaBoostClassifier,RandomForestClassifier
import altair as alt
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
# Emoji
import emoji

# Fxn
def convert_to_df(sentiment):
	sentiment_dict = {'polarity':sentiment.polarity,'subjectivity':sentiment.subjectivity}
	sentiment_df = pd.DataFrame(sentiment_dict.items(),columns=['metric','value'])
	return sentiment_df

def analyze_token_sentiment(docx):
	analyzer = SentimentIntensityAnalyzer()
	pos_list = []
	neg_list = []
	neu_list = []
	for i in docx.split():
		res = analyzer.polarity_scores(i)['compound']
		if res > 0.1:
			pos_list.append(i)
			pos_list.append(res)

		elif res <= -0.1:
			neg_list.append(i)
			neg_list.append(res)
		else:
			neu_list.append(i)

	result = {'positives':pos_list,'negatives':neg_list,'neutral':neu_list}
	return result 



def main():
	"""Sentiment Analysis Emoji App """

	st.title("Sentiment Analysis")

	activities = ["Sentiment","About"]
	choice = st.sidebar.selectbox("Choice",activities)

	if choice == 'Sentiment':
		st.subheader("Group-3")
		#st.write(emoji.emojize('Everyone :red_heart: Streamlit ',use_aliases=True))
		from_sent = st.text_area("Enter Your Text","Type Here")
		if st.button("Analyze"):
			br=TextBlob(from_sent)
			result = br.sentiment.polarity
			if result==0:
				custom_emoji = ':smile:'
				st.success("This is a Neutral Massage")
			elif result>0:
				custom_emoji = ':disappointed:'
				st.success("This is a Positive message")
			else:
				st.success("This is a Negative message")


			sentiment = TextBlob(from_sent).sentiment
			#st.write(sentiment)


			# Emoji
			if sentiment.polarity > 0:
				st.markdown("Sentiment:: Positive :smiley: ")
			elif sentiment.polarity < 0:
				st.markdown("Sentiment:: Negative :angry: ")
			else:
				st.markdown("Sentiment:: Neutral 😐 ")

			# Dataframe
			result_df = convert_to_df(sentiment)
			st.dataframe(result_df)

			# Visualization
			c = alt.Chart(result_df).mark_bar().encode(
			x='metric',
			y='value',
			color='metric')
			st.altair_chart(c,use_container_width=True)


			st.info("Token Sentiment")

			token_sentiments = analyze_token_sentiment(from_sent)
			st.write(token_sentiments)

			


	if choice == 'About':
		st.subheader("About:Team Members")
		#st.info("Built with Streamlit,Textblob and Emoji")
		st.text("Arti Sadanande")
		st.text("Balasubramanian.P")
		st.text("Manjunath Pujer")
		st.text("Poornima C L")
		st.text("Smitha Mandlur S")
		st.text("Swasthik S")
		st.text("Yashawanth K N")







if __name__ == '__main__':
	main()