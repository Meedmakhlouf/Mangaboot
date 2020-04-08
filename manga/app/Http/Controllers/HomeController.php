<?php

namespace App\Http\Controllers;
use App\Chapter;
use App\Manga;
use App\Page;
use Illuminate\Support\Facades\DB;
use Illuminate\Http\Request;

class HomeController extends Controller
{
    public function latest(){
        $mangas = DB::table('mangas as m')
                    ->join('chapters as c','m.id','=','c.manga_id')
            ->select('m.cover','m.title','c.id as chapter_id','m.about','m.id','c.views','c.edition_number')
            ->where('m.stopped','=',0)->where('m.updatable','=',0)
            ->groupBy('m.id')
            ->orderBy('c.edition_number','DESC')
            ->take(5)
            ->get();


        return response($mangas,200,['Content-Type'=>'application/json']);
    }


public function allManga(){
        $mangas = Manga::all();

        //return response($mangas,200,['Content-Type'=>'application/json']);
        return view('index',compact('mangas'));
        
    }


    public function fixed(){
        $mangas = DB::table('mangas as m')
            ->join('chapters as c','m.id','=','c.manga_id')
            ->select('m.cover','c.id','m.stopped','c.edition_number')
            ->selectRaw('CONCAT(m.title," - الفصل ", c.edition_number) as title , CASE WHEN m.stopped = 0 THEN "مستمر" ELSE "متوقف" END as etat')
            ->where('m.fixed','=',1)->where('m.updatable','=',0)
            ->groupBy('m.id')
            ->orderBy('c.edition_number',"desc")
            ->get();

        return response($mangas,200,['Content-Type'=>'application/json']);
    }

    public function manga($id){
        $info = Manga::where('id','=',$id)
            ->selectRaw('title,title_en,cover,stopped,about,CASE WHEN stopped = 0 THEN "مستمر" ELSE "متوقف" END as etat')
            ->first();
        $chapters = Chapter::select('edition_number','id')->where('manga_id','=',$id)->orderBy('edition_number','DESC')->get();

        $tags = DB::select("SELECT t.name FROM tags t,mangas m,tag_manga tm WHERE  m.id=tm.manga_id and t.id=tm.tag_id and m.id=?",[$id]);
        $auteur = DB::select("SELECT t.name FROM tags t,mangas m,tag_manga tm WHERE  m.id=tm.manga_id and t.id=tm.tag_id and m.id=?",[$id]);
        //return response($chapters,200,['Content-Type'=>'application/json']);
        //$mangas = Manga::all();
        return view('chapter',compact('info','chapters','tags'));

        return response()->json(['infos'=>$info,'chapters'=>$chapters]);
    }
    public function chapter($id){
        $info = Chapter::where('id','=',$id)->first();
        $images = Page::where('chapter_id','=',$id)->get();
        return response()->json(['infos'=>$info,'images'=>$images]);
    }



                    // JSON RESPENSE****************

public function allMangaJson(){
        $mangas = Manga::all();

        return response($mangas,200,['Content-Type'=>'application/json']);

        
    }


    public function mangaJson($id){
        $info = Manga::where('id','=',$id)
            ->selectRaw('title,title_en,cover,stopped,about,CASE WHEN stopped = 0 THEN "مستمر" ELSE "متوقف" END as etat')
            ->first();
        $chapters = Chapter::select('edition_number','id')->where('manga_id','=',$id)->orderBy('edition_number','DESC')->get();

        $tags = DB::select("SELECT t.name FROM tags t,mangas m,tag_manga tm WHERE  m.id=tm.manga_id and t.id=tm.tag_id and m.id=?",[$id]);
        $auteur = DB::select("SELECT t.name FROM tags t,mangas m,tag_manga tm WHERE  m.id=tm.manga_id and t.id=tm.tag_id and m.id=?",[$id]);
        return response($chapters,200,['Content-Type'=>'application/json']);
        //$mangas = Manga::all();
        return view('chapter',compact('info','chapters','tags'));

        return response()->json(['infos'=>$info,'chapters'=>$chapters]);
    }
    public function chapterJson($id){
        $info = Chapter::where('id','=',$id)->first();
        $images = Page::where('chapter_id','=',$id)->get();
        return response()->json(['infos'=>$info,'images'=>$images]);
    }


}
