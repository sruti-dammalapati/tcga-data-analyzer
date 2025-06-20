from aws_cdk import Stack, App
from aws_cdk import aws_dynamodb as dynamodb
from constructs import Construct
from aws_cdk import Environment

class BiospecimenStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        dynamodb.Table(
            self,
            "BiospecimenTable",
            table_name="biospecimen",
            partition_key=dynamodb.Attribute(
                name="case_id",
                type=dynamodb.AttributeType.STRING
            ),
            sort_key=dynamodb.Attribute(
                name="submitter_id",
                type=dynamodb.AttributeType.STRING
            )
        )

app = App()
env = Environment(account="417414404534", region="us-east-1")
BiospecimenStack(app, "BiospecimenStack", env=env)
app.synth()