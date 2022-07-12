from django import template

register = template.Library()


@register.filter(name='stage_filter')
def stage_filter(all_clients, stage):
    return all_clients.filter(stage_status=stage)
