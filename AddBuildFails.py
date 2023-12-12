from yandex_tracker_client import TrackerClient
client = TrackerClient(token="y0_AgAAAAA_j5z4AAr7GgAAAAD0m_F56984zz5ISTe5i8rruJYXc3SNT8k", cloud_org_id="bpf4sm1fdaovra00h3qc")
failsQueue = client.queues["BUILDFAILS"]

client.issues.create(
    queue = "BUILDFAILS", summary = "API TEST ISSUE", assignee = failsQueue.lead
)