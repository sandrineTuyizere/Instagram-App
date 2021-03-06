from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
# Create your models here.
class Image(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=30)
    image=models.ImageField(upload_to='images_galleries/')
    user=models.ForeignKey(User,on_delete=models.CASCADE, blank=True,related_name="images")
    # comments=models.TextField(blank=True)
    post = HTMLField(null=True)
    # comments=models.ForeignKey(Comment)
    likes=models.IntegerField(default=0)
   
    pub_date=models.DateTimeField(auto_now_add=True,null=True)
    @classmethod
    def get_all_images(cls):
        images=cls.objects.all().prefetch_related('comment_set')
        return images
  
    def save_image(self):
        self.save()
    def save_user(self):
        self.save()
    def delete_image_id(cls,id):
        pictures=cls.objects.get(pk=id)
        pictures.delete()
    @classmethod
    def update_image(cls,update):
        pictures=cls.objects.filter(id=id).update(id=id)
        return pictures
    @classmethod
    def get_id_image(cls,id):
        pictures=cls.objects.get(pk=id)
        return pictures  
    @classmethod
    def search_image(cls,search_iterm):
        pictures=cls.objects.filter(name__icontains=search_iterm)
        return pictures
    @classmethod
    def filter_by_name(cls,name):
        images=Image.objects.filter(name=name)
        return images
    # @classmethod
    # def update_description(cls, id):
    #     pictures = cls.objects.filter(id=id).update(id=id)
    #     return pictures

  
    
    # @classmethod
    # def get_image_by_id(cls)


class Profile(models.Model):
    class Meta:
        db_table='profile'
    profile_pic=models.ImageField(upload_to='picture/',null=True,blank=True)
    user=models.OneToOneField(User, on_delete=models.CASCADE,blank=True,related_name="profile")
    bio=models.TextField(max_length=200,null=True,default="bio")
    Followers=models.ManyToManyField(User,related_name="followers",blank=True)
    Following=models.ManyToManyField(User,related_name="following",blank=True)
    def save_prof(self):
        self.save()

    def delete_prof(self):
        self.delete()

    def follo(self,follower):
        return self.following.add(follower)

    def unfollo(self,unfollower):
        return self.following.remove(unfollower)

    def isfollowing(self,checkuser):
        return checkuser in self.following.all()
    
    def number_following(self):
        if self.fowing.count():
            returnself.following.count()
        else:
            return 0
    @classmethod
    def search(cls,username):
        profiles=cls.objects.filter(user__username__icontains=username)
        return profiles
    # @classmethod
    # def search_by_bio(cls,search_term):
    #     photo=cls.objects.filter(category__photo_category__icontains=search_term)
    #     return photo
    def __str__(self):
        return self.user.username

class Followers(models.Model):
    user=models.CharField(max_length=20,default="")
    Follower=models.CharField(max_length=20)
    profile=models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)

class Comment(models.Model):
    posted_by=models.ForeignKey(Profile, on_delete=models.CASCADE,null=True)
    comment_image=models.ForeignKey(Image,on_delete=models.CASCADE,null=True)
    comment=models.CharField(max_length=20,null=True)

    def save_com(self):
        self.save()

    def get_comment(self,id):
        comments=Comment.objects.filter(image_id=id)
        return comments
    def __str__(self):
        return self.posted_by

class NewsLetterRecients(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()