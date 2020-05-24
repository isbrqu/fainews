import re
import telegram
from telegram.ParseMode import MARKDOWN_V2
from decouple import config
from datetime import datetime
from utils import escape

class Faibot(object):
	"""docstring for Faibot"""
	def __init__(self):
		self.bot = telegram.Bot(token=config('TELEGRAM_BOT_TOKEN'))
		self.my_id = config('TELEGRAM_MY_CHAT')
		self.group_id = config('TELEGRAM_GROUP_CHAT')
		if config('DEBUG', default=True, cast=bool):
			self.group_id = self.my_id

	def send_nov(self, alias, title, url):
		title = escape(title)
		url = escape(url)
        msg = f'*Materia*: {alias}\n\n*Descripción*: Posteo en Novedades\n{title}\n\n_Link: {url}_'
		self.send_group()

	def send_photo(self, path):
		self.bot.send_photo(chat_id=self.group_id, photo=open(path, 'rb'))

	def check(self):
		self.send_me(datetime.now().strftime('`%a %H:%M:%S`'))

	def send_me(self, msg, markdown=True):
		if markdown:
			self.bot.send_message(chat_id=self.my_id, text=msg, parse_mode=MARKDOWN_V2)
		else:
			self.bot.send_message(chat_id=self.my_id, text=msg)

	def send_group(self, msg):
		self.bot.send_message(chat_id=self.group_id, text=msg, parse_mode=MARKDOWN_V2)

	def send_url(self, alias, url):
		if 'youtu' in url['url']:
			notice = 'entregado un video de youtube'
		elif 'assign' in url['url']:
			notice = 'asignado una entrega'
		elif 'quiz' in url['url']:
			notice = 'creado un cuestionario'
		elif 'book' in url['url']:
			notice = 'subido libro para ver/realizar'
		elif 'page' in url['url']:
			notice = 'añadido una pagina con contenido a realizar o ver'
		elif 'url' in url['url']:
			notice = 'añadido un enlace como rescurso'
		elif 'resource' in url['url']:
			notice = 'subido un archivo'
		elif 'forum' in url['url']:
			notice = 'habilitado un foro'
		elif 'folder' in url['url']:
			notice = 'añadido una carpeta'
		else:
			notice = None
		name = escape(url['name'])
		url = escape(url['url'])
		if notice:
			msg = f'*Materia*: {alias}\n\n*Descripción*: Se ha {notice}\n{name}\n\n_Link: {url}_'
			self.send_group(msg)
		else:
			msg = f'*Materia*: {alias}\n\n*Descripción*: Link no categorizado\n{name}\n\n_Link: {url}_'
			self.send_me(msg)

	def _send(self, chat_id, msg):
		self.bot.send_message(chat_id=chat_id, text=msg, parse_mode=MARKDOWN_V2)
