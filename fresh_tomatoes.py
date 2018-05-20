#!/usr/bin/env python

import webbrowser
import os
import re
print("Content-type:text/html \n")

# styling and scripting the page
pedda_thala = '''
<!DOCTYPE html>
<html>

<head >
     <meta name="viewport" content="width=device-width,initial-scale=1.0">
     <title>Movie trailer Project</title>
     <link href="https://fonts.googleapis.com/css?family=PT+Sans|Shadows+Into+Light" 
                    rel="stylesheet">
     <link href="https://fonts.googleapis.com/css?family=Quattrocento" rel="stylesheet">
             
 <style>
   /*modal box is added*/
  .modal {
        display: none;
        position: fixed;
        z-index: 1;
        padding-top:40px;
        left: 0;
        top: 0;
        width: 100%;
        height: 100%; 
        overflow: auto; 
        background-color: rgb(0,0,0); 
        background-color: rgba(0,0,0,0.4);
   }
  /*modal content is added*/
  .modal-content {
        position:relative;    
        margin: 5% auto;
        padding: 40px;
        width: 70%;
        height:auto;
  }

  /*close button is given*/
  .close {
        position:relative;
        top:45%;
        left:-14%;
        color: #aaa;
        float: right;
        font-size: 35px;
        font-weight: bold;
        background-color: rgb(194, 81, 6);
  }
.close:hover,
.close:focus {
        background-color: rgb(28, 10, 196);
        text-decoration: none;
        cursor: pointer;
        padding-left:5px;
        padding-right:5px;
}

.container{
        display: flex;
        flex-wrap:wrap;
        font-family:arial,cursive;
}
.box{
        width:100%;
        min-height:150px;
        cursor:pointer;
}
     
@media screen and (min-width :450px)  {
    div.cap1:hover{
        border:0px 0px 0px 0px;
        background-color: #006080;
        border-radius:20px;
    }
    div.cap2:hover{
        border:1px;
        background-color:#696ac7;
        border-radius:20px;
    }
    div.cap3:hover{
        border:1px;
        background-color:#ff4d4d;
        border-radius:20px;
    }  
    div.cap4:hover{
        border:1px;
        background-color:#e69900;
        border-radius:20px;
    }  
    div.cap5:hover{
        border:1px;
        background-color:black;
        border-radius:20px;
    }       
    .cap1,.cap2,.cap3,.cap4,.cap5 {width:33%;}
    
    h1 {background-color:black;}
}

@media screen and (min-width :451px) and (max-width:850px)  {
    div.cap1:hover{
        border:0px 0px 0px 0px;
        background-color: #006080;
        border-radius:20px;
    }
    div.cap2:hover{
        border:1px;
        background-color:#696ac7;
        border-radius:20px;
    }
    div.cap3:hover{
        border:1px;
        background-color:#ff4d4d;
        border-radius:20px;
    }  
    div.cap4:hover{
        border:1px;
        background-color:#e69900;
        border-radius:20px;
    }  
    div.cap5:hover{
        border:1px;
        background-color:black;
        border-radius:20px;
    }       
    .cap1,.cap2,.cap3,.cap4,.cap5 {width:50%;}
    
    h1 {background-color:black;}
}
                                    
                                    
div.cap1:hover{
    border:0px 0px 0px 0px;
    background-color: #006080;
    border-radius:20px;
}
div.cap2:hover{
    border:1px;
    background-color:#696ac7;
    border-radius:20px;
}
div.cap3:hover{
    border:1px;
    background-color:#ff4d4d;
    border-radius:20px;
}  
div.cap4:hover{
    border:1px;
    background-color:#e69900;
    border-radius:20px;
}  
div.cap5:hover{
    border:1px;
    background-color:black;
    border-radius:20px;
}                                        

h1 {
    background-color:black;
    border-radius:25px;
    padding:5px;
}

h2 {
    margin:0px;
    font-family: 'Quattrocento', serif;
}  

.img{border-radius:10px;}
         
</style>

<div>
    <!-- The Modal -->
    <div id="myModal" class="modal">
        <!-- Modal content -->
        <div class="modal-content">
            <span class="close">&times;</span>
            <iframe id="f" width=70% height="315" src="" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen>
            </iframe>
        </div> 
    </div>
</div>
   
<script>
        var modal = document.getElementById('myModal');

        var span = document.getElementsByClassName("close")[0];

        var onc = function(c) {
                    modal.style.display = "block";
                    c='https://www.youtube.com/embed/'+c;
                    console.log(c);
                    document.getElementById("f").setAttribute("src",c);
                };

        span.onclick = function(){
            console.log("hello");
            var iframe = document.getElementById("f");
            iframe.src = iframe.src;
            modal.style.display = "none";
        } 

        window.onclick = function(event) {
            if(event.target == modal){
                modal.style.display = "none";
            } 
        }
</script> 
</head>
'''
thala = '''
<body style="text-align:center">
   <h1 style="color:white; font-family: 'PT Sans', sans-serif;
     font-family: 'Shadows Into Light', cursive;">
       MOVIE TRAILERS
   </h1>
   <div class="container">

        <div class="box cap1" onclick="onc('eEH2ba3VGjc')"> 
            <img vspace="30" src="https://bit.ly/2IuNNTb" style="width:55%"height="350" hspace="20" class="img";>
            <h2 style="color:white;">Premam</h2>
        </div>

        <div class="box cap4" onclick="onc('v2uV0_1C4UM')"> 
                <img vspace="30" src="https://bit.ly/2KHpCxn", style="width:55%"height="350"  hspace="20" class="img">
                <h2 style="color:white;">Sorcerer's Apprentice</h2>
        </div>

        <div class="box cap3" onclick="onc('1sVr-uWZPjE')"> 
                <img vspace="30" src="https://bit.ly/2rURLd" style="width:55%" height="350" hspace="20" class="img">
                <h2 style="color:white;">Vikram Vedha</h2> 
        </div>

        <div class="box cap2" onclick="onc('eBi8syxPd14')"> 
                <img vspace="30" src="https://bit.ly/2IPVsuy" style="width:55%"height="350" hspace="20" class="img">
                <h2 style="color:white;">Rab ne bana di jodi</h2>
        </div>

        <div class="box cap5" onclick="onc('NnoaCE1VPgc')"> 
                <img vspace="30" src="https://bit.ly/2KD8qcq", style="width:55%"height="350"  hspace="20" class="img">
                <h2 style="color:white;">Wrong Turn</h2>
        </div>

        <div class="box cap4" onclick="onc('MVt32qoyhi0')">
                <img vspace="30" src= "https://bit.ly/2IBomQ0" style="width:55%"height="350"  hspace="20" class="img">
                <h2 style="color:white;">Lucy</h2>
        </div> 

    </div>      
</body>

</html>
'''
# a single movie entry html template
tile_content = '''
<div class="col-md-6 col-lg-4 movie-title text-center" data-trailer-youtube-
            id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
            <img src="{poster_image_url}" width="220" height="342">
            <h2 style="color:white;">{movie_title}</h2>
</div>            
'''


def create_movie_tiles_content(movies):
    '''html content for the section of the page'''
    content = ''
    for movie in movies:
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        content += tile_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id
        )
    return content


def open_movies_page(movies):
    '''creating or overwriting the output file'''
    output_file = open('trailer2.htm', 'w')

    #reolace the movietiles placeholder generated content
    rendered_content = thala.format(
        movie_tiles=create_movie_tiles_content(movies))

    # output the file
    output_file.write(pedda_thala + rendered_content)
    output_file.close()

    #open the output file in new browser
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
    ''
