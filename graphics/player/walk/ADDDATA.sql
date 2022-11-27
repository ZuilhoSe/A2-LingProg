INSERT INTO Company (CompanyID, CompanyName, CompanyJapName, CompanyStablishment, CompanyTwitter, CompanyFacebook, CompanyInstagram, CompanyWebsite) VALUES (16, 'TV Tokyo', 'テレビ東京', '1964-04-12', 'https://twitter.com/tvtokyo_pr', 'https://www.facebook.com/tvtokyo.pr/', '', 'tv-tokyo.co.jp');
INSERT INTO Company (CompanyID, CompanyName, CompanyJapName, CompanyStablishment, CompanyTwitter, CompanyFacebook, CompanyInstagram, CompanyWebsite) VALUES (159, 'Kodansha', '講談社', '1909-05-01', 'https://twitter.com/KODANSHA_JP', 'https://facebook.com/kodansha.co.jp/', 'https://www.instagram.com/kodansha.co.jp/', 'kodansha.com');
INSERT INTO Company (CompanyID, CompanyName, CompanyJapName, CompanyStablishment, CompanyTwitter, CompanyFacebook, CompanyInstagram, CompanyWebsite) VALUES (102, 'Funimation', 'ファニメーション', '1994-5-9', '@funimation', 'https://facebook.com/funimation', 'https://www.instagram.com/funimation/', 'funimation.com');
INSERT INTO Company (CompanyID, CompanyName, CompanyJapName, CompanyStablishment, CompanyTwitter, CompanyFacebook, CompanyInstagram, CompanyWebsite) VALUES (43, 'ufotable', 'ユーフォーテーブル', '2000-10-2', 'https://twitter.com/ufotable', '', 'https://www.instagram.com/ufotable_inc/', 'http://www.ufotable.com/index.html');
INSERT INTO Company (CompanyID, CompanyName, CompanyJapName, CompanyStablishment, CompanyTwitter, CompanyFacebook, CompanyInstagram, CompanyWebsite) VALUES (17, 'Aniplex', 'アニプレックス', '1995-9-1', 'https://twitter.com/aniplex_aj', 'https://www.facebook.com/aniplex.co.jp', '', 'http://www.aniplex.co.jp/');
INSERT INTO Company (CompanyID, CompanyName, CompanyJapName, CompanyStablishment, CompanyTwitter, CompanyFacebook, CompanyInstagram, CompanyWebsite) VALUES (1365, 'Shueisha', '集英社', '1926-08-19', 'https://twitter.com/shueisha_pr', 'https://facebook.com/shueisha.manga.net/', 'https://www.instagram.com/shueisha.manga.net/', 'shueisha.co.jp');

INSERT INTO Manga (MangaID, MangaName, MangaJapName, MangaVolumes, MangaChapters, MangaStatus, MangaPublished, MangaDemographic, MangaSynopsis) VALUES (598, 'Fairy Tail', 'FAIRY TAIL', 63, 549, 'Finished', 'Aug 2, 2006 to Jul 26, 2017', 'Shounen', 'Magos malucos aprontando grandes confusões num mundo fantástico.');
INSERT INTO Manga (MangaID, MangaName, MangaJapName, MangaVolumes, MangaChapters, MangaStatus, MangaPublished, MangaDemographic, MangaSynopsis) VALUES (96792, 'Kimetsu no Yaiba', '鬼滅の刃', 23, 207, 'Finished', 'Feb 15, 2016 to May 18, 2020', 'Shounen', 'Cacadores de demônios tentando curar uma pessoa que virou demônio.');
INSERT INTO Manga (MangaID, MangaName, MangaJapName, MangaVolumes, MangaChapters, MangaStatus, MangaPublished, MangaDemographic, MangaSynopsis) VALUES (31240, 'Shokugeki no Souma', '食戟のソーマ', 36, 325, 'Finished', 'Nov 26, 2012 to Aug 29, 2019', 'Shounen', 'Manga de batalha de culinária.');

INSERT INTO DateAired (AnimeAired, AnimePremiered) VALUES ('Oct 12, 2009 to Mar 30, 2013', 'Fall 2009');
INSERT INTO DateAired (AnimeAired, AnimePremiered) VALUES ('Apr 6, 2019 to Sep 28, 2019', 'Spring 2019');
INSERT INTO DateAired (AnimeAired, AnimePremiered) VALUES ('Apr 4, 2016 to Sep 19, 2016', 'Spring 2016');

