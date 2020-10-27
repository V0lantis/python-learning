import textwrap
from google.cloud import bigquery

_client = bigquery.Client()
_dataset_ref = _client.dataset("hacker_news", project="bigquery-public-data")
_dataset = _client.get_dataset(_dataset_ref)
_tables = list(_client.list_tables(_dataset))


def q1_answer():
    answer = textwrap.dedent(
        """
        answer:
        from google.cloud import bigquery
        client = bigquery.Client()
        """
    )
    print(answer)


def q2_check(dataset_ref, dataset):
    assert (
        dataset_ref == _dataset_ref
    ), f"dataset_ref should be equal to : {_dataset_ref}. Value = {dataset_ref}"
    assert (
        dataset.dataset_id == _dataset.dataset_id
    ), f"dataset should be equal to : {_dataset.dataset_id}. Value = {dataset.dataset_id}"
    print("correct")


def q2_hint():
    answer = textwrap.dedent(
        """
        hint:
        methods are dataset() and get_dataset()
        """
    )
    print(answer)


def q2_answer():
    answer = textwrap.dedent(
        """
        answer:
        dataset_ref = client.dataset("hacker_news", project="bigquery-public-data")
        dataset = client.get_dataset(dataset_ref)
        """
    )
    print(answer)


def q3_hint():
    answer = textwrap.dedent(
        """
        hint: 
        method is list_tables
        property is table_id
        """
    )
    print(answer)


def q3_answer():
    answer = textwrap.dedent(
        """
        answer:
        tables = client.list_tables(dataset)
        for table in tables:
            print(table.table_id)
        """
    )
    print(answer)


def q4_hint():
    answer = textwrap.dedent(
        """
        hint: 
        methods are table and get_table. Careful on which object you call them
        """
    )
    print(answer)


def q4_answer():
    answer = textwrap.dedent(
        """
        answer:
        table_ref = dataset_ref.table("full")
        table = client.get_table(table_ref)
        """
    )
    print(answer)


def q5_answer():
    answer = textwrap.dedent(
        """
        answer:
        client.list_rows(table, max_results=5).to_dataframe()
        """
    )
    print(answer)


def q6_answer():
    answer = textwrap.dedent(
        """
        answer:
        client.list_rows(table, selected_fields=table.schema[:1], max_results=5).to_dataframe()
        """
    )
    print(answer)
