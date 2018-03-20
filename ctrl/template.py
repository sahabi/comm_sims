class {{ctrl_name}}:

    def __init__(self):
        self.state = 0

    def comms(self, tp):
        {% for ifstat in commsifs %}
        if self.state == {{ifstat.state}} and tp == {{ifstat.tp}}:
            return {{ifstat.c}}
        {% endfor %}

    def move(self, i, c):
        {% for ifstat in moveifs %}
        if self.state == {{ifstat.state}} and i == {{ifstat.i}} and c == {{ifstat.c}}:
            self.state = {{ifstat.ns}}
            return {{ifstat.o}}
        {% endfor %}