INSERT INTO Anime (AnimeID, AnimeName, AnimeJapName, AnimeEngName, AnimeType, AnimeEpisodes, AnimeStatus, AnimeSource, AnimeDuration, AnimeRating,  AnimeSynopsis, MangaID, AnimeAired) VALUES (6702, 'Fairy Tail', 'FAIRY TAIL（フェアリーテイル）', 'Fairy Tail', 'TV', 175, 'Finished Airing', 'Manga', '24 min. per ep.', 'PG-13 - Teens 13 or older',  'Magos malucos aprontando grandes confusões num mundo fantástico.', 598, 'Oct 12, 2009 to Mar 30, 2013');
INSERT INTO Anime (AnimeID, AnimeName, AnimeJapName, AnimeEngName, AnimeType, AnimeEpisodes, AnimeStatus, AnimeSource, AnimeDuration, AnimeRating, AnimeSynopsis, MangaID, AnimeAired) VALUES (38000, 'Kimetsu no Yaiba', '鬼滅の刃', 'Demon Slayer: Kimetsu no Yaiba', 'TV', 26, 'Finished Airing', 'Manga', '23 min. per ep.', 'R - 17+ (violence & profanity)',  'Cacadores de demônios tentando curar uma pessoa que virou demônio.', 96792, 'Apr 6, 2019 to Sep 28, 2019');
INSERT INTO Anime (AnimeID, AnimeName, AnimeJapName, AnimeEngName, AnimeType, AnimeEpisodes, AnimeStatus, AnimeSource, AnimeDuration, AnimeRating,  AnimeSynopsis, MangaID, AnimeAired) VALUES (31240, 'Re:Zero kara Hajimeru Isekai Seikatsu', 'Re：ゼロから始める異世界生活', 'Re:ZERO -Starting Life in Another World-', 'TV', 25, 'Finished Airing', 'Light novel', '25 min. per ep.', 'R - 17+ (violence & profanity)',  'Garoto nerd morre e reencarna em mundo de fantasia.', NULL, 'Apr 4, 2016 to Sep 19, 2016');

INSERT INTO Animates (AnimeID, CompanyID) VALUES (6702, 102);
INSERT INTO Animates (AnimeID, CompanyID) VALUES (38000, 43);
INSERT INTO Animates (AnimeID, CompanyID) VALUES (31240, 102);

INSERT INTO club (ClubID,ClubName, ClubDescription, ClubCategory) VALUES (20081,'Recommendation Club', 'A place where you can chat, ask for anime & manga recommendations, vote in polls, play games, and much more', 'Anime');
INSERT INTO club (ClubID,ClubName, ClubDescription, ClubCategory) VALUES (256,'Brasil', 'Bem-vindos ao Brasil \ Brazil. Ponto de encontro para todos os brasileiros do MAL.', 'Cities & Neighborhoods');
INSERT INTO club (ClubID,ClubName, ClubDescription, ClubCategory) VALUES (32683,'Slice of Life Club', 'A club for fans of the wonderful slice of life genre. Join our active Discord community!', 'Anime');


INSERT INTO AnimeTopic (AnimeID, ClubID) VALUES (6702, 20081);
INSERT INTO AnimeTopic (AnimeID, ClubID) VALUES (38000, 256);
INSERT INTO AnimeTopic (AnimeID, ClubID) VALUES (31240, 32683);


INSERT INTO "Character" (CharName, CharID) VALUES ('Emilia Satella, Lia', 118737);
INSERT INTO "Character" (CharName, CharID) VALUES ('Zenitsu Agatsuma', 146158);
INSERT INTO "Character" (CharName, CharID) VALUES ('Happy', 5188);

INSERT INTO AppearsManga (CharID, MangaID) VALUES (146158, 96792);
INSERT INTO AppearsManga (CharID, MangaID) VALUES (5188, 598);

