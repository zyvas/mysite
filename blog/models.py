#coding:utf-8
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length = 200)
    email = models.EmailField()
   
    def __unicode__(self):
        return u'%s'%(self.name)

class Tag(models.Model):
    content = models.CharField(max_length=20, blank=True)
    create_time = models.DateTimeField(auto_now_add = True)
        
    def __unicode__(self):
        return u'%s'%(self.content)

class Blog(models.Model):
    title = models.CharField(max_length=100)  #标题
    author = models.ForeignKey(Author)   #作者
    update_time = models.DateTimeField(auto_now=True)   #修改时间
    publish_time = models.DateTimeField(auto_now_add=True)  #发布时间
    content = models.TextField()   #内容
    tags = models.ManyToManyField(Tag, blank=True) #标签


    def __unicode__(self):
        return u'%s  %s  %s'%(self.title,self.author,self.publish_time)

    class Meta:
        ordering = ['-publish_time']




