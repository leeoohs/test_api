# import yaml
#
# with open("request_demo.yaml") as yaml_file:
#     data = yaml.load(yaml_file, Loader=yaml.Loader)
#     print(type(data))
#     print(data)


from string import Template


class MyTemplate(Template):
    delimiter = '$'


s = 'hello , $world'

t = Template(s)
data = t.substitute(world='python')
print(data)