SET ANSI_WARNINGS OFF
INSERT INTO Author (AuthorID, AuthorName, AuthorFamilyName, AuthorAlternativeName, AuthorBirthday, AuthorWebsite, AuthorTwitter, AuthorInstagram, AuthorFacebook, AuthorReddit) VALUES (40398, 'Gotouge, Koyoharu', '呼世晴', 'Gotouge', '1988-05-05', '', 'http://twitter.com/share?related=MyAnimeList.net&via=myanimelist&url=https%3A%2F%2Fmyanimelist.net%2Fpeople%2F40398%2FGotouge_Koyoharu&text=Koyoharu%20Gotouge&hashtags=', '', 'http://www.facebook.com/share.php?u=https%3A%2F%2Fmyanimelist.net%2Fpeople%2F40398%2FGotouge_Koyoharu', 'http://reddit.com/submit?url=https%3A%2F%2Fmyanimelist.net%2Fpeople%2F40398%2FGotouge_Koyoharu&title=Koyoharu%20Gotouge');
INSERT INTO Author (AuthorID, AuthorName, AuthorFamilyName, AuthorAlternativeName, AuthorBirthday, AuthorWebsite, AuthorTwitter, AuthorInstagram, AuthorFacebook, AuthorReddit) VALUES (1882, 'Mashima, Hiro', '真島', 'H. Mashima', '1977-05-03', '', 'http://twitter.com/share?related=MyAnimeList.net&via=myanimelist&url=https%3A%2F%2Fmyanimelist.net%2Fpeople%2F1882%2FMashima_Hiro&text=Hiro%20Mashima&hashtags=', '', 'http://www.facebook.com/share.php?u=https%3A%2F%2Fmyanimelist.net%2Fpeople%2F1882%2FMashima_Hiro', 'http://reddit.com/submit?url=https%3A%2F%2Fmyanimelist.net%2Fpeople%2F1882%2FMashima_Hiro&title=Hiro%20Mashima');
INSERT INTO Author (AuthorID, AuthorName, AuthorFamilyName, AuthorAlternativeName, AuthorBirthday, AuthorWebsite, AuthorTwitter, AuthorInstagram, AuthorFacebook, AuthorReddit) VALUES (19791, 'Tsukuda, Yuuto', '祐斗', 'T. Hito', '1986-03-13', '', 'http://twitter.com/share?related=MyAnimeList.net&via=myanimelist&url=https%3A%2F%2Fmyanimelist.net%2Fpeople%2F19791%2FTsukuda_Yuuto&text=Yuuto%20Tsukuda&hashtags=', '', 'http://www.facebook.com/share.php?u=https%3A%2F%2Fmyanimelist.net%2Fpeople%2F19791%2FTsukuda_Yuuto', 'http://reddit.com/submit?url=https%3A%2F%2Fmyanimelist.net%2Fpeople%2F19791%2FTsukuda_Yuuto&title=Yuuto%20Tsukuda');
SET ANSI_WARNINGS ON

INSERT INTO "User" (UserID, UserName, UserGender, UserBirthday, UserLocation, UserJoinDate, UserLastOnline) VALUES (77777, 'ZuilhoDragneel', 'Male', '2001-11-11', 'Brazil', '2018-01-16', '2021-08-09 13:57:40');
INSERT INTO "User" (UserID, UserName, UserGender, UserBirthday, UserLocation, UserJoinDate, UserLastOnline) VALUES (666, 'GeorgeFullbuster', 'Male', '2003-05-17', 'Brazil', '2022-09-20', '2022-09-20 13:25:05');
INSERT INTO "User" (UserID, UserName, UserGender, UserBirthday, UserLocation, UserJoinDate, UserLastOnline) VALUES (747, 'BrunoTogata', 'Male', '2001-12-08', 'Brazil', '2022-09-20', '2022-09-22 15:43:20');

INSERT INTO Blog (BlogID, BlogTitle, BlogContent, BlogPostDate, UserID) VALUES (887427, 'Favorite Anime', 'favorite.html', '2022-09-02', 77777);
INSERT INTO Blog (BlogID, BlogTitle, BlogContent, BlogPostDate, UserID) VALUES (887403, 'How to choose an online casino', 'casino.html', '2022-8-28', 666);
INSERT INTO Blog (BlogID, BlogTitle, BlogContent, BlogPostDate, UserID) VALUES (887402, 'Best Waifu', 'best_waifu.html', '2021-11-05', 747);


INSERT INTO clubimage (ClubImgID, ClubImgArchive, ClubID) VALUES (258540, 'KawaiiIMG.png', 20081);
INSERT INTO clubimage (ClubImgID, ClubImgArchive, ClubID) VALUES (8765432, 'MainIconClub.png', 256);
INSERT INTO clubimage (ClubImgID, ClubImgArchive, ClubID) VALUES (1792322, 'HeaderSlice.png', 32683);


INSERT INTO CharPicture (CharImgID, CharImgArchive, CharID) VALUES (123, 'emilia.png', 118737);
INSERT INTO CharPicture (CharImgID, CharImgArchive, CharID) VALUES (654, 'zenitsu.png', 146158);
INSERT INTO CharPicture (CharImgID, CharImgArchive, CharID) VALUES (898, 'happy.png', 5188);


INSERT INTO CharTopic (CharID, ClubID) VALUES (118737, 20081);
INSERT INTO CharTopic (CharID, ClubID) VALUES (146158, 256);
INSERT INTO CharTopic (CharID, ClubID) VALUES (5188, 32683);

