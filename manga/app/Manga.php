<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class Manga extends Model
{
    protected $table = "mangas";
    protected $fillable = [
        'title', 'title_en', 'about', 'cover', 'fixed', 'year','auth_ird','mag_id'
    ];
}
