# coding:utf-8

from django.db import models

# Create your models here.
class Ghost(models.Model):
    name = models.CharField(max_length=50, verbose_name="式神名称")
    chapter_name = models.CharField(max_length=50, verbose_name="出现章节")


    def __str__(self):
        return self.name

class Chapter(models.Model):
    chapter_name = models.CharField(max_length=50, verbose_name="章节名称")   # 章节名
    ghost_name = models.CharField(max_length=50, verbose_name="显示式神/层数")     # 显示怪物名
    fight_ghost = models.CharField(max_length=100, verbose_name="战斗式神")    # 战斗中怪物

    def __str__(self):
        return self.chapter_name