INSERT INTO Genre (GenreName, GenreDescription) VALUES ('Action', 'Muita ação!');
INSERT INTO Genre (GenreName, GenreDescription) VALUES ('Adventure', 'Animes com muita aventura!');
INSERT INTO Genre (GenreName, GenreDescription) VALUES ('Fantasy', 'Realidades fantasticas!');
INSERT INTO Genre (GenreName, GenreDescription) VALUES ('Drama', 'Animes para refletir e chorar.');
INSERT INTO Genre (GenreName, GenreDescription) VALUES ('Suspense', 'O que será que acontece no final?');

INSERT INTO ClassifiesAnime (AnimeID, GenreName) VALUES (6702, 'Action');
INSERT INTO ClassifiesAnime (AnimeID, GenreName) VALUES (6702, 'Adventure');
INSERT INTO ClassifiesAnime (AnimeID, GenreName) VALUES (6702, 'Fantasy');
INSERT INTO ClassifiesAnime (AnimeID, GenreName) VALUES (38000, 'Action');
INSERT INTO ClassifiesAnime (AnimeID, GenreName) VALUES (38000, 'Fantasy');
INSERT INTO ClassifiesAnime (AnimeID, GenreName) VALUES (31240, 'Adventure');
INSERT INTO ClassifiesAnime (AnimeID, GenreName) VALUES (31240, 'Drama');
INSERT INTO ClassifiesAnime (AnimeID, GenreName) VALUES (31240, 'Suspense');

INSERT INTO ClassifiesManga (MangaID, GenreName) VALUES (598, 'Action');
INSERT INTO ClassifiesManga (MangaID, GenreName) VALUES (598, 'Adventure');
INSERT INTO ClassifiesManga (MangaID, GenreName) VALUES (598, 'Fantasy');
INSERT INTO ClassifiesManga (MangaID, GenreName) VALUES (96792, 'Action');
INSERT INTO ClassifiesManga (MangaID, GenreName) VALUES (96792, 'Fantasy');
INSERT INTO ClassifiesManga (MangaID, GenreName) VALUES (31240, 'Adventure');
INSERT INTO ClassifiesManga (MangaID, GenreName) VALUES (31240, 'Drama');


SET ANSI_WARNINGS OFF
INSERT INTO VoiceActor (VoiceActorID, VoiceActorName, VoiceActorJapName, VoiceActorBirthday, VoiceActorWebsite, VoiceActorTwitter, VoiceActorFacebook, VoiceActorBlog, VoiceActorInstagram) VALUES (34785, 'Takahashi, Rie', '李依','1980-04-22' , 'https://taka8rie.com/', 'http://twitter.com/share?related=MyAnimeList.net&via=myanimelist&url=https%3A%2F%2Fmyanimelist.net%2Fpeople%2F34785%2FTakahashi_Rie&text=Rie%20Takahashi&hashtags=', 'http://www.facebook.com/share.php?u=https%3A%2F%2Fmyanimelist.net%2Fpeople%2F34785%2FTakahashi_Rie', '', 'https://www.instagram.com/riery_syame/');
INSERT INTO VoiceActor (VoiceActorID, VoiceActorName, VoiceActorJapName, VoiceActorBirthday, VoiceActorWebsite, VoiceActorTwitter, VoiceActorFacebook, VoiceActorBlog, VoiceActorInstagram) VALUES (356, 'Shimono, Hiro', '紘', '1980-04-21', 'http://shimonohiro.com/', 'http://twitter.com/share?related=MyAnimeList.net&via=myanimelist&url=https%3A%2F%2Fmyanimelist.net%2Fpeople%2F356%2FShimono_Hiro&text=Hiro%20Shimono&hashtags=', 'http://www.facebook.com/share.php?u=https%3A%2F%2Fmyanimelist.net%2Fpeople%2F356%2FShimono_Hiro', 'http://kimadou.exblog.jp/', '');
INSERT INTO VoiceActor (VoiceActorID, VoiceActorName, VoiceActorJapName, VoiceActorBirthday, VoiceActorWebsite, VoiceActorTwitter, VoiceActorFacebook, VoiceActorBlog, VoiceActorInstagram) VALUES (8, 'Kugimiya, Rie', '理恵', '1979-05-30', 'http://ameblo.jp/kugimiyarie-blog/', 'http://twitter.com/share?related=MyAnimeList.net&via=myanimelist&url=https%3A%2F%2Fmyanimelist.net%2Fpeople%2F8%2FKugimiya_Rie&text=Rie%20Kugimiya&hashtags=', 'http://www.facebook.com/share.php?u=https%3A%2F%2Fmyanimelist.net%2Fpeople%2F8%2FKugimiya_Rie', 'http://www.imenterprise.jp/profile.php?id=52', '');
SET ANSI_WARNINGS ON

