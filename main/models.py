
from django.db import models


class notes(models.Model):
	title = models.CharField(max_length = 100)
	image = models.FileField('Фото',upload_to='photos/', blank=True)
	like = models.IntegerField(blank=True, default=0)
	dislike = models.IntegerField(blank=True, default=0)
	
	def __str__(self):
		return self.title

	class Meta:
		verbose_name = "Заметка"
		verbose_name_plural = "Заметки"

class comment(models.Model):
	note = models.ForeignKey(notes, default=None, on_delete=models.CASCADE, verbose_name='Название товара')
	single_comment = models.CharField(max_length = 500)



	class Meta:
		verbose_name = 'Комментарий'
		verbose_name_plural = 'Комментарии'