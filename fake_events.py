import boto3
import json
from fake_web_events import Simulation


client = boto3.client('firehose')


def put_record(event: dict):
    data = json.dumps(event) + "\n"
    response = client.put_record(
        DeliveryStreamName='fake-events-streaming', 
        Record={"Data":data}
    )
    print(event)
    return response

simulation = Simulation(user_pool_size=100, sessions_per_day=100000)
events = simulation.run(duration_seconds=300)

for event in events:
    put_record(event)

# events/landing-date=!{timestamp:yyyy}-!{timestamp:MM}-!{timestamp:dd}/
# python3 fake_events.py