INSERT INTO Dubbing (Anime_AnimeID, Character_CharID, VoiceActor_VoiceActorID) VALUES (6702, 5188, 8);
INSERT INTO Dubbing (Anime_AnimeID, Character_CharID, VoiceActor_VoiceActorID) VALUES (38000, 146158, 356);
INSERT INTO Dubbing (Anime_AnimeID, Character_CharID, VoiceActor_VoiceActorID) VALUES (31240, 118737, 34785);

INSERT INTO favorites (UserID, CharID) VALUES (77777, 118737);
INSERT INTO favorites (UserID, CharID) VALUES (666, 146158);
INSERT INTO favorites (UserID, CharID) VALUES (747, 5188);

INSERT INTO ListsAnime (AnimeStatus, EpsSeen, AnimeScore, UserID, AnimeID) VALUES ('Completed', 26, 10.0, 747, 38000);
INSERT INTO ListsAnime (AnimeStatus, EpsSeen, AnimeScore, UserID, AnimeID) VALUES ('Watching', 18, 9.5, 666, 31240);
INSERT INTO ListsAnime (AnimeStatus, EpsSeen, AnimeScore, UserID, AnimeID) VALUES ('Plan to Watch','', 0, 77777, 6702);
INSERT INTO ListsAnime (AnimeStatus, EpsSeen, AnimeScore, UserID, AnimeID) VALUES ('Completed', 175, 10.0, 666, 6702);

INSERT INTO ListsManga (MangaStatus, MangaScore, VolumesRead, ChaptersRead, UserID, MangaID) VALUES ('Completed', 9.0, 36, 325, 666, 31240);
INSERT INTO ListsManga (MangaStatus, MangaScore, VolumesRead, ChaptersRead, UserID, MangaID) VALUES ('Reading', 10.0, 50, 435, 77777, 598);
INSERT INTO ListsManga (MangaStatus, MangaScore, VolumesRead, ChaptersRead, UserID, MangaID) VALUES ('Plan to Read','', 0, 0, 666, 96792);


INSERT INTO mangatopic (MangaID, ClubID) VALUES (598, 20081);
INSERT INTO mangatopic (MangaID, ClubID) VALUES (96792, 256);
INSERT INTO mangatopic (MangaID, ClubID) VALUES (31240, 32683);

INSERT INTO participates (UserID, ClubID, "Role") VALUES (77777, 20081, 'Admin');
INSERT INTO participates (UserID, ClubID, "Role") VALUES (666, 256, 'Creator');
INSERT INTO participates (UserID, ClubID, "Role") VALUES (747, 32683, 'Member');
INSERT INTO participates (UserID, ClubID, "Role") VALUES (747, 256, 'Oficer');

INSERT INTO Produces (AnimeID, CompanyID) VALUES (6702, 16);
INSERT INTO Produces (AnimeID, CompanyID) VALUES (38000, 17);
INSERT INTO Produces (AnimeID, CompanyID) VALUES (31240, 16);

INSERT INTO Serializes (CompanyID, MangaID) VALUES (1365, 96792);
INSERT INTO Serializes (CompanyID, MangaID) VALUES (1365, 31240);
INSERT INTO Serializes (CompanyID, MangaID) VALUES (159, 598);

INSERT INTO StreamingPlatform (StPlatName, StPlatStablishment) VALUES ('Crunchyroll', '2006-05-14');
INSERT INTO StreamingPlatform (StPlatName, StPlatStablishment) VALUES ('Netflix', '1997-8-29');
INSERT INTO StreamingPlatform (StPlatName, StPlatStablishment) VALUES ('Ani-One Asia', '1994-5-7');

INSERT INTO Streams (AnimeID, StPlatName) VALUES (6702, 'Crunchyroll');
INSERT INTO Streams (AnimeID, StPlatName) VALUES (38000, 'Ani-One Asia');
INSERT INTO Streams (AnimeID, StPlatName) VALUES (31240, 'Netflix');

INSERT INTO Works (VoiceActorID, CompanyID) VALUES (34785, 16);
INSERT INTO Works (VoiceActorID, CompanyID) VALUES (356, 17);
INSERT INTO Works (VoiceActorID, CompanyID) VALUES (8, 16);

INSERT INTO Writes (AuthorID, MangaID) VALUES (40398, 31240);
INSERT INTO Writes (AuthorID, MangaID) VALUES (1882, 598);
INSERT INTO Writes (AuthorID, MangaID) VALUES (19791, 96792);
