-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2022-11-03 14:37:45.456

-- tables
-- Table: Animates
CREATE TABLE Animates (
    CompanyID int  NOT NULL,
    AnimeID int  NOT NULL,
    CONSTRAINT Animates_pk PRIMARY KEY  (CompanyID,AnimeID)
);

-- Table: Anime
CREATE TABLE Anime (
    AnimeID int  NOT NULL,
    AnimeType varchar(45)  NOT NULL,
    AnimeSource varchar(45)  NOT NULL,
    AnimeDuration varchar(45)  NOT NULL,
    AnimeRating varchar(45)  NOT NULL,
    AnimeSynopsis text  NOT NULL,
    AnimeEngName nchar(45)  NOT NULL,
    AnimeJapName nchar(45)  NOT NULL,
    AnimeName nchar(45)  NOT NULL,
    MangaID int  NULL,
    AnimeAired varchar(45)  NOT NULL,
    AnimeEpisodes int  NOT NULL,
    AnimeStatus varchar(45)  NOT NULL,
    CONSTRAINT AK_2 UNIQUE (AnimeEngName),
    CONSTRAINT AK_3 UNIQUE (AnimeJapName),
    CONSTRAINT AK_4 UNIQUE (AnimeName),
    CONSTRAINT Anime_pk PRIMARY KEY  (AnimeID)
);

-- Table: AnimeTopic
CREATE TABLE AnimeTopic (
    ClubID int  NOT NULL,
    AnimeID int  NOT NULL,
    CONSTRAINT AnimeTopic_pk PRIMARY KEY  (ClubID,AnimeID)
);

-- Table: AppearsManga
CREATE TABLE AppearsManga (
    CharID int  NOT NULL,
    MangaID int  NOT NULL,
    CONSTRAINT AppearsManga_pk PRIMARY KEY  (CharID,MangaID)
);

-- Table: Author
CREATE TABLE Author (
    AuthorID int  NOT NULL,
    AuthorName nchar(45)  NOT NULL,
    AuthorFamilyName nchar(45)  NOT NULL,
    AuthorAlternativeName nchar(45)  NOT NULL,
    AuthorBirthday date  NULL,
    AuthorWebsite varchar(45)  NULL,
    AuthorTwitter varchar(45)  NULL,
    AuthorInstagram varchar(45)  NULL,
    AuthorFacebook varchar(45)  NULL,
    AuthorReddit varchar(45)  NULL,
    CONSTRAINT Author_pk PRIMARY KEY  (AuthorID)
);

-- Table: Blog
CREATE TABLE Blog (
    BlogID int  NOT NULL,
    BlogTitle nchar(45)  NOT NULL,
    BlogContent varchar(45)  NOT NULL,
    BlogPostDate date  NOT NULL,
    UserID int  NOT NULL,
    CONSTRAINT Blog_pk PRIMARY KEY  (BlogID)
);

-- Table: CharPicture
CREATE TABLE CharPicture (
    CharImgID int  NOT NULL,
    CharImgArchive image  NOT NULL,
    CharID int  NOT NULL,
    CONSTRAINT CharPicture_pk PRIMARY KEY  (CharImgID)
);

-- Table: CharTopic
CREATE TABLE CharTopic (
    ClubID int  NOT NULL,
    CharID int  NOT NULL,
    CONSTRAINT CharTopic_pk PRIMARY KEY  (ClubID,CharID)
);

-- Table: Character
CREATE TABLE Character (
    CharName nchar(45)  NOT NULL,
    CharID int  NOT NULL,
    CONSTRAINT Character_pk PRIMARY KEY  (CharID)
);

-- Table: ClassifiesAnime
CREATE TABLE ClassifiesAnime (
    AnimeID int  NOT NULL,
    GenreName varchar(45)  NOT NULL,
    CONSTRAINT ClassifiesAnime_pk PRIMARY KEY  (AnimeID,GenreName)
);

