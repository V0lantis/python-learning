import textwrap


def q1_answer():
    answer = textwrap.dedent(
        """
        i, f, s, b = 1, 2.5, "string", True
        """
    )
    print(answer)


def q2_answer():
    answer = textwrap.dedent(
        """
        print('Hello, my name is ' 
      + name 
      + ' and I am ' + str(age) 
      + '. My banking balance is ' + str(bank_balance))
        """
    )
    print(answer)


def q3_answer():
    answer = textwrap.dedent(
        """
        print('Hello, my name is {name} and I am {age}. \
        My banking balance is {bank_balance}'
        .format(name=name, age=age, bank_balance=bank_balance))
        """
    )
    print(answer)


def q4_answer():
    answer = textwrap.dedent(
        """
        print(f'Hello, my name is {name} and I am {age}. \
        My banking balance is {bank_balance}')
        """
    )
    print(answer)


def q5_answer():
    answer = textwrap.dedent(
        """
        print(s.capitalize())
        print(s.upper())
        print(s.lower())
        print(s.swapcase())
        print(len(s))
        print(s.replace("world", "you"))
        print(s.count("l"))
        print(s.startswith("hello"))
        print(s.endswith("world"))
        print(s.split())
        print(s.find("w"))
        s = "helloworld"
        print(s.isalnum())
        print(s.isalpha())
        s = "90"
        print(s.isnumeric())
        """
    )
    print(answer)


def q6_answer():
    answer = textwrap.dedent(
        """
        answer:
        us_cities = query_job.to_dataframe()
        """
    )
    print(answer)


def q7_answer():
    answer = textwrap.dedent(
        """
        answer:
        # What five cities have the most measurements?
        us_cities.city.value_counts().head()
        """
    )
    print(answer)


def q8_answer():
    answer = textwrap.dedent(
        """
        answer:
        query = \"""
            SELECT city, country
            FROM `bigquery-public-data.openaq.global_air_quality`
            WHERE country = 'US'
            \"""
        """
    )
    print(answer)


def q9_answer():
    answer = textwrap.dedent(
        """
        answer:
        query = \"""
                SELECT score, title
                FROM `bigquery-public-data.hacker_news.full`
                WHERE type = "job" 
                \"""

        # Create a QueryJobConfig object to estimate size of query without running it
        dry_run_config = bigquery.QueryJobConfig(dry_run=True)

        # API request - dry run query to estimate costs
        dry_run_query_job = client.query(query, job_config=dry_run_config)

        print("This query will process {} bytes.".format(dry_run_query_job.total_bytes_processed))
        """
    )
    print(answer)


def q10_answer():
    answer = textwrap.dedent(
        """
        answer:
        # Only run the query if it's less than 1 MB
        ONE_MB = 1000*1000
        safe_config = bigquery.QueryJobConfig(maximum_bytes_billed=ONE_MB)

        # Set up the query (will only run if it's less than 1 MB)
        safe_query_job = client.query(query, job_config=safe_config)

        # API request - try to run the query, and return a pandas DataFrame
        safe_query_job.to_dataframe()
        """
    )
    print(answer)


def q12_answer():
    answer = textwrap.dedent(
        """
        answer:
        # Only run the query if it's less than 1 GB
        ONE_GB = 1000*1000*1000
        safe_config = bigquery.QueryJobConfig(maximum_bytes_billed=ONE_GB)

        # Set up the query (will only run if it's less than 1 GB)
        safe_query_job = client.query(query, job_config=safe_config)

        # API request - try to run the query, and return a pandas DataFrame
        job_post_scores = safe_query_job.to_dataframe()

        # Print average score for job posts
        job_post_scores.score.mean()
        """
    )
    print(answer)
