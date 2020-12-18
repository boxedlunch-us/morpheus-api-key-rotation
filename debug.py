import yaml

with open("config.yaml", "r") as yaml_config:
    cfg = yaml.load(yaml_config)
print("")
# for section in cfg:
#     print(section)
# print(cfg["mysql"])
# print(cfg["other"])