-- Table: ClassifiesManga
CREATE TABLE ClassifiesManga (
    GenreName varchar(45)  NOT NULL,
    MangaID int  NOT NULL,
    CONSTRAINT ClassifiesManga_pk PRIMARY KEY  (GenreName,MangaID)
);

-- Table: Club
CREATE TABLE Club (
    ClubID int  NOT NULL,
    ClubName nchar(45)  NOT NULL,
    ClubDescription text  NOT NULL,
    ClubCategory varchar(45)  NOT NULL,
    CONSTRAINT Club_pk PRIMARY KEY  (ClubID)
);

-- Table: ClubImage
CREATE TABLE ClubImage (
    ClubImgID int  NOT NULL,
    ClubImgArchive image  NOT NULL,
    ClubID int  NOT NULL,
    CONSTRAINT ClubImage_pk PRIMARY KEY  (ClubImgID)
);

-- Table: Company
CREATE TABLE Company (
    CompanyID int  NOT NULL,
    CompanyName nchar(45)  NOT NULL,
    CompanyJapName nchar(45)  NOT NULL,
    CompanyStablishment date  NOT NULL,
    CompanyTwitter varchar(45)  NULL,
    CompanyFacebook varchar(45)  NULL,
    CompanyInstagram varchar(45)  NULL,
    CompanyWebsite varchar(45)  NULL,
    CONSTRAINT Company_pk PRIMARY KEY  (CompanyID)
);

-- Table: DateAired
CREATE TABLE DateAired (
    AnimeAired varchar(45)  NOT NULL,
    AnimePremiered varchar(45)  NOT NULL,
    CONSTRAINT DateAired_pk PRIMARY KEY  (AnimeAired)
);

-- Table: Dubbing
CREATE TABLE Dubbing (
    Anime_AnimeID int  NOT NULL,
    Character_CharID int  NOT NULL,
    VoiceActor_VoiceActorID int  NOT NULL,
    CONSTRAINT Dubbing_pk PRIMARY KEY  (Anime_AnimeID,Character_CharID,VoiceActor_VoiceActorID)
);

-- Table: Favorites
CREATE TABLE Favorites (
    UserID int  NOT NULL,
    CharID int  NOT NULL,
    CONSTRAINT Favorites_pk PRIMARY KEY  (UserID,CharID)
);

-- Table: Genre
CREATE TABLE Genre (
    GenreName varchar(45)  NOT NULL,
    GenreDescription text  NOT NULL,
    CONSTRAINT Genre_pk PRIMARY KEY  (GenreName)
);

-- Table: ListsAnime
CREATE TABLE ListsAnime (
    AnimeStatus varchar(45)  NOT NULL,
    EpsSeen int  NOT NULL,
    AnimeScore float  NOT NULL,
    UserID int  NOT NULL,
    AnimeID int  NOT NULL,
    CONSTRAINT ListsAnime_pk PRIMARY KEY  (UserID,AnimeID)
);

-- Table: ListsManga
CREATE TABLE ListsManga (
    MangaStatus varchar(45)  NOT NULL,
    MangaScore float  NOT NULL,
    VolumesRead int  NOT NULL,
    ChaptersRead int  NOT NULL,
    UserID int  NOT NULL,
    MangaID int  NOT NULL,
    CONSTRAINT ListsManga_pk PRIMARY KEY  (UserID,MangaID)
);

-- Table: Manga
CREATE TABLE Manga (
    MangaVolumes int  NOT NULL,
    MangaChapters int  NOT NULL,
    MangaStatus varchar(45)  NOT NULL,
    MangaPublished varchar(45)  NOT NULL,
    MangaDemographic varchar(45)  NOT NULL,
    MangaID int  NOT NULL,
    MangaSynopsis text  NOT NULL,
    MangaName nchar(45)  NOT NULL,
    MangaJapName nchar(45)  NOT NULL,
    CONSTRAINT AK_0 UNIQUE (MangaName),
    CONSTRAINT AK_1 UNIQUE (MangaJapName),
    CONSTRAINT Manga_pk PRIMARY KEY  (MangaID)
);

