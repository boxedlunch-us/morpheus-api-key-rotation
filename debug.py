import yaml
from morpheuscypher import Cypher

with open("config.yaml", "r") as yaml_config:
    cfg = yaml.load(yaml_config, Loader=yaml.FullLoader)
print(cfg)
morpheus = 'https://' + cfg['appliance']['name']

c = Cypher(url=morpheus, token=cfg['api']['access']['token'])
print c.get(cfg['api']['access']['secret'])

# for section in cfg:
#     print(section)
# print(cfg["mysql"])
# print(cfg["other"])
