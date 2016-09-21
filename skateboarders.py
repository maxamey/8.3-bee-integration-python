from bottle import get, post, route, run, template, request, static_file, error, \
    redirect



@route('/')
def skateboarders():
    return '''
    <!DOCTYPE html>
    <html>
      <head>
        <link rel="stylesheet" href="styles/main.css">
        <meta charset="utf-8">
        <title>summer16-1.4-css-maxAmey</title>
    </head>
    <body class="backgroundImage">
        <div class="mainDiv--centered">
          <header>
            <!-- this is where the "subscribe" and subsequent dots go-->
            <div class="subscribe">
              <a href="#subsribe.com" class="subscribe__link">subscribe</a>
              <div class="subscribe__dot--1"></div>
            </div>
            <div class="dots__stack--container">
              <div class="dots__stack"></div>
              <div class="dots__stack"></div>
              <div class="dots__stack"></div>
              <div class="dots__stack"></div>
              <div class="dots__stack"></div>
            </div>
            <!-- social media links -->

            <!-- facebook -->
            <nav class="mediaBar">
              <a class="socialMedia facebook" href="#facbook.com/sk8rsRus">
                <img src="assets/facebookIcon.png" alt="facebook icon" class="img--size facebook--icon" />
              </a>
              <!-- rss -->
              <a class="socialMedia rss" href="#rss.sk8rsRus">
                <img src="assets/rssIcon.png" alt="rss icon" class="img--size" />
              </a>
              <!-- twitter -->
              <a class="socialMedia twitter"  href="#twitter.com/sk8rsRus">
                <img src="assets/twitterIcon.png" alt="twitter icon" class="img--size" />
              </a>
              <!-- youtube -->
              <a class="socialMedia youtube" href="#youtube.com/sk8rsRus">
                  <img src="assets/youtubeIcon.png" alt="youtube icon" class="img--size" />
              </a>
            </nav>
            <!-- main navbar -->
            <nav class="menuBar">
              <a href="#page1.html" class="menuBar--button"> sk8 news </a>
              <a href="#page2.html" class="menuBar--button"> skateboarders </a>
              <a href="#page3.html" class="menuBar--button"> board design </a>
              <a href="#page4.html" class="menuBar--button"> contact us </a>
            </nav>
          </header>
          <main>
            <!-- carousel image -->
            <div class="carousel__main">
              <div class="gridFilter"></div>
              <img src="assets/peralta-logo.png" alt="logo for powell/peralta skateboards" class="logo"/>
            </div>

            <!-- carousel buttons -->
            <section class="carousel__buttons">
              <a href="carouselImage-1" class="carousel__button--link">
                <div class="carousel__buttons--circle">
                  <div class="innerDot"></div>
                </div>
              </a>
              <a href="carouselImage-2" class="carousel__button--link">
                <div class="carousel__buttons--circle"></div>
              </a>
              <a href="carouselImage-3" class="carousel__button--link">
                <div class="carousel__buttons--circle"></div>
              </a>
            </section>

            <!-- ***NEED TO ADD CSS STYLING FOR EVERYTHING PAST THIS POINT*** -->

            <!-- article grid -->
            <section class="grid__row">
              <div class="grid__column">
                <article class="article">
                  <a class="article__title--link" href="Tony_Hawk_article">
                    <h2 class="article__title">Tony Hawk Foundation Raises Big Money At Fundraiser</h2>
                  </a>
                  <time datetime="2013-10-10" class="timestamp">October 10, 2013</time>
                  <p class="article__preview">
                    Skate ipsum dolor sit amet, crail grab front foot impossible Mike Taylor helipop judo air Japan air crail slide backside. Wall ride nose grab sponsored finger flip downhill lien air lip...
                  </p>
                  <div class="readMore">
                    <a class="readMore__link" href="#articlePage-1">[ READ MORE ]</a>
                  </div>
                </article>
                <article class="article">
                  <a class="article__title--link" href="#">
                    <h2 class="article__title">Rodney Mullen: Pop an ollie and innovate! (TED Talk)</h2>
                  </a>
                  <time datetime="2013-03-10" class="timestamp">March 10, 2013</time>
                  <p class="article__preview">
                    Skate ipsum dolor sit amet, crail grab front foot impossible Mike Taylor helipop judo air Japan air crail slide backside. Wall ride nose grab sponsored finger flip downhill lien air lip...
                  <div class="readMore">
                    <a class="readMore__link" href="#articlePage-2">[ READ MORE ]</a>
                  </div>
                  </p>
                </article>
                <article class="article">
                  <a class="article__title--link" href="#">
                    <h2 class="article__title">Ray Barbee Talks 'Ban This'</h2>
                  </a>
                  <time datetime="2013-10-04" class="timestamp">October 4, 2013</time>
                  <p class="article__preview">
                    Skate ipsum dolor sit amet, crail grab front foot impossible Mike Taylor helipop judo air Japan air crail slide backside. Wall ride nose grab sponsored finger flip downhill lien air lip...
                  </p>
                  <div class="readMore">
                    <a class="readMore__link" href="#articlePage-3">[ READ MORE ]</a>
                  </div>
                </article>
              </div>
            </section>
            <!-- section for the "sk8r" bios (or bois for the Avril people)-->
            <section class="bios">
              <div class="bios__container lance">
                <a href="#bioPage-lance" class="bios__link">
                  <h3 class="bios__heading">lance mountain</h3>
                </a>
              </div>
              <div class="bios__container rodney">
                <a href="#bioPage-rodney" class="bios__link">
                  <h3 class="bios__heading">rodney mullen</h3>
                </a>
              </div>
              <div class="bios__contianer tommy">
                <a href="#bioPage-tommy" class="bios__link">
                  <h3 class="bios__heading">tommy guerrero</h3>
                </a>
              </div>
              <div class="bios__container steve">
                <a href="#bioPage-steve" class="bios__link">
                  <h3 class="bios__heading">steve<br> caballero</h3>
                </a>
              </div>
            </section>
            <section class="boards">
              <img src="assets/sk8-3.png" alt="board-1" class="boards__images leftmost" />
              <img src="assets/sk8-4.png" alt="board-2" class="boards__images" />
              <img src="assets/sk8-5.png" alt="board-3" class="boards__images" />
              <img src="assets/sk8-6.png" alt="board-4" class="boards__images" />
              <img src="assets/sk8-7.png" alt="board-5" class="boards__images" />
              <img src="assets/sk8-8.png" alt="board-6" class="boards__images" />
              <img src="assets/sk8-9.png" alt="board-7" class="boards__images" />
              <img src="assets/sk8-10.png" alt="board-8" class="boards__images" />
              <img src="assets/sk8-1.png" alt="board-9" class="boards__images" />
              <img src="assets/sk8-2.png" alt="board-10" class="boards__images rightmost" />
            </section>
        </main>
        <!-- use summer16-1.3-maxamey html index as a reference -->
        <footer class="footer__container">
          <div class="contactUs__container">
            <h2 class="contactUs__heading">contact us for more information</h2>
              Skate ipsum dolor sit amet, crail grab front foot impossible Mike Taylor helipop judo air Japan air crail slide backside. Wall ride nose grab sponsored finger flip downhill lien air lip. Nose grab fakie out tic-tac hip pop shove-it snake opposite footed Hard Corps. Salad grind heel flip rail feeble nosebone darkslide 540.
            </p>


              <!-- These are icon links for each social media site for the footer -->
            <nav class="mediaBar__footer">
              <a class="socialMedia__Footer facebookFooter" href="#facbook.com/sk8rsRus">
                <img src="assets/facebookIcon.png" alt="facebook icon" class="img--sizeFooter facebookFooter--icon" />
              </a>
              <!-- rss -->
              <a class="socialMedia__Footer rssFooter" href="#rss.sk8rsRus">
                <img src="assets/rssIcon.png" alt="rss icon" class="img--sizeFooter" />
              </a>
              <!-- twitter -->
              <a class="socialMedia__Footer twitterFooter"  href="#twitter.com/sk8rsRus">
                <img src="assets/twitterIcon.png" alt="twitter icon" class="img--sizeFooter" />
              </a>
              <!-- youtube -->
              <a class="socialMedia__Footer youtubeFooter" href="#youtube.com/sk8rsRus">
                  <img src="assets/youtubeIcon.png" alt="youtube icon" class="img--sizeFooter" />
              </a>
            </nav>
          </div>
          <form class="forms__container" action="index.html" method="post">
            <input type="text" name="Name" placeholder="Name"  class="inputs__box nameBox"><br>
            <input type="text" name="Email" placeholder="email" class="inputs__box emailBox"><br>
            <textarea name="Text" placeholder="your message" class="inputs__box textInput"></textarea><br>
            <input type="submit" name="submit" class="submit">
          </form>

        </footer>


        </div>
    </body>
    </html>
    '''

@get('/assets/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./assets')

@get('/styles/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./styles')


run(host='localhost', port=8080, debug=True)