-- Table: MangaTopic
CREATE TABLE MangaTopic (
    ClubID int  NOT NULL,
    MangaID int  NOT NULL,
    CONSTRAINT MangaTopic_pk PRIMARY KEY  (ClubID,MangaID)
);

-- Table: Participates
CREATE TABLE Participates (
    Role varchar(45)  NOT NULL,
    ClubID int  NOT NULL,
    UserID int  NOT NULL,
    CONSTRAINT Participates_pk PRIMARY KEY  (ClubID,UserID)
);

-- Table: Produces
CREATE TABLE Produces (
    AnimeID int  NOT NULL,
    CompanyID int  NOT NULL,
    CONSTRAINT Produces_pk PRIMARY KEY  (AnimeID,CompanyID)
);

-- Table: Serializes
CREATE TABLE Serializes (
    CompanyID int  NOT NULL,
    MangaID int  NOT NULL,
    CONSTRAINT Serializes_pk PRIMARY KEY  (CompanyID,MangaID)
);

-- Table: StreamingPlatform
CREATE TABLE StreamingPlatform (
    StPlatName nchar(45)  NOT NULL,
    StPlatStablishment date  NOT NULL,
    CONSTRAINT StreamingPlatform_pk PRIMARY KEY  (StPlatName)
);

-- Table: Streams
CREATE TABLE Streams (
    StPlatName nchar(45)  NOT NULL,
    AnimeID int  NOT NULL,
    CONSTRAINT Streams_pk PRIMARY KEY  (StPlatName,AnimeID)
);

-- Table: User
CREATE TABLE "User" (
    UserLastOnline datetime  NOT NULL,
    UserName nchar(45)  NOT NULL,
    UserID int  NOT NULL,
    UserGender varchar(45)  NULL,
    UserBirthday date  NULL,
    UserLocation varchar(45)  NULL,
    UserJoinDate date  NOT NULL,
    CONSTRAINT User_pk PRIMARY KEY  (UserID)
);

-- Table: VoiceActor
CREATE TABLE VoiceActor (
    VoiceActorID int  NOT NULL,
    VoiceActorBirthday date  NULL,
    VoiceActorWebsite varchar(45)  NULL,
    VoiceActorTwitter varchar(45)  NULL,
    VoiceActorFacebook varchar(45)  NULL,
    VoiceActorBlog varchar(45)  NULL,
    VoiceActorInstagram varchar(45)  NULL,
    VoiceActorName nchar(45)  NOT NULL,
    VoiceActorJapName nchar(45)  NOT NULL,
    CONSTRAINT VoiceActor_pk PRIMARY KEY  (VoiceActorID)
);

-- Table: Works
CREATE TABLE Works (
    VoiceActorID int  NOT NULL,
    CompanyID int  NOT NULL,
    CONSTRAINT Works_pk PRIMARY KEY  (VoiceActorID,CompanyID)
);

-- Table: Writes
CREATE TABLE Writes (
    AuthorID int  NOT NULL,
    MangaID int  NOT NULL,
    CONSTRAINT Writes_pk PRIMARY KEY  (AuthorID,MangaID)
);

-- foreign keys
-- Reference: Dubbing_Anime (table: Dubbing)
ALTER TABLE Dubbing ADD CONSTRAINT Dubbing_Anime
    FOREIGN KEY (Anime_AnimeID)
    REFERENCES Anime (AnimeID);

-- Reference: Dubbing_Character (table: Dubbing)
ALTER TABLE Dubbing ADD CONSTRAINT Dubbing_Character
    FOREIGN KEY (Character_CharID)
    REFERENCES Character (CharID);

-- Reference: Dubbing_VoiceActor (table: Dubbing)
ALTER TABLE Dubbing ADD CONSTRAINT Dubbing_VoiceActor
    FOREIGN KEY (VoiceActor_VoiceActorID)
    REFERENCES VoiceActor (VoiceActorID);

