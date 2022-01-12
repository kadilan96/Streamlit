st.title("title")
my_table = st.empty()

def update_notice():
    global my_table
    global categories

    my_table.empty()

    filter = {}

    try:  # whenever I change category, it is changed too
        if categories:
            filter = {"$or": [{"category": category} for category in categories]}
    except NameError:
        pass

    sort = list({"id": -1}.items())

    # I tried same method like categories for count, but the count value never changes
    result = tuple(
        client["db"]["collection"].find(filter=filter, sort=sort, limit=count)
    )

    # print(result)

    data = {
        "title": tuple(article["title"] for article in result),
    }

    df = pd.DataFrame(data)
    df.index = [f"{i}th" for i in range(1, len(result) + 1)]
    my_table.table(df)

categories = st.multiselect(
    "label",
    categories,  # like ["a", "b"...]
    [],
    on_change=update_notice(),  # I should pass the function not return value, but the table disappears when I use  lambda: f() or f...
    help="help",
)

count = st.slider(
    "label",
    min_value=1,
    max_value=100,
    value=10,
    on_change=update_notice(),  # I should pass the function not return value, but the table disappears...
    help="help",
)