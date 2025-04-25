
MONGO_USER: str = "chaoshead"
MONGO_PASS: str = "Kaliber44"
MONGO_CLUSTER: str= "chaoscluster.31nmknk.mongodb.net"
MONGO_PARAMS: str = "retryWrites=true&w=majority&appName=ChaosCluster"

MONGO_URI: str = f"mongodb+srv://{MONGO_USER}:{MONGO_PASS}@{MONGO_CLUSTER}/?{MONGO_PARAMS}"
