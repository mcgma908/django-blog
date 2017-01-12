from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from blog.models import Post, Extra
from math import ceil
from blog.other_functions import deslugify
from .forms import CommentForm

def blog_home(request, page): #Grab the blogs we want just for the first page
   
   blogs_per_page = 2 #This needs to be changed in "blog_more" as well
   
   #Works out how many blogs to put on each page, and some info needed for 
   #displaying them including whether its the "first" or "last" page
   total_blogs = len(Post.objects.filter(publish=True))
   pages = ceil(total_blogs/blogs_per_page)
   if int(page) == 1:
      first = True
   else:
      first = False
   if int(page)*blogs_per_page >= total_blogs:
      last = True
   else:
      last = False      
   
   #Grabs the blogs for the page (if they exist...)
   start_blog = int(page)*blogs_per_page-blogs_per_page
   end_blog = int(page)*blogs_per_page
   blog_posts = Post.objects.filter(publish=True).order_by("-date")[start_blog:end_blog] #[:blogs_per_page]
   if not blog_posts:
      raise Http404("Sorry, we could not find that page")
   
   #Dictionary to pass to html template
   context = {"blogs": blog_posts, "blogs_per_page": blogs_per_page, 
              "total_blogs": total_blogs, "first": first, 
              "last": last, "pages": pages, "page": page} 
   return render(request, 'blog/home.html', context)


def blog_single(request, year, page_slug):
   #Grab the blog we want 
   post = Post.objects.get(slug=page_slug)
   if post.publish==False:
      raise Http404("Sorry, we could not find that page")
   elif year != str(Post.get_year(post)):
      raise Http404("Sorry, we could not find that page")
   else:
      if request.method == "POST":
         form = CommentForm(request.POST)
         if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('blog_single', year = year, page_slug=page_slug)
      else:
         form = CommentForm()
      context = {'post': post, 'form': form}   
      return render(request, 'blog/blog1.html', context)

def about(request):
   context = Extra.objects.get(slug="about-me")
   return render(request, 'blog/basic.html', {"context": context})

def archive(request):
   all_tags = Post.tag.all()
   #Figure out what years to print
   all_blogs = Post.objects.all()
   all_years = []
   for x in all_blogs:
      year = Post.get_year(x)
      if year not in all_years:
         all_years.append(year)
   sorted(all_years)
         
   return render(request, 'blog/archive.html', {"all_tags": all_tags, 
                                                "all_years": all_years})
def year_archive(request, year):
   #for all blog posts of one year eg "2017"
   all_blogs = Post.objects.filter(publish=True)
   blog_posts = []   
   for x in all_blogs:
      if year == str(Post.get_year(x)):
         blog_posts.append(x)
   context = {"blogs": blog_posts, "tag_name": year}
   return render(request, 'blog/single_archive.html', context)

def single_archive(request, tag_slug):
   #for all blog posts of one tag eg "psuedocontext"
   deslug=deslugify(tag_slug)
   blog_posts = Post.objects.filter(tag__name__in=[deslug], publish=True).order_by("-date")
   context = {"blogs": blog_posts, "tag_name": deslug}
   return render(request, 'blog/single_archive.html', context)

def further(request):
   context = Extra.objects.get(slug="further-reading")
   return render(request, 'blog/basic.html', {"context": context})

