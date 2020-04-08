<?php

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/

Route::get('/', function () {
	
    return view('index');
})->name('index');

Route::get('/all',['as'=>'allManga','uses'=>'HomeController@allManga']);
Route::get('/latest',['as'=>'getHome','uses'=>'HomeController@latest']);
//Route::get('/latest',['as'=>'latest','uses'=>'HomeController@latest']);
Route::get('/fixed',['as'=>'fixed','uses'=>'HomeController@fixed']);
Route::get('manga/{id}',['as'=>'manga','uses'=>'HomeController@manga']);
Route::get('chapter/{id}',['as'=>'chapter','uses'=>'HomeController@chapter']);
//Route::post('etudiant/update/{id}',['as'=>'postUpdate','uses'=>'PagesController@postUpdate'])->where('id','[0-9]+');


Route::get('/allJson',['as'=>'allManga','uses'=>'HomeController@allMangaJson']);