-- Reference: FK_0 (table: Blog)
ALTER TABLE Blog ADD CONSTRAINT FK_0
    FOREIGN KEY (UserID)
    REFERENCES "User" (UserID);

-- Reference: FK_1 (table: ClubImage)
ALTER TABLE ClubImage ADD CONSTRAINT FK_1
    FOREIGN KEY (ClubID)
    REFERENCES Club (ClubID);

-- Reference: FK_10 (table: Participates)
ALTER TABLE Participates ADD CONSTRAINT FK_10
    FOREIGN KEY (UserID)
    REFERENCES "User" (UserID);

-- Reference: FK_11 (table: Works)
ALTER TABLE Works ADD CONSTRAINT FK_11
    FOREIGN KEY (VoiceActorID)
    REFERENCES VoiceActor (VoiceActorID);

-- Reference: FK_12 (table: Works)
ALTER TABLE Works ADD CONSTRAINT FK_12
    FOREIGN KEY (CompanyID)
    REFERENCES Company (CompanyID);

-- Reference: FK_13 (table: AppearsManga)
ALTER TABLE AppearsManga ADD CONSTRAINT FK_13
    FOREIGN KEY (CharID)
    REFERENCES Character (CharID);

-- Reference: FK_14 (table: AppearsManga)
ALTER TABLE AppearsManga ADD CONSTRAINT FK_14
    FOREIGN KEY (MangaID)
    REFERENCES Manga (MangaID);

-- Reference: FK_15 (table: Writes)
ALTER TABLE Writes ADD CONSTRAINT FK_15
    FOREIGN KEY (AuthorID)
    REFERENCES Author (AuthorID);

-- Reference: FK_16 (table: Writes)
ALTER TABLE Writes ADD CONSTRAINT FK_16
    FOREIGN KEY (MangaID)
    REFERENCES Manga (MangaID);

-- Reference: FK_17 (table: Favorites)
ALTER TABLE Favorites ADD CONSTRAINT FK_17
    FOREIGN KEY (UserID)
    REFERENCES "User" (UserID);

-- Reference: FK_18 (table: Favorites)
ALTER TABLE Favorites ADD CONSTRAINT FK_18
    FOREIGN KEY (CharID)
    REFERENCES Character (CharID);

-- Reference: FK_19 (table: MangaTopic)
ALTER TABLE MangaTopic ADD CONSTRAINT FK_19
    FOREIGN KEY (ClubID)
    REFERENCES Club (ClubID);

-- Reference: FK_2 (table: CharPicture)
ALTER TABLE CharPicture ADD CONSTRAINT FK_2
    FOREIGN KEY (CharID)
    REFERENCES Character (CharID);

-- Reference: FK_20 (table: MangaTopic)
ALTER TABLE MangaTopic ADD CONSTRAINT FK_20
    FOREIGN KEY (MangaID)
    REFERENCES Manga (MangaID);

-- Reference: FK_21 (table: CharTopic)
ALTER TABLE CharTopic ADD CONSTRAINT FK_21
    FOREIGN KEY (ClubID)
    REFERENCES Club (ClubID);

-- Reference: FK_22 (table: CharTopic)
ALTER TABLE CharTopic ADD CONSTRAINT FK_22
    FOREIGN KEY (CharID)
    REFERENCES Character (CharID);

-- Reference: FK_23 (table: Anime)
ALTER TABLE Anime ADD CONSTRAINT FK_23
    FOREIGN KEY (MangaID)
    REFERENCES Manga (MangaID);

-- Reference: FK_24 (table: Anime)
ALTER TABLE Anime ADD CONSTRAINT FK_24
    FOREIGN KEY (AnimeAired)
    REFERENCES DateAired (AnimeAired);

-- Reference: FK_25 (table: Produces)
ALTER TABLE Produces ADD CONSTRAINT FK_25
    FOREIGN KEY (AnimeID)
    REFERENCES Anime (AnimeID);

