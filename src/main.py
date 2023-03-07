from generate import GPT3
from medium import Article

if __name__ == "__main__":
    gen = GPT3()
    post = Article()

    article_name = str(input("Enter topic of article: "))

    text = gen.gen_article(f"{article_name}")
    # print(text)

    keywords = gen.extract_keywords(text)
    try:
        tags_list = keywords.split(",")
    except BaseException:  # TODO: Better exception handling
        print("Bad keywords")
        tags_list = []

    response = post.publish(
        article_name=article_name,
        article_tags=tags_list,
        article_content=text,
    )
    print(response)
    ...

