import boto3
import os
import logging
from dotenv import load_dotenv
from botocore.exceptions import ClientError

load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class InstanceWrapper:
    """Encapsulates Amazon RDS DB instance actions."""

    def __init__(self, rds_client):
        """
        :param rds_client: A Boto3 Amazon RDS client.
        """
        self.rds_client = rds_client

    @classmethod
    def from_client(cls):
        """
        Instantiates this class using environment variables.
        """
        rds_client = boto3.client("rds", 
                                  aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
                                  aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
                                  region_name=os.getenv('AWS_REGION'))
        return cls(rds_client)

    def create_db_instance(
        self,
        instance_id,
        db_engine,
        instance_class,
        admin_name,
        admin_password,
    ):
        """
        Creates a DB instance.

        :param instance_id: The ID to give the newly created DB instance.
        :param db_engine: The database engine of a database to create in the DB instance.
        :param instance_class: The DB instance class for the newly created DB instance.
        :param admin_name: The name of the admin user for the created database.
        :param admin_password: The admin password for the created database.
        :return: Data about the newly created DB instance.
        """
        try:
            response = self.rds_client.create_db_instance(
                DBInstanceIdentifier=instance_id,
                Engine=db_engine,
                DBInstanceClass=instance_class,
                MasterUsername=admin_name,
                MasterUserPassword=admin_password,
                AllocatedStorage=20,  # Minimum storage for RDS
            )
            db_inst = response["DBInstance"]
        except ClientError as err:
            logger.error(
                "Couldn't create DB instance %s. Here's why: %s: %s",
                instance_id,
                err.response["Error"]["Code"],
                err.response["Error"]["Message"],
            )
            raise
        else:
            return db_inst

instance = InstanceWrapper.from_client()

instance.create_db_instance(
    instance_id='clinical',
    db_engine='postgres',
    instance_class='db.t4g.micro',
    admin_name=os.getenv('DB_ADMIN_NAME'),
    admin_password=os.getenv('DB_ADMIN_PASSWORD'),
)