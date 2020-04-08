<!DOCTYPE HTML>
<!--
	Aesthetic by gettemplates.co
	Twitter: http://twitter.com/gettemplateco
	URL: http://gettemplates.co
-->
<html>
	<head>
	<meta charset="utf-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<title>Photo &mdash; Free Website Template, Free HTML5 Template by gettemplates.co</title>
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<meta name="description" content="Free HTML5 Website Template by gettemplates.co" />
	<meta name="keywords" content="free website templates, free html5, free template, free bootstrap, free website template, html5, css3, mobile first, responsive" />
	<meta name="author" content="gettemplates.co" />

  	<!-- Facebook and Twitter integration -->
	<meta property="og:title" content=""/>
	<meta property="og:image" content=""/>
	<meta property="og:url" content=""/>
	<meta property="og:site_name" content=""/>
	<meta property="og:description" content=""/>
	<meta name="twitter:title" content="" />
	<meta name="twitter:image" content="" />
	<meta name="twitter:url" content="" />
	<meta name="twitter:card" content="" />
<style type="text/css">
	.tags a{border:1px solid #DDD;display:inline-block;color:#717171;background:#FFF;-webkit-box-shadow:0 1px 1px 0 rgba(180,180,180,0.1);box-shadow:0 1px 1px 0 rgba(180,180,180,0.1);-webkit-transition:all .1s ease-in-out;-moz-transition:all .1s ease-in-out;-o-transition:all .1s ease-in-out;-ms-transition:all .1s ease-in-out;transition:all .1s ease-in-out;border-radius:2px;margin:0 3px 6px 0;padding:5px 10px}
.tags a:hover{border-color:#08C;}
.tags a.primary{color:#FFF;background-color:#428BCA;border-color:#357EBD}
.tags a.success{color:#FFF;background-color:#5CB85C;border-color:#4CAE4C}
.tags a.info{color:#FFF;background-color:#5BC0DE;border-color:#46B8DA}
.tags a.warning{color:#FFF;background-color:#F0AD4E;border-color:#EEA236}
.tags a.danger{color:#FFF;background-color:#D9534F;border-color:#D43F3A}
</style>
	<!-- Place favicon.ico and apple-touch-icon.png in the root directory -->
	<link rel="shortcut icon" href="{{ URL::asset('favicon.ico') }}">
	<link href='https://fonts.googleapis.com/css?family=Varela+Round' rel='stylesheet' type='text/css'>
	<!-- <link href="https://fonts.googleapis.com/css?family=Bungee+Shade" rel="stylesheet"> -->
	
	
	<!-- Theme style  -->

	<!-- Magnific Popup -->

	

	<!-- Modernizr JS -->
	<script src="js/modernizr-2.6.2.min.js"></script>
	<!-- FOR IE9 below -->
	<!--[if lt IE 9]>
	<script src="js/respond.min.js"></script>
	<![endif]-->
	<link rel="stylesheet" href="{{ URL::asset('css/animate.css') }}">
	<!-- Icomoon Icon Fonts-->
	<link rel="stylesheet" href="{{ URL::asset('css/icomoon.css') }}">
	<!-- Bootstrap  -->
	<link rel="stylesheet" href="{{ URL::asset('css/bootstrap.css') }}">
	<!-- Theme style  -->
	<link rel="stylesheet" href="{{ URL::asset('css/style.css') }}">

	<!-- Magnific Popup -->
	<link rel="stylesheet" href="{{ URL::asset('css/magnific-popup.css') }}">

	<!-- Modernizr JS -->
	<script src="{{ URL::asset('js/modernizr-2.6.2.min.js') }}"></script>
	<link href="//netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css" rel="stylesheet" id="bootstrap-css">
<script src="//netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
<script src="//code.jquery.com/jquery-1.11.1.min.js"></script>

	</head>
	<body>
	

	<div id="fh5co-page">
	
	<div class="aside-toggle btn-circle">
		<a href="#"><span></span><em>About</em></a>
	</div>

	


	<div id="fh5co-aside">
		<div class="image-bg"></div>
		<div class="overlay"></div> 
		<div class="row">
			<div class="col-md-12">
				<div id="fh5co-aside-inner">
					<div class="row" id="fh5co-bio">
						
						<div class="col-md-12">
							<h2>{{ $info->title_en }}  ({{ $info->title }})</h2>
						</div>
						<div class="col-md-6">
							<p> @if ($info->stopped === 0)<a href="#">مستمر</a>
   									
							@else 
								<a href="#">متوقف</a>
							@endif
    					, {{ $info->about }}</p>
						</div>

						<div class="tags">
							 @foreach($tags as $tag)
               				 <a href="#">{{$tag->name}}</a> 
                				@endforeach
          			  </div>
						<div class="col-md-6">
							<p></p>
						</div>
						<div class="col-md-12 fh5co-social">
							<a href="#"><i class="icon-envelope"></i></a>
							<a href="#"><i class="icon-twitter"></i></a>
							<a href="#"><i class="icon-linkedin"></i></a>
							<a href="#"><i class="icon-instagram"></i></a>
							<a href="#"><i class="icon-google-plus"></i></a>
						</div>
						<div class="col-md-12" style="margin-top: 40px;">
							<p>&copy; 2018 MangaLive. All Rights Reserved. Designed by <a href="#">Authors</a> </p>
						</div>
					
					</div>
				</div>
			</div>
		</div>
	</div>
	<div class="container-fluid" id="fh5co-image-grid">
		

		<div class="grid">
		  <div class="grid-sizer"></div>
		  @foreach($chapters as $chapter)
		  <div class="grid-item item animate-box" data-animate-effect="fadeIn">
		  		<a href="{{route('chapter',['id'=>$chapter->id])}}" class="image-popup" title="Name of photo or title here">
					<div class="img-wrap">
						<img src="{{ $info->cover }}" alt="" class="img-responsive">
					</div>
					<div class="text-wrap">
						<div class="text-inner popup">
							<div>
								<h2> Number Eddition : {{ $chapter->edition_number }}</h2>
							</div>
						</div>
					</div>
				</a>
		  </div>
		  @endforeach
		 


		</div>

		
	</div>

	</div>
	
	<!-- jQuery -->
	<script src="{{ URL::asset('js/jquery.min.js') }}"></script>
	<!-- jQuery Easing -->
	<script src="{{ URL::asset('js/jquery.easing.1.3.js') }}"></script>
	<!-- Bootstrap -->
	<script src="{{ URL::asset('js/bootstrap.min.js') }}"></script>
	<!-- Waypoints -->
	<script src="{{ URL::asset('js/jquery.waypoints.min.js') }}"></script>

	<!-- Magnific -->
	<script src="{{ URL::asset('js/jquery.magnific-popup.min.js') }}"></script>
	<script src="{{ URL::asset('js/magnific-popup-options.js') }}"></script>
	<!-- Isotope & imagesLoaded -->
	<script src="{{ URL::asset('js/isotope.pkgd.min.js') }}"></script>
	<script src="{{ URL::asset('js/imagesloaded.pkgd.min.js') }}"></script>
	<!-- GSAP  -->
	<script src="{{ URL::asset('js/TweenLite.min.js') }}"></script>
	<script src="{{ URL::asset('js/CSSPlugin.min.js') }}"></script>
	<script src="{{ URL::asset('js/EasePack.min.js') }}"></script>

	<!-- MAIN JS -->
	<script src="{{ URL::asset('js/main.js') }}"></script>


	
	</body>
</html>