-- Reference: FK_26 (table: Produces)
ALTER TABLE Produces ADD CONSTRAINT FK_26
    FOREIGN KEY (CompanyID)
    REFERENCES Company (CompanyID);

-- Reference: FK_27 (table: Animates)
ALTER TABLE Animates ADD CONSTRAINT FK_27
    FOREIGN KEY (CompanyID)
    REFERENCES Company (CompanyID);

-- Reference: FK_28 (table: Animates)
ALTER TABLE Animates ADD CONSTRAINT FK_28
    FOREIGN KEY (AnimeID)
    REFERENCES Anime (AnimeID);

-- Reference: FK_29 (table: ClassifiesAnime)
ALTER TABLE ClassifiesAnime ADD CONSTRAINT FK_29
    FOREIGN KEY (AnimeID)
    REFERENCES Anime (AnimeID);

-- Reference: FK_3 (table: ClassifiesManga)
ALTER TABLE ClassifiesManga ADD CONSTRAINT FK_3
    FOREIGN KEY (GenreName)
    REFERENCES Genre (GenreName);

-- Reference: FK_30 (table: ClassifiesAnime)
ALTER TABLE ClassifiesAnime ADD CONSTRAINT FK_30
    FOREIGN KEY (GenreName)
    REFERENCES Genre (GenreName);

-- Reference: FK_31 (table: ListsAnime)
ALTER TABLE ListsAnime ADD CONSTRAINT FK_31
    FOREIGN KEY (UserID)
    REFERENCES "User" (UserID);

-- Reference: FK_32 (table: ListsAnime)
ALTER TABLE ListsAnime ADD CONSTRAINT FK_32
    FOREIGN KEY (AnimeID)
    REFERENCES Anime (AnimeID);

-- Reference: FK_33 (table: Streams)
ALTER TABLE Streams ADD CONSTRAINT FK_33
    FOREIGN KEY (StPlatName)
    REFERENCES StreamingPlatform (StPlatName);

-- Reference: FK_34 (table: Streams)
ALTER TABLE Streams ADD CONSTRAINT FK_34
    FOREIGN KEY (AnimeID)
    REFERENCES Anime (AnimeID);

-- Reference: FK_35 (table: AnimeTopic)
ALTER TABLE AnimeTopic ADD CONSTRAINT FK_35
    FOREIGN KEY (ClubID)
    REFERENCES Club (ClubID);

-- Reference: FK_36 (table: AnimeTopic)
ALTER TABLE AnimeTopic ADD CONSTRAINT FK_36
    FOREIGN KEY (AnimeID)
    REFERENCES Anime (AnimeID);

-- Reference: FK_4 (table: ClassifiesManga)
ALTER TABLE ClassifiesManga ADD CONSTRAINT FK_4
    FOREIGN KEY (MangaID)
    REFERENCES Manga (MangaID);

-- Reference: FK_5 (table: Serializes)
ALTER TABLE Serializes ADD CONSTRAINT FK_5
    FOREIGN KEY (CompanyID)
    REFERENCES Company (CompanyID);

-- Reference: FK_6 (table: Serializes)
ALTER TABLE Serializes ADD CONSTRAINT FK_6
    FOREIGN KEY (MangaID)
    REFERENCES Manga (MangaID);

-- Reference: FK_7 (table: ListsManga)
ALTER TABLE ListsManga ADD CONSTRAINT FK_7
    FOREIGN KEY (UserID)
    REFERENCES "User" (UserID);

-- Reference: FK_8 (table: ListsManga)
ALTER TABLE ListsManga ADD CONSTRAINT FK_8
    FOREIGN KEY (MangaID)
    REFERENCES Manga (MangaID);

-- Reference: FK_9 (table: Participates)
ALTER TABLE Participates ADD CONSTRAINT FK_9
    FOREIGN KEY (ClubID)
    REFERENCES Club (ClubID);

-- End of file.