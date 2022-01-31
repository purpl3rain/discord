from discord import Webhook, RequestsWebhookAdapter
import json


def notify_discord_channel(channel, username, content):
    disc_channel = json.load(open('Discord/webhooks.json'))
    try:
        channel_id = disc_channel[channel]['channel_id']
        token_id = disc_channel[channel]['token_id']
        webhook = Webhook.partial(channel_id, token_id, adapter=RequestsWebhookAdapter())
        webhook.send(content, username=username)
    except KeyError:
        print('No Channel named %s found - Notification was not sent' % channel)


# webhook = Webhook.partial(channel_id, token_id, adapter=RequestsWebhookAdapter())
#
# webhook.send('https://twitter.com/FearlessSec/status/1488200227634876419', username='Foo')
