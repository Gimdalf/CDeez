from cd.utils import Driver
import json

x = '''[{"_id": "AAAS 106","subid":["ANTH 248","HIST 110"],"name":"THE MAKING OF MODERN AFRICA","terms":["Fall"],"prereqs":[],"subject":"AAAS","credits":4}
,{"_id": "AAAS 113","subid":[],"name":"AFRICAN AMERICANS IN SOUTH AFRICA","terms":["Fall"],"prereqs":[],"subject":"AAAS","credits":4}
,{"_id": "AAAS 121","subid":["ANTH 213","MUSC 121"],"name":"WORLD MUSIC","terms":["Fall"],"prereqs":[],"subject":"AAAS","credits":4}
,{"_id": "AAAS 150","subid":["HIST 150"],"name":"COLONIAL LATIN AMERICA","terms":["Fall"],"prereqs":[],"subject":"AAAS","credits":4}
,{"_id": "AAAS 154","subid":["DMST 153","EHUM 153","FMST 153","MUSC 173","SART 153"],"name":"INTRODUCTION TO SOUND ART","terms":["Fall"],"prereqs":[],"subject":"AAAS","credits":4}
,{"_id": "AAAS 165","subid":[],"name":"INTRODUCTORY MBIRA ENSEMBLE","terms":["Fall","Spring"],"prereqs":[],"subject":"AAAS","credits":1}
,{"_id": "AAAS 171","subid":["DANC 171"],"name":"CAPOEIRA:BRAZILIAN ART MOVEMENT","terms":["Fall"],"prereqs":[],"subject":"AAAS","credits":2}
,{"_id": "AAAS 184","subid":[],"name":"SANSIFANYI ENSEMBLE","terms":["Fall","Spring"],"prereqs":["THE 181","THE 182","THE 283","THE 253","THE 285","MUSC 168","MUSC 146"],"subject":"AAAS","credits":1}
,{"_id": "AAAS 188","subid":["DANC 188"],"name":"HIP HOP CULTURE AND BREAKING","terms":["Fall"],"prereqs":[],"subject":"AAAS","credits":2}
,{"_id": "AAAS 206","subid":["ENGL 236","FMST 266"],"name":"BLACK ADAPTATIONS","terms":["Fall"],"prereqs":[],"subject":"AAAS","credits":4}
,{"_id": "AAAS 210","subid":["DANC 212","MUSC 210","MUSC 410"],"name":"NGOMA:DRUM, DANCE, S AFRICA","terms":["Fall"],"prereqs":[],"subject":"AAAS","credits":4}
,{"_id": "AAAS 213","subid":["EHUM 213","GSWS 213","GSWS 213W"],"name":"POLITICS OF NATURE: GENDER, RACE, AND THE ENVIRONMENT","terms":["Fall"],"prereqs":[],"subject":"AAAS","credits":4}
,{"_id": "AAAS 215","subid":["HIST 251","HIST 251W"],"name":"AFRICAN DIASPORA IN LATIN AMERICA, 1441-1804","terms":["Fall"],"prereqs":[],"subject":"AAAS","credits":4}
,{"_id": "AAAS 224","subid":[],"name":"BLACK GEOGRAPHIES","terms":["Fall"],"prereqs":[],"subject":"AAAS","credits":4}
,{"_id": "AAAS 230","subid":["ENGL 230","ENGL 380","ENGL 430"],"name":"AFRICAN AMERICAN AUTOBIOGRAPHY","terms":["Fall"],"prereqs":[],"subject":"AAAS","credits":4}
,{"_id": "AAAS 235","subid":["ANTH 235","GSWS 234"],"name":"THE BLACK BODY","terms":["Fall"],"prereqs":[],"subject":"AAAS","credits":4}
,{"_id": "AAAS 245","subid":["EHUM 245","ENGL 212","FMST 274","SUST 245"],"name":"RACE, COLONIALISM, AND NATURE (FORMERLY ENVIRONMENTAL LITERATURE)","terms":["Fall"],"prereqs":[],"subject":"AAAS","credits":4}
,{"_id": "AAAS 254","subid":["DANC 181"],"name":"WEST AFRICAN DANCE FORMS I","terms":["Fall"],"prereqs":[],"subject":"AAAS","credits":2}
,{"_id": "AAAS 275","subid":["CLTR 275A","JPNS 275","MUSC 275"],"name":"HIP HOP JAPAN","terms":["Fall"],"prereqs":[],"subject":"AAAS","credits":4}
,{"_id": "AAAS 285","subid":["EHUM 284","GSWS 285","RELC 284"],"name":"CIVIL DISOBEDIENCE","terms":["Fall"],"prereqs":[],"subject":"AAAS","credits":4}
,{"_id": "AAAS 296","subid":["PSCI 213"],"name":"BLACK POLITICS","terms":["Fall"],"prereqs":[],"subject":"AAAS","credits":4}
,{"_id": "AAAS 303","subid":["AAAS 444","CLTR 221","CLTR 421","FREN 243","FREN 443","GSWS 244","GSWS 444"],"name":"MUTILATED BODIES: FROM TRADITIONS TO CUTTING-EDGE TECHNOLOGIES","terms":["Fall"],"prereqs":[],"subject":"AAAS","credits":4}
,{"_id": "AAAS 327","subid":[],"name":"SANSIFANYI:WEST AFRICAN DANCE &AMP; DRUM ENSEMBLE","terms":["Fall","Spring"],"prereqs":[],"subject":"AAAS","credits":3}
,{"_id": "AAAS 394","subid":[],"name":"INTERNSHIP","terms":["Fall"],"prereqs":[],"subject":"AAAS","credits":4}
,{"_id": "AAAS 395W","subid":[],"name":"INDEPENDENT RESEARCH","terms":["Fall"],"prereqs":[],"subject":"AAAS","credits":4}
,{"_id": "AAAS 124","subid":["MUSC 127A"],"name":"AMERICAN PROTEST MUSIC","terms":["Spring"],"prereqs":[],"subject":"AAAS","credits":4}
,{"_id": "AAAS 140","subid":["MUSC 139","RELC 168"],"name":"RELIGION AND BLACK POP MUSIC","terms":["Spring"],"prereqs":[],"subject":"AAAS","credits":4}
,{"_id": "AAAS 142","subid":["HIST 171"],"name":"AFRICAN-AMERICAN HISTORY II SINCE 1900","terms":["Spring"],"prereqs":[],"subject":"AAAS","credits":4}
,{"_id": "AAAS 156","subid":["ENGL 116","GSWS 155"],"name":"INTRO TO AFRICAN-AMERICAN LITERATURE","terms":["Spring"],"prereqs":[],"subject":"AAAS","credits":4}
,{"_id": "AAAS 183","subid":["HIST 112","PSCI 224","RELC 183"],"name":"INCARCERATION NATION","terms":["Spring"],"prereqs":[],"subject":"AAAS","credits":4}
,{"_id": "AAAS 200","subid":["ANTH 233","GSWS 233","PSCI 225","RELC 230"],"name":"CLTRL POLITICS PRISON TOWNS","terms":["Spring"],"prereqs":[],"subject":"AAAS","credits":4}
,{"_id": "AAAS 201","subid":["HIST 228","HIST 228W"],"name":"NORTH AFRICA AND THE MIDDLE EAST SINCE 1838","terms":["Spring"],"prereqs":[],"subject":"AAAS","credits":4}
,{"_id": "AAAS 208","subid":["GSWS 282","SPAN 282","SPAN 482"],"name":"SI EL NORTE FUERA EL SUR: LATINX LITERATURE AND THOUGHT&NBSP;&NBSP;&NBSP;","terms":["Spring"],"prereqs":["SPAN 200"],"subject":"AAAS","credits":4}
,{"_id": "AAAS 211","subid":["AMST 200","ENGL 242","ENGL 429","HIST 264"],"name":"IDEAS OF AMERICA","terms":["Spring"],"prereqs":[],"subject":"AAAS","credits":4}
,{"_id": "AAAS 212","subid":["PSCI 214"],"name":"RACE AND THE LAW","terms":["Spring"],"prereqs":[],"subject":"AAAS","credits":4}
,{"_id": "AAAS 217","subid":["AHST 240","AHST 440","FMST 211"],"name":"AFRICAN AMERICAN CINEMA AND ITS CONTEXTS","terms":["Spring"],"prereqs":[],"subject":"AAAS","credits":4}
,{"_id": "AAAS 221","subid":["ANTH 243","EHUM 243","GSWS 236"],"name":"ENERGY AND POWER","terms":["Spring"],"prereqs":[],"subject":"AAAS","credits":4}
,{"_id": "AAAS 222","subid":["ANTH 240","GSWS 241","MUSC 236","MUSC 436","PHLT 227"],"name":"MUSIC, ETHNOGRAPHY &AMP; HIV/AIDS","terms":["Spring"],"prereqs":[],"subject":"AAAS","credits":4}
,{"_id": "AAAS 225","subid":[],"name":"PUBLIC POLICY AND BLACK COMMUNITIES:  EDUCATION, POVERTY, AFFIRMATIVE ACTION, AND CRIME","terms":["Spring"],"prereqs":[],"subject":"AAAS","credits":4}
,{"_id": "AAAS 234","subid":["DANC 253"],"name":"WEST AFRICAN DANCE: CONTEXT &AMP; PRACTICE","terms":["Spring"],"prereqs":[],"subject":"AAAS","credits":4}
,{"_id": "AAAS 247","subid":["AAAS 447","CLTR 229A","CLTR 429A"],"name":"BIOGRAPHIES OF EMANCIPATION IN THE BLACK WORLD","terms":["Spring"],"prereqs":[],"subject":"AAAS","credits":4}
,{"_id": "AAAS 256","subid":["ENGL 225","ENGL 425","HIST 268A"],"name":"AMERICAN RENAISSANCE","terms":["Spring"],"prereqs":[],"subject":"AAAS","credits":4}
,{"_id": "AAAS 280","subid":["AAAS 412","CLTR 229B","CLTR 429B","FREN 228","FREN 428"],"name":"HUMANITARIANISM AND SOCIAL INSECURITIES","terms":["Spring"],"prereqs":[],"subject":"AAAS","credits":4}
,{"_id": "AAAS 298","subid":[],"name":"CRITICAL RACE THEORIES","terms":["Spring"],"prereqs":[],"subject":"AAAS","credits":4}
,{"_id": "ACC 201","subid":[],"name":"FINANCIAL ACCOUNTING","terms":["Fall","Spring"],"prereqs":[],"subject":"ACC","credits":4}
,{"_id": "ACC 224","subid":[],"name":"INTERMEDIATE ACCOUNTING I","terms":["Fall"],"prereqs":["ACC 201"],"subject":"ACC","credits":4}
,{"_id": "ACC 226","subid":[],"name":"AUDITING","terms":["Fall"],"prereqs":["ACC 225"],"subject":"ACC","credits":4}
,{"_id": "ACC 227","subid":[],"name":"INDIVIDUAL INCOME TAX","terms":["Fall"],"prereqs":["ACC 225"],"subject":"ACC","credits":4}
,{"_id": "ACC 221","subid":[],"name":"MANAGERIAL ACCOUNTING","terms":["Spring"],"prereqs":["ACC 221","ACC 201"],"subject":"ACC","credits":4}
,{"_id": "ACC 222","subid":[],"name":"FINANCIAL STATEMENT ANALYSIS","terms":["Spring"],"prereqs":[],"subject":"ACC","credits":4}
,{"_id": "ACC 225","subid":[],"name":"INTERMEDIATE ACCOUNTING II","terms":["Spring"],"prereqs":[],"subject":"ACC","credits":4}
,{"_id": "ACC 228","subid":[],"name":"CORPORATE, GIFT &AMP; ESTATE TAX","terms":["Spring"],"prereqs":[],"subject":"ACC","credits":4}
,{"_id": "AHST 101","subid":[],"name":"INTRO ART &AMP; VIS CULTURE","terms":["Fall"],"prereqs":[],"subject":"AHST","credits":4}
,{"_id": "AHST 127","subid":[],"name":"ART AND ARCHITECTURE OF ANCIENT EGYPT","terms":["Fall","Spring"],"prereqs":[],"subject":"AHST","credits":4}
,{"_id": "AHST 136","subid":["ENGL 117","FMST 132"],"name":"INTRO TO THE ART OF FILM","terms":["Fall","Spring"],"prereqs":[],"subject":"AHST","credits":4}
,{"_id": "AHST 137","subid":[],"name":"INTRO TO MODERN ARCHITECTURE","terms":["Fall"],"prereqs":[],"subject":"AHST","credits":4}
,{"_id": "AHST 142","subid":[],"name":"ARTS OF EAST ASIA","terms":["Fall"],"prereqs":[],"subject":"AHST","credits":4}
,{"_id": "AHST 148","subid":["ATHS 163","RELC 173"],"name":"INTRODUCTION TO ART AND ARCHITECTURE OF SOUTH ASIA","terms":["Fall"],"prereqs":[],"subject":"AHST","credits":4}
,{"_id": "AHST 202","subid":["AHST 402"],"name":"PHOTOGRAPHIES BEFORE ART","terms":["Fall"],"prereqs":[],"subject":"AHST","credits":4}
,{"_id": "AHST 209","subid":["SART 209"],"name":"WRITING ON ART","terms":["Fall"],"prereqs":[],"subject":"AHST","credits":4}
,{"_id": "AHST 212","subid":["CLTR 208A","HIST 146","JPNS 210","RELC 132"],"name":"VENGEANCE, LONGING, AND SALVATION: TOPICS IN �TRADITIONAL� JAPANESE CULTURE","terms":["Fall"],"prereqs":[],"subject":"AHST","credits":4}
,{"_id": "AHST 216","subid":["AHST 416","CLTR 208H","CLTR 408H","JPNS 216","RELC 225"],"name":"CULTURES OF ENLIGHTENMENT: MEDITATION, MATERIALITY, AND THE LITERARY CULTURES OF JAPANESE BUDDHISM","terms":["Fall"],"prereqs":[],"subject":"AHST","credits":4}
,{"_id": "AHST 231","subid":["SART 279"],"name":"GALLERY PRACTICUM","terms":["Fall","Spring"],"prereqs":[],"subject":"AHST","credits":4}
,{"_id": "AHST 252","subid":["ENGL 255","ENGL 455","FMST 247"],"name":"FILM HISTORY: EARLY CINEMA","terms":["Fall"],"prereqs":[],"subject":"AHST","credits":4}
,{"_id": "AHST 254","subid":["AHST 454","ENGL 257","ENGL 457","FMST 249"],"name":"FILM HISTORY: 1959-1989","terms":["Fall"],"prereqs":[],"subject":"AHST","credits":4}
,{"_id": "AHST 259","subid":["AHST 459"],"name":"ISLAMIC TEXTILES: SOCIETY, ECONOMY, POLITICS","terms":["Fall","Spring"],"prereqs":[],"subject":"AHST","credits":4}
,{"_id": "AHST 277","subid":["ENGL 380","ENGL 462","FMST 224"],"name":"AMERICAN EXPERIMENTS","terms":["Fall"],"prereqs":[],"subject":"AHST","credits":4}
,{"_id": "AHST 284","subid":["AHST 484","ENGL 251A","FMST 244"],"name":"THE ROAD MOVIE","terms":["Fall"],"prereqs":[],"subject":"AHST","credits":4}
,{"_id": "AHST 393","subid":[],"name":"ART HISTORY HONORS PROJECT","terms":["Fall","Spring"],"prereqs":[],"subject":"AHST","credits":4}
,{"_id": "AHST 394","subid":[],"name":"INTERNSHIP","terms":["Fall"],"prereqs":[],"subject":"AHST","credits":0}
,{"_id": "AHST 396","subid":[],"name":"MUSEUM INTERNSHIP","terms":["Fall","Spring"],"prereqs":[],"subject":"AHST","credits":4}
,{"_id": "AHST 583","subid":["CLTR 462"],"name":"VCS COLLOQUIUM","terms":["Fall"],"prereqs":[],"subject":"AHST","credits":4}
,{"_id": "AHST 595","subid":[],"name":"PHD RESEARCH / VIS &AMP; CULT STUDIES","terms":["Fall","Spring"],"prereqs":[],"subject":"AHST","credits":12}
,{"_id": "AHST 995","subid":[],"name":"CONT OF DOCTORAL ENROLLMENT","terms":["Fall","Spring"],"prereqs":[],"subject":"AHST","credits":0}
,{"_id": "AHST 997","subid":[],"name":"DOCTORAL DISSERTATION","terms":["Fall","Summer","Spring"],"prereqs":[],"subject":"AHST","credits":0}
,{"_id": "AHST 999","subid":[],"name":"DOCTORAL DISSERTATION","terms":["Fall","Spring"],"prereqs":[],"subject":"AHST","credits":0}
,{"_id": "AHST 986V","subid":[],"name":"FULL TIME VISITING STUDENT","terms":["Summer"],"prereqs":[],"subject":"AHST","credits":0}
,{"_id": "AHST 100","subid":["GSWS 123"],"name":"INTRODUCTION TO VISUAL AND CULTURAL STUDIES","terms":["Spring"],"prereqs":[],"subject":"AHST","credits":4}
,{"_id": "AHST 102","subid":["ENGL 118","FMST 131"],"name":"INTRO TO MEDIA STUDIES","terms":["Spring"],"prereqs":[],"subject":"AHST","credits":4}
,{"_id": "AHST 114","subid":["SART 114"],"name":"CREATING ARCHITECTURE","terms":["Spring"],"prereqs":[],"subject":"AHST","credits":4}
,{"_id": "AHST 128","subid":[],"name":"MODERN ART","terms":["Spring"],"prereqs":[],"subject":"AHST","credits":4}
,{"_id": "AHST 140","subid":["ATHS 210","CLST 134","HIST 117"],"name":"ARCHAEOLOGICAL THOUGHT","terms":["Spring"],"prereqs":[],"subject":"AHST","credits":4}
,{"_id": "AHST 172","subid":["FMST 103","GSWS 100"],"name":"TOPICS IN GSWS: TV DREAMS AND GENDERED SCREENS","terms":["Spring"],"prereqs":[],"subject":"AHST","credits":4}
,{"_id": "AHST 183","subid":[],"name":"BEYOND BANKSY: A CRITICAL INTRODUCTION TO STREET ART AND GRAFFITI","terms":["Spring"],"prereqs":[],"subject":"AHST","credits":4}
,{"_id": "AHST 199","subid":["CLST 131","HIST 104"],"name":"ANCIENT CITIES OF THE MEDITERRANEAN","terms":["Spring"],"prereqs":[],"subject":"AHST","credits":4}
,{"_id": "AHST 208","subid":["AHST 408"],"name":"CITIES OF THE WORLD:  BABYLON TO BRASILIA","terms":["Spring"],"prereqs":[],"subject":"AHST","credits":4}
,{"_id": "AHST 215","subid":["AHST 415"],"name":"SEMINAR ON CONTEMPORARY ART: MUSEUMS","terms":["Spring"],"prereqs":[],"subject":"AHST","credits":4}
,{"_id": "AHST 219","subid":["AHST 419"],"name":"THE 21ST CENTURY ART MUSEUM: AN INTRODUCTION TO MUSEUM STUDIES","terms":["Spring"],"prereqs":[],"subject":"AHST","credits":4}
,{"_id": "AHST 225","subid":["CLST 230","CLST 230W"],"name":"GREEK ART &AMP; ARCHAEOLOGY","terms":["Spring"],"prereqs":[],"subject":"AHST","credits":4}
,{"_id": "AHST 232","subid":["ANTH 296","ATHS 212","HIST 220"],"name":"ART HISTORY AND ETHNOARCHAEOLOGY OF WEST AFRICA","terms":["Spring"],"prereqs":[],"subject":"AHST","credits":4}
,{"_id": "AHST 240","subid":["AAAS 217","AHST 440","FMST 211"],"name":"AFRICAN AMERICAN CINEMA AND ITS CONTEXTS","terms":["Spring"],"prereqs":[],"subject":"AHST","credits":4}
,{"_id": "AHST 244","subid":[],"name":"MONUMENTS OF ANCIENT ITALY AREZZO","terms":["Spring"],"prereqs":[],"subject":"AHST","credits":4}
,{"_id": "AHST 260","subid":[],"name":"TOURIST JAPAN","terms":["Spring"],"prereqs":[],"subject":"AHST","credits":4}
,{"_id": "AHST 275","subid":["AHST 475"],"name":"PAPER AND DEATH/CRITICAL PAPER","terms":["Spring"],"prereqs":[],"subject":"AHST","credits":4}
,{"_id": "AHST 282","subid":["DMST 271"],"name":"HISTORY OF GRAPHIC DESIGN","terms":["Spring"],"prereqs":[],"subject":"AHST","credits":4}
,{"_id": "AHST 286A","subid":["ATHS 233A","SUST 233A"],"name":"CLIMATE CHANGE AND THE AFRICAN CULTURAL HERITAGE","terms":["Spring"],"prereqs":[],"subject":"AHST","credits":4}
,{"_id": "AHST 300","subid":[],"name":"ART NEW YORK NEW FIELD STUDIO","terms":["Spring"],"prereqs":[],"subject":"AHST","credits":4}
,{"_id": "AHST 305K","subid":[],"name":"ART NEW YORK COLLOQUIM","terms":["Spring"],"prereqs":[],"subject":"AHST","credits":4}
,{"_id": "AHST 346","subid":["AHST 546","EHUM 346"],"name":"ARCTIC VISION","terms":["Spring"],"prereqs":[],"subject":"AHST","credits":4}
,{"_id": "AHST 392A","subid":[],"name":"PRACTICUM - ART NY","terms":["Spring"],"prereqs":[],"subject":"AHST","credits":8}
,{"_id": "AHST 395","subid":[],"name":"INDEPENDENT RESEARCH","terms":["Spring"],"prereqs":[],"subject":"AHST","credits":0}
,{"_id": "AHST 397","subid":[],"name":"EUROPEAN ARTS INTERNSHIP","terms":["Spring"],"prereqs":[],"subject":"AHST","credits":8}
,{"_id": "AHST 591","subid":[],"name":"INDEPENDENT STUDY","terms":["Spring"],"prereqs":[],"subject":"AHST","credits":5}
,{"_id": "AHST 594","subid":[],"name":"PHD RESEARCH INTERNSHIP","terms":["Spring"],"prereqs":[],"subject":"AHST","credits":1}
,{"_id": "AHST 595A","subid":[],"name":"PHD RESEARCH IN ABSENTIA","terms":["Spring"],"prereqs":[],"subject":"AHST","credits":12}
,{"_id": "AHST 595B","subid":[],"name":"PHD RSRCH IN ABSENTIA ABROAD","terms":["Spring"],"prereqs":[],"subject":"AHST","credits":12}
,{"_id": "AHST 997A","subid":[],"name":"DOCT DISSERTATN IN ABSENTIA","terms":["Spring"],"prereqs":[],"subject":"AHST","credits":0}
,{"_id": "AHST 999A","subid":[],"name":"DOCTORAL DISSERTATION IN ABSENTIA","terms":["Spring"],"prereqs":[],"subject":"AHST","credits":0}
,{"_id": "AHST 999B","subid":[],"name":"DOC DISS IN-ABSENTIA ABROAD","terms":["Spring"],"prereqs":[],"subject":"AHST","credits":0}
,{"_id": "AME 140","subid":["EAS 103","ECE 140","MUSC 141"],"name":"INTRO TO AUDIO MUSIC &AMP; ENGIN","terms":["Fall"],"prereqs":["AME 140"],"subject":"AME","credits":4}
,{"_id": "AME 191","subid":["DMST 121","MUSC 191"],"name":"ART AND TECH OF RECORDING","terms":["Fall","Spring"],"prereqs":[],"subject":"AME","credits":4}
,{"_id": "AME 192","subid":["DMST 122","MUSC 192"],"name":"LISTENING AND AUDIO PROD","terms":["Fall","Spring"],"prereqs":["AME 191"],"subject":"AME","credits":4}
,{"_id": "AME 193","subid":["DMST 123","MUSC 193"],"name":"COMPUTER SOUND DESIGN","terms":["Fall","Spring"],"prereqs":[],"subject":"AME","credits":4}
,{"_id": "AME 194","subid":[],"name":"AUDIO FOR VISUAL MEDIA","terms":["Fall","Spring"],"prereqs":["AME 193"],"subject":"AME","credits":4}
,{"_id": "AME 223","subid":["ECE 429"],"name":"AUDIO ELECTRONICS","terms":["Fall"],"prereqs":[],"subject":"AME","credits":4}
,{"_id": "AME 264","subid":["ECE 476","TEE 476"],"name":"AUDIO SOFTWARE DES II","terms":["Fall"],"prereqs":["AME 262","ECE 475"],"subject":"AME","credits":4}
,{"_id": "AME 294","subid":[],"name":"AUDIO DSP PORTFOLIO","terms":["Fall"],"prereqs":["AME 272","ECE 210"],"subject":"AME","credits":2}
,{"_id": "AME 386","subid":[],"name":"SENIOR DES PORTFOLIO I","terms":["Fall"],"prereqs":["AME 223","AME 233","AME 272"],"subject":"AME","credits":2}
,{"_id": "AME 395","subid":[],"name":"INDEPENDENT RESEARCH","terms":["Fall"],"prereqs":[],"subject":"AME","credits":4}
,{"_id": "AME 460","subid":[],"name":"DIGITAL PROGRAMS &AMP; PROG I","terms":["Fall","Spring"],"prereqs":[],"subject":"AME","credits":4}
,{"_id": "AME 461","subid":[],"name":"DIGITAL PROGRAM. AND PROG II","terms":["Fall","Spring"],"prereqs":[],"subject":"AME","credits":4}
,{"_id": "AME 141","subid":[],"name":"FUNDMNTLS. OF DIGITAL AUDIO","terms":["Spring"],"prereqs":[],"subject":"AME","credits":4}
,{"_id": "AME 196","subid":[],"name":"INTERACTIVE COMPUTER MUSIC","terms":["Spring"],"prereqs":[],"subject":"AME","credits":4}
,{"_id": "AME 197","subid":["ECE 473"],"name":"AUDIO FOR GAMING","terms":["Spring"],"prereqs":["AME 193","AME 194"],"subject":"AME","credits":4}
,{"_id": "AME 198","subid":[],"name":"DESIGNING THE LIVING RECORDING STUDIO","terms":["Spring"],"prereqs":[],"subject":"AME","credits":4}
,{"_id": "AME 233","subid":["ECE 233","ECE 433","PHYS 233","TEE 433"],"name":"MUSICAL ACOUSTICS","terms":["Spring"],"prereqs":["THE 165","THE 121"],"subject":"AME","credits":4}
,{"_id": "AME 262","subid":["ECE 475","TEE 475"],"name":"AUDIO SOFTWARE DESIGN","terms":["Spring"],"prereqs":["ECE 114"],"subject":"AME","credits":4}
,{"_id": "AME 272","subid":["ECE 272","ECE 472","TEE 472"],"name":"AUDIO DIG SIGNAL PROCESSING","terms":["Spring"],"prereqs":[],"subject":"AME","credits":4}
,{"_id": "AME 292","subid":[],"name":"ACOUSTICS PORTFOLIO","terms":["Spring"],"prereqs":[],"subject":"AME","credits":2}
,{"_id": "AME 293","subid":["ECE 480"],"name":"ADV. AUDIO AMPLIFIER DESIGN","terms":["Spring"],"prereqs":[],"subject":"AME","credits":4}
,{"_id": "AME 295","subid":[],"name":"AUDIO ELECTRONICS PORTFOLIO","terms":["Spring"],"prereqs":[],"subject":"AME","credits":2}
,{"_id": "AME 387","subid":[],"name":"SENIOR DESIGN PROJECT II","terms":["Spring"],"prereqs":[],"subject":"AME","credits":4}
,{"_id": "AME 491","subid":[],"name":"INDEPENDENT STUDY: VOCAL MIXING TECHNIQUES","terms":["Spring"],"prereqs":[],"subject":"AME","credits":2}
,{"_id": "AMST 200","subid":["AAAS 211","ENGL 242","ENGL 429","HIST 264"],"name":"THE IDEA OF AMERICA","terms":["Spring"],"prereqs":[],"subject":"AMST","credits":4}
,{"_id": "ANTH 101","subid":[],"name":"BEING HUMAN: CULTURAL ANTHROPOLOGY","terms":["Fall","Spring"],"prereqs":[],"subject":"ANTH","credits":4}
,{"_id": "ANTH 102","subid":["GSWS 115"],"name":"INTRO TO MED ANTHROPOLOGY","terms":["Fall"],"prereqs":[],"subject":"ANTH","credits":4}
,{"_id": "ANTH 104","subid":[],"name":"REFUGEES IN THE U.S.","terms":["Fall"],"prereqs":[],"subject":"ANTH","credits":4}
,{"_id": "ANTH 105","subid":["LING 104"],"name":"LANGUAGE &AMP; CULTURE","terms":["Fall"],"prereqs":[],"subject":"ANTH","credits":4}
,{"_id": "ANTH 200","subid":[],"name":"ANTHRO. RESEARCH &AMP; METHODS","terms":["Fall"],"prereqs":["THE 101"],"subject":"ANTH","credits":4}
,{"_id": "ANTH 201","subid":[],"name":"ANTHROPOLOGICAL THEORY: PAST AND PRESENT","terms":["Fall"],"prereqs":[],"subject":"ANTH","credits":4}
,{"_id": "ANTH 213","subid":["AAAS 121","MUSC 121"],"name":"WORLD MUSIC IN CONTEXT","terms":["Fall"],"prereqs":[],"subject":"ANTH","credits":4}
,{"_id": "ANTH 220","subid":["ANTH 420"],"name":"PERSONHOOD","terms":["Fall"],"prereqs":[],"subject":"ANTH","credits":4}
,{"_id": "ANTH 229","subid":["ANTH 429"],"name":"LINGUISTIC ANTHROPOLOGY","terms":["Fall"],"prereqs":[],"subject":"ANTH","credits":4}
,{"_id": "ANTH 231","subid":[],"name":"IL(LEGAL) ANTHROPOLOGY","terms":["Fall"],"prereqs":[],"subject":"ANTH","credits":4}
,{"_id": "ANTH 235","subid":["AAAS 235","GSWS 234"],"name":"THE BLACK BODY","terms":["Fall"],"prereqs":[],"subject":"ANTH","credits":4}
,{"_id": "ANTH 248","subid":["AAAS 106","HIST 110"],"name":"THE MAKING OF MODERN AFRICA","terms":["Fall"],"prereqs":[],"subject":"ANTH","credits":4}
,{"_id": "ANTH 261","subid":[],"name":"LEAF SEMINAR","terms":["Fall"],"prereqs":[],"subject":"ANTH","credits":4}
,{"_id": "ANTH 302","subid":["ANTH 502"],"name":"ADV TOPICS SEM: WASTE AND WASTING","terms":["Fall"],"prereqs":["ANTH 101","ANTH 200"],"subject":"ANTH","credits":4}
,{"_id": "ANTH 390","subid":[],"name":"SUPERVISED TEACHING ANTH 101","terms":["Fall","Spring"],"prereqs":[],"subject":"ANTH","credits":4}
,{"_id": "ANTH 391","subid":[],"name":"INDEPENDENT STUDY","terms":["Fall"],"prereqs":[],"subject":"ANTH","credits":4}
,{"_id": "ANTH 394","subid":[],"name":"INTERNSHIP","terms":["Fall"],"prereqs":[],"subject":"ANTH","credits":0}
,{"_id": "ANTH 395","subid":[],"name":"INDEPENDENT RESEARCH","terms":["Fall"],"prereqs":[],"subject":"ANTH","credits":4}
,{"_id": "ANTH 395H","subid":[],"name":"ANTHROPOLOGY HONORS RESEARCH","terms":["Fall","Spring"],"prereqs":[],"subject":"ANTH","credits":4}
,{"_id": "ANTH 202","subid":[],"name":"MODERN SOCIAL THEORY","terms":["Spring"],"prereqs":[],"subject":"ANTH","credits":4}
,{"_id": "ANTH 204","subid":[],"name":"READING ETHNOGRAPHY","terms":["Spring"],"prereqs":["THE 101"],"subject":"ANTH","credits":4}
,{"_id": "ANTH 205","subid":["EHUM 205"],"name":"THEORIES &AMP; DEBATES: CULTURE VS. ONTOLOGY","terms":["Spring"],"prereqs":[],"subject":"ANTH","credits":4}
,{"_id": "ANTH 215","subid":["PHLT 215W"],"name":"PUBLIC HEALTH ANTHROPOLOGY","terms":["Spring"],"prereqs":[],"subject":"ANTH","credits":4}
,{"_id": "ANTH 216","subid":[],"name":"MEDICAL ANTHROPOLOGY","terms":["Spring"],"prereqs":[],"subject":"ANTH","credits":4}
,{"_id": "ANTH 224","subid":["SUST 224"],"name":"ANTHROPOLOGY OF DEVELOPMENT","terms":["Spring"],"prereqs":[],"subject":"ANTH","credits":4}
,{"_id": "ANTH 232","subid":["EHUM 232"],"name":"INDIGENOUS PEOPLE'S MOVEMENT","terms":["Spring"],"prereqs":[],"subject":"ANTH","credits":4}
,{"_id": "ANTH 233","subid":["AAAS 200","GSWS 233","PSCI 225","RELC 230"],"name":"CULTURAL POLITICS OF PRISON TOWNS","terms":["Spring"],"prereqs":[],"subject":"ANTH","credits":4}
,{"_id": "ANTH 240","subid":["AAAS 222","GSWS 241","MUSC 236","MUSC 436","PHLT 227"],"name":"MUSIC, ETHNOGRAPHY &AMP; HIV/AIDS","terms":["Spring"],"prereqs":[],"subject":"ANTH","credits":4}
,{"_id": "ANTH 243","subid":["AAAS 221","EHUM 243","GSWS 236"],"name":"ENERGY AND POWER","terms":["Spring"],"prereqs":[],"subject":"ANTH","credits":4}
,{"_id": "ANTH 251","subid":["RELC 247"],"name":"ISLAMIC MODERNITIES IN AFRICA","terms":["Spring"],"prereqs":[],"subject":"ANTH","credits":4}
,{"_id": "ANTH 257","subid":["ANTH 457"],"name":"CONTEMPORARY CHINESE SOCIETY","terms":["Spring"],"prereqs":[],"subject":"ANTH","credits":4}
,{"_id": "ANTH 262","subid":[],"name":"SPRING LEAF SEMINAR","terms":["Spring"],"prereqs":[],"subject":"ANTH","credits":2}
,{"_id": "ANTH 265","subid":["PHLT 265W"],"name":"GLOBAL HEALTH","terms":["Spring"],"prereqs":[],"subject":"ANTH","credits":4}
,{"_id": "ANTH 296","subid":["AHST 232","ATHS 212","HIST 220"],"name":"ART HISTORY AND ETHNOARCHAEOLOGY OF WEST AFRICA","terms":["Spring"],"prereqs":[],"subject":"ANTH","credits":4}
,{"_id": "ANTH 315","subid":[],"name":"ADVANCED TOPICS: BORDERS AND BOUNDARIES","terms":["Spring"],"prereqs":["ANTH 200"],"subject":"ANTH","credits":4}
,{"_id": "ANTH 405","subid":[],"name":"THEORIES &AMP; DEBATES: CULTURE VS. ONTOLOGY","terms":["Spring"],"prereqs":[],"subject":"ANTH","credits":4}
,{"_id": "ANTH 432","subid":[],"name":"INDIGENOUS PEOPLE'S MOVEMENT","terms":["Spring"],"prereqs":[],"subject":"ANTH","credits":4}
,{"_id": "ANTH 433","subid":[],"name":"CULTURAL POLITICS OF PRISON TOWNS","terms":["Spring"],"prereqs":[],"subject":"ANTH","credits":4}
,{"_id": "ARBC 101","subid":[],"name":"ELEMENTARY ARABIC I","terms":["Fall"],"prereqs":[],"subject":"ARBC","credits":4}
,{"_id": "ARBC 103","subid":[],"name":"INTERMEDIATE ARABIC","terms":["Fall"],"prereqs":[],"subject":"ARBC","credits":4}
,{"_id": "ARBC 149","subid":["RELC 149"],"name":"THE MIDDLE EAST: REVOLUTION, WAR AND DISSENT","terms":["Fall"],"prereqs":[],"subject":"ARBC","credits":4}
,{"_id": "ARBC 205","subid":[],"name":"ADV ARABIC PROSE SEMINAR II","terms":["Fall"],"prereqs":[],"subject":"ARBC","credits":4}
,{"_id": "ARBC 394","subid":[],"name":"INTERNSHIP","terms":["Fall"],"prereqs":[],"subject":"ARBC","credits":0}
,{"_id": "ARBC 102","subid":[],"name":"ELEMENTARY ARABIC II","terms":["Spring"],"prereqs":[],"subject":"ARBC","credits":4}
,{"_id": "ARBC 104","subid":[],"name":"INTERMEDIATE ARABIC II","terms":["Spring"],"prereqs":[],"subject":"ARBC","credits":4}
,{"_id": "ARBC 206","subid":[],"name":"ADV ARABIC PROSE SEM III","terms":["Spring"],"prereqs":[],"subject":"ARBC","credits":4}
,{"_id": "ASLA 101","subid":[],"name":"BEGINNING AMER SIGN LANG I","terms":["Fall","Summer","Spring"],"prereqs":[],"subject":"ASLA","credits":4}
,{"_id": "ASLA 102","subid":[],"name":"BEGINNING AMER SIGN LANG II","terms":["Fall","Spring"],"prereqs":[],"subject":"ASLA","credits":4}
,{"_id": "ASLA 105","subid":[],"name":"INTERMED AMERICN SIGN LANG I","terms":["Fall","Spring"],"prereqs":[],"subject":"ASLA","credits":4}
,{"_id": "ASLA 106","subid":[],"name":"INTERMEDIATE ASL II","terms":["Fall","Spring"],"prereqs":["THE 105"],"subject":"ASLA","credits":4}
,{"_id": "ASLA 201","subid":[],"name":"INTRO TO ASL LITERATURE","terms":["Fall"],"prereqs":["ASLA 106"],"subject":"ASLA","credits":4}
,{"_id": "ASLA 202","subid":[],"name":"HIS&AMP;CULT OF AMER DEAF CMMNTY","terms":["Fall"],"prereqs":["THE 105"],"subject":"ASLA","credits":4}
,{"_id": "ASLA 203","subid":[],"name":"ADVANCED ASL","terms":["Fall"],"prereqs":["THE 106"],"subject":"ASLA","credits":4}
,{"_id": "ASLA 204","subid":[],"name":"THEORY&AMP;PRAC SIGN LANG INTERP","terms":["Fall"],"prereqs":["THE 106"],"subject":"ASLA","credits":4}
,{"_id": "ASLA 208","subid":["BCSC 259","LING 208","PSYC 259"],"name":"LANGUAGE DEVELOPMENT","terms":["Fall"],"prereqs":["BCSC 152","LING 110"],"subject":"ASLA","credits":4}
,{"_id": "ASLA 260","subid":["BCSC 152","LING 217","PSYC 152"],"name":"LANGUAGE &AMP; PSYCHOLINGUISTICS","terms":["Fall"],"prereqs":["BCSC 110","BCSC 111"],"subject":"ASLA","credits":4}
,{"_id": "ASLA 280","subid":[],"name":"DEAF-RELATED CAREERS","terms":["Fall"],"prereqs":["SPAN 106","SPAN 113","SPAN 201","SPAN 202"],"subject":"ASLA","credits":4}
,{"_id": "ASLA 394","subid":[],"name":"INTERNSHIP","terms":["Fall"],"prereqs":[],"subject":"ASLA","credits":4}
,{"_id": "ASLA 113","subid":[],"name":"FRN SIGN LANG &AMP; DEAF CULTURE","terms":["Summer"],"prereqs":["THE 110"],"subject":"ASLA","credits":4}
,{"_id": "ASLA 110","subid":[],"name":"COMPAR STUDY OF FRENCH SIGN LANG","terms":["Spring"],"prereqs":[],"subject":"ASLA","credits":4}
,{"_id": "ASLA 200","subid":["BCSC 264","BCSC 564","LING 230","LING 430"],"name":"SIGN LANGUAGE STRUCTURE","terms":["Spring"],"prereqs":["THE 106"],"subject":"ASLA","credits":4}
,{"_id": "ASLA 205","subid":[],"name":"ART OF TRANSLATION","terms":["Spring"],"prereqs":["SPAN 106","SPAN 113","SPAN 201","SPAN 202"],"subject":"ASLA","credits":4}
,{"_id": "ASLA 209","subid":[],"name":"TEACHING ASL AS A 2ND LANG","terms":["Spring"],"prereqs":["ASLA 106"],"subject":"ASLA","credits":4}
,{"_id": "ASLA 250","subid":[],"name":"SOCIOLINGUISTICS OF DEAF COMNTY","terms":["Spring"],"prereqs":["ASLA 106"],"subject":"ASLA","credits":4}
,{"_id": "ASTR 102","subid":[],"name":"RELATIVITY, BLACK HOLES &AMP; THE BIG BANG","terms":["Fall"],"prereqs":[],"subject":"ASTR","credits":4}
,{"_id": "ASTR 111","subid":[],"name":"THE SOLAR SYSTEM &AMP; ITS ORIGIN","terms":["Fall"],"prereqs":["ASTR 111","SPAN 161","SPAN 165","SPAN 171","SPAN 174","SPAN 141","SPAN 143"],"subject":"ASTR","credits":4}
,{"_id": "ASTR 232W","subid":[],"name":"THE MILKY WAY GALAXY","terms":["Fall"],"prereqs":["PHYS 121","PHYS 123","PHYS 141","PHYS 143","MTH 161","MTH 165","MTH 171","MTH 174","ASTR 111","ASTR 142"],"subject":"ASTR","credits":4}
,{"_id": "ASTR 393W","subid":[],"name":"SENIOR THESIS","terms":["Fall","Spring"],"prereqs":[],"subject":"ASTR","credits":4}
,{"_id": "ASTR 395","subid":[],"name":"INDEPENDENT RESEARCH","terms":["Fall"],"prereqs":[],"subject":"ASTR","credits":4}
,{"_id": "ASTR 461","subid":[],"name":"ASTROPHYSICS I","terms":["Fall"],"prereqs":[],"subject":"ASTR","credits":4}
,{"_id": "ASTR 554","subid":[],"name":"COSMOLOGY","terms":["Fall"],"prereqs":[],"subject":"ASTR","credits":4}
,{"_id": "ASTR 595","subid":[],"name":"PHD RESEARCH IN ASTROPHYSICS","terms":["Fall","Spring"],"prereqs":[],"subject":"ASTR","credits":12}
,{"_id": "ASTR 995","subid":[],"name":"CONT OF DOCTORAL ENROLLMENT","terms":["Fall","Spring"],"prereqs":[],"subject":"ASTR","credits":0}
,{"_id": "ASTR 999","subid":[],"name":"DOCTORAL DISSERTATION","terms":["Fall","Spring"],"prereqs":[],"subject":"ASTR","credits":0}
,{"_id": "ASTR 104","subid":[],"name":"SOLAR SYSTEM","terms":["Spring"],"prereqs":[],"subject":"ASTR","credits":4}
,{"_id": "ASTR 142","subid":[],"name":"ELEMENTARY ASTROPHYSICS (HONORS)","terms":["Spring"],"prereqs":["THE 200","SPAN 141","SPAN 143","SPAN 121","SPAN 123","SPAN 161","SPAN 165","SPAN 171","SPAN 174","SPAN 111"],"subject":"ASTR","credits":4}
,{"_id": "ASTR 243","subid":[],"name":"ASTROPHYSICAL FLUID DYNAMICS","terms":["Spring"],"prereqs":["SPAN 237","THE 142","THE 111"],"subject":"ASTR","credits":4}
,{"_id": "ASTR 244W","subid":["ASTR 444"],"name":"OBSERVATIONAL ASTRONOMY","terms":["Spring"],"prereqs":[],"subject":"ASTR","credits":4}
,{"_id": "ASTR 391","subid":[],"name":"INDEPENDENT STUDY","terms":["Spring"],"prereqs":[],"subject":"ASTR","credits":4}
,{"_id": "ASTR 393","subid":[],"name":"SENIOR PROJECT","terms":["Spring"],"prereqs":[],"subject":"ASTR","credits":4}
,{"_id": "ASTR 453","subid":[],"name":"STELLAR STRUCTURE AND ATMOSPHERES","terms":["Spring"],"prereqs":[],"subject":"ASTR","credits":4}
,{"_id": "ASTR 551","subid":[],"name":"THE INTERSTELLAR MEDIUM","terms":["Spring"],"prereqs":[],"subject":"ASTR","credits":4}
,{"_id": "ASTR 595A","subid":[],"name":"PHD RESEARCH IN ABSENTIA","terms":["Spring","Spring"],"prereqs":[],"subject":"ASTR","credits":12}
,{"_id": "ASTR 999A","subid":[],"name":"DOCT DISSERTATN IN ABSENTIA","terms":["Spring"],"prereqs":[],"subject":"ASTR","credits":0}
,{"_id": "ATHS 163","subid":["AHST 148","RELC 173"],"name":"INTRODUCTION TO ART &AMP; ARCHITECTURE OF SOUTH ASIA","terms":["Fall"],"prereqs":[],"subject":"ATHS","credits":4}
,{"_id": "ATHS 223","subid":[],"name":"AZTECS AND THEIR ANCESTORS","terms":["Fall"],"prereqs":[],"subject":"ATHS","credits":4}
,{"_id": "ATHS 259W","subid":["RELC 259W"],"name":"PUBLIC AND COMMUNITY-ENGAGED ARCHAEOLOGY","terms":["Fall"],"prereqs":[],"subject":"ATHS","credits":4}
,{"_id": "ATHS 102","subid":["RELC 186"],"name":"RITUAL AND RELIGION IN ARCHAEOLOGICAL PERSPECTIVE","terms":["Spring"],"prereqs":[],"subject":"ATHS","credits":4}
,{"_id": "ATHS 155","subid":["AHST 127"],"name":"ART AND ARCHITECTURE OF ANCIENT EGYPT","terms":["Spring"],"prereqs":[],"subject":"ATHS","credits":4}
,{"_id": "ATHS 210","subid":["AHST 140","CLST 134","HIST 117"],"name":"ARCHAEOLOGICAL THOUGHT","terms":["Spring"],"prereqs":[],"subject":"ATHS","credits":4}
,{"_id": "ATHS 212","subid":["AHST 232","ANTH 296","HIST 220"],"name":"ART HISTORY AND ETHNOARCHAEOLOGY OF WEST AFRICA","terms":["Spring"],"prereqs":[],"subject":"ATHS","credits":4}
,{"_id": "ATHS 233A","subid":["AHST 286A","SUST 233A"],"name":"CLIMATE CHANGE AND THE AFRICAN CULTURAL HERITAGE","terms":["Spring"],"prereqs":[],"subject":"ATHS","credits":4}
,{"_id": "ATHS 240","subid":["HIST 280","HIST 280W","HIST 497"],"name":"HISTORICAL ARCHAEOLOGY","terms":["Spring"],"prereqs":[],"subject":"ATHS","credits":4}
,{"_id": "ATHS 245","subid":["HIST 285","HIST 285W","HIST 485"],"name":"DIGITAL HISTORY: BUILDING A VIRTUAL ST. GEORGE'S","terms":["Spring"],"prereqs":[],"subject":"ATHS","credits":4}
,{"_id": "ATHS 391","subid":[],"name":"INDEPENDENT STUDY","terms":["Spring"],"prereqs":[],"subject":"ATHS","credits":4}
,{"_id": "ATHS 393","subid":[],"name":"SENIOR THESIS","terms":["Spring"],"prereqs":[],"subject":"ATHS","credits":4}
,{"_id": "ATHS 395","subid":[],"name":"INDEPENDENT RESEARCH","terms":["Spring"],"prereqs":[],"subject":"ATHS","credits":4}
,{"_id": "BCSC 110","subid":["CVSC 110","PSYC 110"],"name":"NEURAL FOUNDATIONS OF BEHAVIOR","terms":["Fall","Summer","Spring"],"prereqs":[],"subject":"BCSC","credits":4}
,{"_id": "BCSC 111","subid":["PSYC 111"],"name":"FOUNDATIONS OF COGNITIVE SCIENCE","terms":["Fall","Summer","Spring"],"prereqs":[],"subject":"BCSC","credits":4}
,{"_id": "BCSC 151","subid":["CVSC 151","PSYC 151"],"name":"PERCEPTION &AMP; ACTION","terms":["Fall"],"prereqs":["BCSC 110","BCSC 111"],"subject":"BCSC","credits":4}
,{"_id": "BCSC 152","subid":["ASLA 260","LING 217","PSYC 152"],"name":"LANGUAGE &AMP; PSYCHOLINGUISTICS","terms":["Fall"],"prereqs":["BCSC 110","BCSC 111"],"subject":"BCSC","credits":4}
,{"_id": "BCSC 163","subid":["WRTG 253"],"name":"COGNITION &AMP; WRITING","terms":["Fall"],"prereqs":[],"subject":"BCSC","credits":4}
,{"_id": "BCSC 170","subid":["PSYC 170"],"name":"CHILD DEVELOPMENT","terms":["Fall"],"prereqs":[],"subject":"BCSC","credits":4}
,{"_id": "BCSC 183","subid":["PSYC 183"],"name":"ANIMAL MINDS","terms":["Fall"],"prereqs":[],"subject":"BCSC","credits":4}
,{"_id": "BCSC 204","subid":[],"name":"LAB IN COGNITIVE NEUROSCIENCE","terms":["Fall","Spring"],"prereqs":["STAT 212","BCSC 153"],"subject":"BCSC","credits":4}
,{"_id": "BCSC 205","subid":["PSYC 205"],"name":"LAB IN DEVELOPMENT &AMP; LEARNING","terms":["Fall"],"prereqs":["STAT 212","STAT 172","THE 151","THE 152","THE 153"],"subject":"BCSC","credits":4}
,{"_id": "BCSC 215","subid":[],"name":"APPLIED PROGRAMMING IN MATLAB","terms":["Fall"],"prereqs":["BCSC 111"],"subject":"BCSC","credits":4}
,{"_id": "BCSC 232","subid":["CSC 242","DSCC 242"],"name":"INTRODUCTION TO ARTIFICIAL INTELLIGENCE","terms":["Fall","Spring"],"prereqs":["CSC 172","CSC 150","CSC 173"],"subject":"BCSC","credits":4}
,{"_id": "BCSC 235","subid":["BCSC 435","CSC 247","CSC 447","LING 247","LING 447","TCS 447"],"name":"NATURAL LANGUAGE PROCESSING","terms":["Fall","Spring"],"prereqs":["CSC 447","CSC 242"],"subject":"BCSC","credits":4}
,{"_id": "BCSC 240","subid":["NSCI 201"],"name":"BASIC NEUROBIOLOGY","terms":["Fall"],"prereqs":["NSCI 201","BIOL 110","BIOL 112"],"subject":"BCSC","credits":4}
,{"_id": "BCSC 241","subid":["BCSC 541","CVSC 241","NSC 541","NSCI 241"],"name":"NEURONS, CIRCUITS, &AMP; SYSTEMS","terms":["Fall"],"prereqs":["BCSC 240","NSCI 201"],"subject":"BCSC","credits":4}
,{"_id": "BCSC 243","subid":["BCSC 543","NSCI 243"],"name":"NEUROCHEMICAL FOUNDATIONS OF BEHAVIOR","terms":["Fall"],"prereqs":["BCSC 240","NSCI 201","BIOL 250"],"subject":"BCSC","credits":4}
,{"_id": "BCSC 245","subid":["CVSC 245","NSCI 245"],"name":"SENSORY &AMP; MOTOR NEUROSCIENCE","terms":["Fall"],"prereqs":["NSCI 201","BCSC 240"],"subject":"BCSC","credits":4}
,{"_id": "BCSC 259","subid":["ASLA 208","LING 208","PSYC 259"],"name":"LANGUAGE DEVELOPMENT","terms":["Fall"],"prereqs":["BCSC 152","LING 110"],"subject":"BCSC","credits":4}
,{"_id": "BCSC 271","subid":[],"name":"AUTISM AND OTHER INTELLECTUAL AND DEVELOPMENTAL DISABILITIES","terms":["Fall"],"prereqs":["BCSC 110","BCSC 172","BCSC 205"],"subject":"BCSC","credits":4}
,{"_id": "BCSC 280","subid":["BCSC 580","NSCI 280"],"name":"ADVANCED TOPICS IN COGNITIVE NEUROSCIENCE","terms":["Fall"],"prereqs":["STAT 212","STAT 213","BCSC 153","NSCI 201","BCSC 240","CSC 229","NSCI 247","CSC 262","MTH 165"],"subject":"BCSC","credits":4}
,{"_id": "BCSC 310","subid":[],"name":"SENIOR SEMINAR","terms":["Fall","Spring"],"prereqs":[],"subject":"BCSC","credits":2}
,{"_id": "BCSC 390","subid":[],"name":"SUPERVISED TEACHING: BCSC 111","terms":["Fall","Spring"],"prereqs":[],"subject":"BCSC","credits":4}
,{"_id": "BCSC 505","subid":[],"name":"PERCEPTION, ACTION, AND NEURAL FOUNDATIONS","terms":["Fall"],"prereqs":[],"subject":"BCSC","credits":4}
,{"_id": "BCSC 528","subid":["CVSC 528"],"name":"SPECIAL TOPICS IN VISION","terms":["Fall","Spring"],"prereqs":[],"subject":"BCSC","credits":4}
,{"_id": "BCSC 570","subid":["BME 410","CSC 413","CVSC 534","ECE 410","NSCI 415","OPT 410"],"name":"INTRODUCTION TO AUGMENTED AND VIRTUAL REALITY","terms":["Fall"],"prereqs":[],"subject":"BCSC","credits":4}
,{"_id": "BCSC 572","subid":["BME 501","CSC 513","CVSC 572","ECE 501","NSCI 540","OPT 503"],"name":"PRACTICUM IN AUGMENTED AND VIRTUAL REALITY","terms":["Fall"],"prereqs":["ECE 410","BCSC 570","NSCI 415","CSC 413","CVSC 534"],"subject":"BCSC","credits":4}
,{"_id": "BCSC 595","subid":[],"name":"PHD RESEARCH","terms":["Fall","Spring"],"prereqs":[],"subject":"BCSC","credits":12}
,{"_id": "BCSC 598","subid":[],"name":"SUPERVISED TEACHING ASSISTANT","terms":["Fall","Spring"],"prereqs":[],"subject":"BCSC","credits":3}
,{"_id": "BCSC 897","subid":[],"name":"MASTER'S DISSERTATION","terms":["Fall","Fall","Summer"],"prereqs":[],"subject":"BCSC","credits":0}
,{"_id": "BCSC 986V","subid":[],"name":"FULL TIME VISITING STUDENT","terms":["Fall","Summer","Spring"],"prereqs":[],"subject":"BCSC","credits":0}
,{"_id": "BCSC 995","subid":[],"name":"CONT OF DOCTORAL ENROLLMENT","terms":["Fall","Spring"],"prereqs":[],"subject":"BCSC","credits":0}
,{"_id": "BCSC 997","subid":[],"name":"DOCTORAL DISSERTATION","terms":["Fall","Summer","Spring"],"prereqs":[],"subject":"BCSC","credits":0}
,{"_id": "BCSC 999","subid":[],"name":"DOCTORAL DISSERTATION","terms":["Fall","Spring"],"prereqs":[],"subject":"BCSC","credits":0}
,{"_id": "BCSC 172","subid":["PSYC 172"],"name":"DEVELOPMENT OF MIND &AMP; BRAIN","terms":["Summer","Spring"],"prereqs":[],"subject":"BCSC","credits":4}
,{"_id": "BCSC 153","subid":["PSYC 153"],"name":"COGNITION","terms":["Spring"],"prereqs":["THE 111","THE 110"],"subject":"BCSC","credits":4}
,{"_id": "BCSC 203","subid":["NSCI 203"],"name":"LAB IN NEUROBIOLOGY","terms":["Spring"],"prereqs":["NSCI 201","BCSC 240","STAT 212"],"subject":"BCSC","credits":4}
,{"_id": "BCSC 208","subid":["CVSC 208","PSYC 208"],"name":"LAB IN PERCEPTION &AMP; COGNITION","terms":["Spring"],"prereqs":["STAT 212","BCSC 151","BCSC 153"],"subject":"BCSC","credits":4}
,{"_id": "BCSC 221","subid":["BCSC 521","PSYC 221"],"name":"AUDITORY PERCEPTION","terms":["Spring"],"prereqs":["BCSC 110","BCSC 111"],"subject":"BCSC","credits":4}
,{"_id": "BCSC 223","subid":["OPT 248","OPT 448","TEO 448"],"name":"VISION AND THE EYE","terms":["Spring"],"prereqs":[],"subject":"BCSC","credits":4}
,{"_id": "BCSC 236","subid":["BCSC 536","CSC 249","CSC 449","ECE 449","TCS 449"],"name":"MACHINE VISION","terms":["Spring"],"prereqs":["CSC 449","MTH 161","CSC 242","MTH 165"],"subject":"BCSC","credits":4}
,{"_id": "BCSC 244","subid":["NSCI 244"],"name":"NEUROETHOLOGY","terms":["Spring"],"prereqs":["BCSC 240","NSCI 201"],"subject":"BCSC","credits":4}
,{"_id": "BCSC 246","subid":["BCSC 546","NSCI 246","PSYC 246"],"name":"BIOLOGY OF MENTAL DISORDERS","terms":["Spring"],"prereqs":["NSCI 201","BCSC 240"],"subject":"BCSC","credits":4}
,{"_id": "BCSC 249","subid":["NSCI 249"],"name":"DEVELOPMENTAL NEUROBIOLOGY","terms":["Spring"],"prereqs":["NSCI 201","BCSC 240"],"subject":"BCSC","credits":4}
,{"_id": "BCSC 250","subid":["NSCI 250"],"name":"ACQUIRED BRAIN DISORDERS","terms":["Spring"],"prereqs":["NSCI 201","BCSC 240"],"subject":"BCSC","credits":4}
,{"_id": "BCSC 252","subid":["NSCI 252"],"name":"FUNCTIONAL NEUROANATOMY","terms":["Spring"],"prereqs":["BIOL 110"],"subject":"BCSC","credits":4}
,{"_id": "BCSC 257","subid":["BCSC 557","CSC 243","CSC 443","NSCI 257"],"name":"ADVANCED COMPUTATIONAL NEUROSCIENCE","terms":["Spring"],"prereqs":["BCSC 247"],"subject":"BCSC","credits":4}
,{"_id": "BCSC 260","subid":["MUSC 162","TH 260","TH 460"],"name":"MUSIC &AMP; THE MIND","terms":["Spring"],"prereqs":["THE 101","THE 110","THE 111"],"subject":"BCSC","credits":4}
,{"_id": "BCSC 264","subid":["ASLA 200","BCSC 564","LING 230","LING 430"],"name":"SIGN LANGUAGE STRUCTURE","terms":["Spring"],"prereqs":["THE 106"],"subject":"BCSC","credits":4}
,{"_id": "BCSC 266","subid":["BME 216","BME 416","LING 216","LING 416"],"name":"SPEECH ON THE BRAIN","terms":["Spring"],"prereqs":[],"subject":"BCSC","credits":4}
,{"_id": "BCSC 278","subid":[],"name":"SOCIAL NEUROSCIENCE","terms":["Spring"],"prereqs":["PSYC 101","BCSC 110"],"subject":"BCSC","credits":4}
,{"_id": "BCSC 393","subid":[],"name":"BCS HONORS THESIS","terms":["Spring"],"prereqs":[],"subject":"BCSC","credits":4}
,{"_id": "BCSC 504","subid":["CVSC 504"],"name":"SENSORY SYSTEMS","terms":["Spring"],"prereqs":[],"subject":"BCSC","credits":4}
,{"_id": "BCSC 509","subid":[],"name":"ADVANCED METHODS IN BRAIN AND COGNITIVE SCIENCES","terms":["Spring"],"prereqs":[],"subject":"BCSC","credits":4}
,{"_id": "BCSC 571","subid":["BME 413","CSC 414","CVSC 535","ECE 411","NSCI 416","OPT 438"],"name":"SELECTED TOPICS IN AUGMENTED AND VIRTUAL REALITY","terms":["Spring"],"prereqs":["THE 202","ECE 410","NSCI 415","CSC 413","CVSC 534"],"subject":"BCSC","credits":4}
,{"_id": "BCSC 582","subid":[],"name":"GRANT WRITING: BRAIN &AMP; COGNITIVE SCIENCE","terms":["Spring"],"prereqs":[],"subject":"BCSC","credits":3}
,{"_id": "BCSC 594","subid":[],"name":"RESEARCH INTERNSHIP","terms":["Spring"],"prereqs":[],"subject":"BCSC","credits":1}
,{"_id": "BCSC 595A","subid":[],"name":"PHD RESEARCH IN ABSENTIA","terms":["Spring"],"prereqs":[],"subject":"BCSC","credits":12}
,{"_id": "BCSC 599","subid":[],"name":"PROFESSIONAL DEVELOPMENT &AMP; CAREER PLANNING","terms":["Spring"],"prereqs":[],"subject":"BCSC","credits":1}
,{"_id": "BCSC 997A","subid":[],"name":"DOCT DISSERTATN IN ABSENTIA","terms":["Spring"],"prereqs":[],"subject":"BCSC","credits":0}
,{"_id": "BCSC 999A","subid":[],"name":"DOCTORAL DISSERTATION IN ABSENTIA","terms":["Spring"],"prereqs":[],"subject":"BCSC","credits":0}











,{"_id": "BIOL 098","subid":[],"name":"PRINCIPLES OF BIOLOGY I LAB (BIWEEKLY A)","terms":["Fall"],"prereqs":[],"subject":"BIOL","credits":0}
,{"_id": "BIOL 1000","subid":[],"name":"TEACHING ASSISTANTSHIP","terms":["Fall"],"prereqs":[],"subject":"BIOL","credits":1}
,{"_id": "BIOL 101","subid":[],"name":"GENES, GERMS, &AMP; GENOMICS","terms":["Fall"],"prereqs":[],"subject":"BIOL","credits":4}
,{"_id": "BIOL 102","subid":[],"name":"NATURAL HISTORY: OBSERVING NATURE","terms":["Fall"],"prereqs":["THE 003","THE 005","THE 001","BIOL 225"],"subject":"BIOL","credits":4}
,{"_id": "BIOL 104K","subid":[],"name":"ECOSYSTEM CONSERVTN&AMP;HUM SOC","terms":["Fall"],"prereqs":[],"subject":"BIOL","credits":4}
,{"_id": "BIOL 109","subid":[],"name":"DARWIN &AMP; DARWINISM","terms":["Fall"],"prereqs":[],"subject":"BIOL","credits":4}
,{"_id": "BIOL 110L","subid":[],"name":"PRINCIPLES OF BIOLOGY I","terms":["Fall","Summer"],"prereqs":["CHEM 131","BIOL 110","BIOL 112"],"subject":"BIOL","credits":4}
,{"_id": "BIOL 112L","subid":[],"name":"BIO PERSPECTIVES I WITH LAB","terms":["Fall"],"prereqs":["BIOL 112","BIOL 110","CHEM 131","BIOL 113"],"subject":"BIOL","credits":4}
,{"_id": "BIOL 190","subid":[],"name":"GENETICS &AMP; THE HUMAN GENOME","terms":["Fall"],"prereqs":["BIOL 198","BIOL 190","BIOL 110","BIOL 112","BIOL 111","BIOL 113","CHEM 131","CHEM 132"],"subject":"BIOL","credits":4}
,{"_id": "BIOL 198","subid":[],"name":"PRINCIPLES OF GENETICS","terms":["Fall","Summer"],"prereqs":["BIOL 198","BIOL 190","BIOL 110","BIOL 112","CHEM 131","CHEM 132"],"subject":"BIOL","credits":4}
,{"_id": "BIOL 198P","subid":[],"name":"PRINCIPLES OF GENETICS LAB","terms":["Fall"],"prereqs":["BIOL 190","BIOL 198"],"subject":"BIOL","credits":1}
,{"_id": "BIOL 202","subid":["BIOL 402"],"name":"MOLECULAR BIOLOGY","terms":["Fall"],"prereqs":["BIOL 198","BIOL 190","BIOL 250"],"subject":"BIOL","credits":4}
,{"_id": "BIOL 202W","subid":[],"name":"MOLECULAR BIOLOGY WRITING","terms":["Fall"],"prereqs":[],"subject":"BIOL","credits":0}
,{"_id": "BIOL 204","subid":[],"name":"PRIN OF HUMAN PHYSIOLOGY","terms":["Fall","Summer"],"prereqs":["SPAN 110","BIOL 112","BIOL 111","BIOL 113"],"subject":"BIOL","credits":4}
,{"_id": "BIOL 204P","subid":[],"name":"MAMMALIAN PHYSIOLOGY - LAB","terms":["Fall"],"prereqs":[],"subject":"BIOL","credits":1}
,{"_id": "BIOL 204W","subid":[],"name":"MAMMALIAN PHYSIOLOGY WRITING","terms":["Fall"],"prereqs":[],"subject":"BIOL","credits":0}
,{"_id": "BIOL 206","subid":["BIOL 406"],"name":"EUKARYOTIC GENOMES","terms":["Fall"],"prereqs":["BIOL 190","BIOL 198"],"subject":"BIOL","credits":4}
,{"_id": "BIOL 206W","subid":[],"name":"EUKARYOTIC GENOMES-WRITING","terms":["Fall"],"prereqs":["BIOL 206"],"subject":"BIOL","credits":1}
,{"_id": "BIOL 220","subid":["BIOL 420"],"name":"ADVANCED CELL BIOLOGY","terms":["Fall"],"prereqs":["BIOL 220","SPAN 190","BIOL 198","BIOL 210","BIOL 250","BIOL 252"],"subject":"BIOL","credits":4}
,{"_id": "BIOL 220W","subid":[],"name":"ADV CELL BIOLOGY WRITING","terms":["Fall"],"prereqs":[],"subject":"BIOL","credits":0}
,{"_id": "BIOL 222","subid":["BIOL 422"],"name":"BIOLOGY OF AGING","terms":["Fall"],"prereqs":["BIOL 198","BIOL 190","BIOL 202"],"subject":"BIOL","credits":4}
,{"_id": "BIOL 222W","subid":[],"name":"BIO OF AGING WRITING","terms":["Fall"],"prereqs":[],"subject":"BIOL","credits":0}
,{"_id": "BIOL 225","subid":[],"name":"ECOLOGY &AMP; EVOLUTIONARY BIO","terms":["Fall"],"prereqs":["BIOL 263","BIOL 205","BIOL 214","BIOL 259","BIOL 260","BIOL 225"],"subject":"BIOL","credits":4}
,{"_id": "BIOL 225W","subid":[],"name":"ECO. &AMP; EVOL. LAB WRITING","terms":["Fall"],"prereqs":[],"subject":"BIOL","credits":0}
,{"_id": "BIOL 226","subid":["BIOL 426"],"name":"DEVELOPMENTAL BIOLOGY","terms":["Fall"],"prereqs":["BIOL 198","BIOL 190"],"subject":"BIOL","credits":4}
,{"_id": "BIOL 226W","subid":[],"name":"DEVELOPMENTAL BIOLOGY WRITING","terms":["Fall"],"prereqs":[],"subject":"BIOL","credits":0}
,{"_id": "BIOL 228B","subid":[],"name":"IGEM II","terms":["Fall"],"prereqs":[],"subject":"BIOL","credits":4}
,{"_id": "BIOL 228W","subid":[],"name":"IGEM WRITING","terms":["Fall"],"prereqs":[],"subject":"BIOL","credits":0}
,{"_id": "BIOL 257L","subid":["BIOL 457L"],"name":"APPLIED GENOMICS WITH LAB","terms":["Fall"],"prereqs":["BIOL 190","BIOL 198"],"subject":"BIOL","credits":4}
,{"_id": "BIOL 257W","subid":[],"name":"APPLIED GENOMICS - WRITING","terms":["Fall"],"prereqs":[],"subject":"BIOL","credits":0}
,{"_id": "BIOL 259L","subid":["BIOL 459L"],"name":"APPLIED POPULATION BIO W/LAB","terms":["Fall"],"prereqs":["BIOL 111","BIOL 113","BIOL 205","BIOL 263"],"subject":"BIOL","credits":4}
,{"_id": "BIOL 259W","subid":[],"name":"APPLIED POP. BIO. WRITING","terms":["Fall"],"prereqs":[],"subject":"BIOL","credits":0}
,{"_id": "BIOL 260","subid":["BIOL 460"],"name":"ANIMAL BEHAVIOR","terms":["Fall"],"prereqs":[],"subject":"BIOL","credits":4}
,{"_id": "BIOL 260W","subid":[],"name":"ANIMAL BEHAVIOR - WRITING","terms":["Fall"],"prereqs":["BIOL 260"],"subject":"BIOL","credits":0}
,{"_id": "BIOL 262W","subid":[],"name":"GENETIC RESEARCH B","terms":["Fall"],"prereqs":[],"subject":"BIOL","credits":4}
,{"_id": "BIOL 272W","subid":["WRTG 272"],"name":"COMMUNICATING YOUR PROFESSIONAL IDENTITY - BIOLOGY AND PUBLIC HEALTH","terms":["Fall","Spring"],"prereqs":[],"subject":"BIOL","credits":2}
,{"_id": "BIOL 390A","subid":[],"name":"SUPERVISED TEACHING-BIOL 198","terms":["Fall"],"prereqs":[],"subject":"BIOL","credits":2}
,{"_id": "BIOL 394","subid":[],"name":"INTERNSHIP","terms":["Fall"],"prereqs":[],"subject":"BIOL","credits":4}
,{"_id": "BIOL 480","subid":[],"name":"GRADUATE LAB ROTATION","terms":["Fall","Spring"],"prereqs":[],"subject":"BIOL","credits":4}
,{"_id": "BIOL 516","subid":[],"name":"CELL/DEV/MOL BIOLOGY SEM","terms":["Fall"],"prereqs":[],"subject":"BIOL","credits":1}
,{"_id": "BIOL 580","subid":[],"name":"JOURNAL CLUB IN EVOL., ECOL., GENETICS &AMP; GENOMICS","terms":["Fall","Spring"],"prereqs":[],"subject":"BIOL","credits":1}
,{"_id": "BIOL 581","subid":[],"name":"TOPICS IN CELL,DEV&AMP;MOL BIOL","terms":["Fall"],"prereqs":[],"subject":"BIOL","credits":2}
,{"_id": "BIOL 584","subid":[],"name":"SEMINAR IN EVOLUTION, ECOLOGY, GENETICS &AMP; GENOMICS","terms":["Fall","Spring"],"prereqs":[],"subject":"BIOL","credits":1}
,{"_id": "BIOL 895","subid":[],"name":"CONT OF MASTERS ENROLLMENT","terms":["Fall"],"prereqs":[],"subject":"BIOL","credits":0}
,{"_id": "BIOL 897","subid":[],"name":"MASTERS DISSERTATION","terms":["Fall","Spring"],"prereqs":[],"subject":"BIOL","credits":0}
,{"_id": "BIOL 899","subid":[],"name":"MASTER'S DISSERTATION","terms":["Fall","Spring"],"prereqs":[],"subject":"BIOL","credits":0}
,{"_id": "BIOL 986V","subid":[],"name":"FULL TIME VISITING STUDENT","terms":["Fall"],"prereqs":[],"subject":"BIOL","credits":0}
,{"_id": "BIOL 995","subid":[],"name":"CONT OF DOCTORAL ENROLLMENT","terms":["Fall","Spring"],"prereqs":[],"subject":"BIOL","credits":0}
,{"_id": "BIOL 997","subid":[],"name":"DOCTORAL DISSERTATION","terms":["Fall","Spring"],"prereqs":[],"subject":"BIOL","credits":0}
,{"_id": "BIOL 999","subid":[],"name":"DOCTORAL DISSERTATION","terms":["Fall"],"prereqs":[],"subject":"BIOL","credits":0}
,{"_id": "BIOL 099","subid":[],"name":"PRINCIPLES OF BIOLOGY II LAB (BIWEEKLY A)","terms":["Spring"],"prereqs":[],"subject":"BIOL","credits":0}
,{"_id": "BIOL 110","subid":[],"name":"PRINCIPLES OF BIOLOGY I","terms":["Spring"],"prereqs":["CHEM 131"],"subject":"BIOL","credits":4}
,{"_id": "BIOL 113L","subid":[],"name":"PERSPECT IN BIO II W/LAB","terms":["Spring"],"prereqs":[],"subject":"BIOL","credits":4}
,{"_id": "BIOL 205","subid":["BIOL 405"],"name":"EVOLUTION","terms":["Spring"],"prereqs":["THE 190","BIOL 198"],"subject":"BIOL","credits":4}
,{"_id": "BIOL 205W","subid":[],"name":"EVOLUTIONARY BIOLOGY - WRITING","terms":["Spring"],"prereqs":["BIOL 205"],"subject":"BIOL","credits":1}
,{"_id": "BIOL 210","subid":[],"name":"CELL BIOLOGY","terms":["Spring"],"prereqs":["BIOL 110","BIOL 112","BIOL 111","BIOL 113","BIOL 198","BIOL 190","BIOL 250"],"subject":"BIOL","credits":4}
,{"_id": "BIOL 210W","subid":[],"name":"CELL BIOLOGY WRITING","terms":["Spring"],"prereqs":[],"subject":"BIOL","credits":0}
,{"_id": "BIOL 217L","subid":[],"name":"PRIN OF HUMAN ANATOMY W/LAB","terms":["Spring"],"prereqs":[],"subject":"BIOL","credits":4}
,{"_id": "BIOL 217W","subid":[],"name":"HUMAN ANATOMY WRITING","terms":["Spring"],"prereqs":[],"subject":"BIOL","credits":0}
,{"_id": "BIOL 219L","subid":["BIOL 419L"],"name":"GENOMICS OF QUANT TRAITS W/LAB","terms":["Spring"],"prereqs":["THE 190","THE 198","BIOL 214"],"subject":"BIOL","credits":4}
,{"_id": "BIOL 228A","subid":[],"name":"IGEM I","terms":["Spring"],"prereqs":[],"subject":"BIOL","credits":4}
,{"_id": "BIOL 243","subid":["BIOL 443","IND 443"],"name":"EUKARYOTIC GENE REGULATION","terms":["Spring"],"prereqs":["BIOL 198","BIOL 250"],"subject":"BIOL","credits":4}
,{"_id": "BIOL 243W","subid":[],"name":"EUKARYOTIC GENE REGULATION-WRITING","terms":["Spring"],"prereqs":[],"subject":"BIOL","credits":0}
,{"_id": "BIOL 250","subid":[],"name":"BIOCHEMISTRY","terms":["Spring"],"prereqs":["BIOL 250","BIOL 110","BIOL 112","CHEM 203","BIOL 190","BIOL 198","CHEM 204"],"subject":"BIOL","credits":4}
,{"_id": "BIOL 250P","subid":[],"name":"BIOCHEMISTRY LAB","terms":["Spring"],"prereqs":["BIOL 250"],"subject":"BIOL","credits":1}
,{"_id": "BIOL 250PW","subid":[],"name":"BIOCHEMISTRY LAB WRITING","terms":["Spring"],"prereqs":[],"subject":"BIOL","credits":0}
,{"_id": "BIOL 252","subid":[],"name":"PRINCIPLES OF BIOCHEMISTRY","terms":["Spring"],"prereqs":["BIOL 250","BIOL 110","BIOL 112","BIOL 190","BIOL 198","CHEM 203","CHEM 204","CHEM 172"],"subject":"BIOL","credits":4}
,{"_id": "BIOL 253L","subid":["BIOL 453L"],"name":"COMPUTATIONAL BIO WITH LAB - LECTURE","terms":["Spring"],"prereqs":[],"subject":"BIOL","credits":4}
,{"_id": "BIOL 253W","subid":[],"name":"COMPUTATIONAL BIOLOGY UPPER-LEVEL WRITING","terms":["Spring"],"prereqs":[],"subject":"BIOL","credits":0}
,{"_id": "BIOL 261W","subid":[],"name":"GENETIC RESEARCH A","terms":["Spring"],"prereqs":[],"subject":"BIOL","credits":4}
,{"_id": "BIOL 263","subid":["BIOL 463"],"name":"ECOLOGY","terms":["Spring"],"prereqs":["BIOL 110","BIOL 112","BIOL 111","BIOL 113","SPAN 142","SPAN 161"],"subject":"BIOL","credits":4}
,{"_id": "BIOL 263W","subid":[],"name":"ECOLOGY WRITING","terms":["Spring"],"prereqs":["BIOL 263"],"subject":"BIOL","credits":0}
,{"_id": "BIOL 268","subid":["BIOL 468"],"name":"LAB IN MOLECULAR, CELL&AMP;DEV BIO","terms":["Spring"],"prereqs":["BIOL 198","BIOL 190","BIOL 250"],"subject":"BIOL","credits":4}
,{"_id": "BIOL 268W","subid":[],"name":"LAB IN MOLECULAR GENETICS","terms":["Spring"],"prereqs":[],"subject":"BIOL","credits":0}
,{"_id": "BIOL 278","subid":["BIOL 478"],"name":"BIOCHEM MECH OF CELL PRO","terms":["Spring"],"prereqs":["THE 278","BIOL 190","BIOL 198","BIOL 250","CHEM 204"],"subject":"BIOL","credits":4}
,{"_id": "BIOL 299","subid":[],"name":"ADVANCED TOPICS IN FIELD BIOLOGY","terms":["Spring"],"prereqs":[],"subject":"BIOL","credits":1}
,{"_id": "BIOL 476","subid":[],"name":"ADVANCED ECOLOGY &AMP; EVOLUTION BIOLOGY F","terms":["Spring"],"prereqs":[],"subject":"BIOL","credits":2}
,{"_id": "BIOL 517","subid":[],"name":"GRADUATE RESEARCH SEMINAR","terms":["Spring"],"prereqs":[],"subject":"BIOL","credits":1}
,{"_id": "BIOL 595A","subid":[],"name":"PHD RESEARCH IN ABSENTIA","terms":["Spring"],"prereqs":[],"subject":"BIOL","credits":12}
,{"_id": "BIOL 595B","subid":[],"name":"BIOLOGY RESEARCH IN ABSENTIA ABROAD","terms":["Spring"],"prereqs":[],"subject":"BIOL","credits":12}
,{"_id": "BIOL 997A","subid":[],"name":"DOCT DISSERTATN IN ABSENTIA","terms":["Spring"],"prereqs":[],"subject":"BIOL","credits":0}
,{"_id": "BIOL 999A","subid":[],"name":"DOCT DISSERTATN IN ABSENTIA","terms":["Spring"],"prereqs":[],"subject":"BIOL","credits":0}
,{"_id": "BME 101","subid":["EAS 101"],"name":"INTRO TO BIOMEDICAL ENGR","terms":["Fall"],"prereqs":[],"subject":"BME","credits":4}
,{"_id": "BME 201","subid":[],"name":"FUNDAMENTALS OF BIOMECHANICS","terms":["Fall"],"prereqs":["THE 161","THE 162","BME 101","BME 121"],"subject":"BME","credits":4}
,{"_id": "BME 201P","subid":[],"name":"MATLAB FOR BME","terms":["Fall"],"prereqs":[],"subject":"BME","credits":1}
,{"_id": "BME 211","subid":["BME 411","TEB 211","TEB 411"],"name":"CELLULAR&AMP;MOLECULAR BIO FOUND","terms":["Fall"],"prereqs":["BIOL 110"],"subject":"BME","credits":4}
,{"_id": "BME 228","subid":["BME 428","TEB 428"],"name":"PHYSIOLOGICAL CONTROL SYSTMS","terms":["Fall"],"prereqs":["MTH 164","MTH 165","BME 230","ECE 241"],"subject":"BME","credits":4}
,{"_id": "BME 229","subid":["BME 429"],"name":"APPLIED NANOSCIENCE AND NANO-ENGINEERING","terms":["Fall"],"prereqs":["CHEM 131","CHEM 132","PHYS 121","SPAN 110","PHYS 122"],"subject":"BME","credits":4}
,{"_id": "BME 230","subid":[],"name":"BME SIGNALS, SYS&AMP;IMAGING","terms":["Fall"],"prereqs":["BME 210","MTH 165"],"subject":"BME","credits":4}
,{"_id": "BME 253","subid":["BME 453","ECE 251","ECE 453","PHYS 257","PHYS 467","TEB 453"],"name":"ULTRASOUND IMAGING","terms":["Fall"],"prereqs":["BME 230","ECE 241"],"subject":"BME","credits":4}
,{"_id": "BME 255","subid":["BME 455"],"name":"TRANSLATIONAL BIOMEDICAL OPT","terms":["Fall"],"prereqs":[],"subject":"BME","credits":4}
,{"_id": "BME 260","subid":["BME 460","TEB 260","TEB 460"],"name":"QUANTITATIVE PHYSIOLOGY","terms":["Fall"],"prereqs":["ECE 113","BME 210"],"subject":"BME","credits":4}
,{"_id": "BME 265","subid":["BME 465","PHP 265","PHP 465"],"name":"INTROCELL MECH &AMP; MECHBIO","terms":["Fall"],"prereqs":["BME 211","SPAN 257","SPAN 411","BME 260"],"subject":"BME","credits":4}
,{"_id": "BME 295","subid":[],"name":"BME DESIGN SEMINAR","terms":["Fall"],"prereqs":[],"subject":"BME","credits":2}
,{"_id": "BME 390A","subid":[],"name":"SUPERVISED TEACHING - BME 101","terms":["Fall"],"prereqs":[],"subject":"BME","credits":2}
,{"_id": "BME 394","subid":[],"name":"INTERNSHIP","terms":["Fall"],"prereqs":[],"subject":"BME","credits":4}
,{"_id": "BME 402","subid":[],"name":"RESEARCH METHODS","terms":["Fall"],"prereqs":[],"subject":"BME","credits":2}
,{"_id": "BME 410","subid":["BCSC 570","CSC 413","CVSC 534","ECE 410","NSCI 415","OPT 410"],"name":"INTRODUCTION TO AUGMENTED AND VIRTUAL REALITY","terms":["Fall"],"prereqs":[],"subject":"BME","credits":4}
,{"_id": "BME 431","subid":[],"name":"FDA &AMP; INTELLECTUAL PROPERTY","terms":["Fall"],"prereqs":[],"subject":"BME","credits":2}
,{"_id": "BME 486","subid":["ME 254","ME 441","TME 441"],"name":"FINITE ELEMENTS METHODS","terms":["Fall"],"prereqs":[],"subject":"BME","credits":4}
,{"_id": "BME 492","subid":[],"name":"NEUROENHANCEMENT&AMP;REHAB ENG","terms":["Fall"],"prereqs":["BME 210","BME 201","BME 230","BME 218"],"subject":"BME","credits":4}
,{"_id": "BME 495","subid":[],"name":"MASTER'S RESEARCH IN BME","terms":["Fall","Spring"],"prereqs":[],"subject":"BME","credits":12}
,{"_id": "BME 496","subid":[],"name":"CURRENT RESEARCH SEMINARS","terms":["Fall","Spring"],"prereqs":[],"subject":"BME","credits":0}
,{"_id": "BME 501","subid":["BCSC 572","CSC 513","CVSC 572","ECE 501","NSCI 540","OPT 503"],"name":"PRACTICUM IN AUGMENTED AND VIRTUAL REALITY","terms":["Fall"],"prereqs":["ECE 410","BCSC 570","NSCI 415","CSC 413","CVSC 534"],"subject":"BME","credits":4}
,{"_id": "BME 535","subid":[],"name":"MED DEVICE DESIGN","terms":["Fall"],"prereqs":[],"subject":"BME","credits":4}
,{"_id": "BME 593","subid":[],"name":"LABORATORY ROTATIONS IN BME","terms":["Fall","Spring"],"prereqs":[],"subject":"BME","credits":2}
,{"_id": "BME 594","subid":[],"name":"INTERNSHIP RESEARCH","terms":["Fall","Summer"],"prereqs":[],"subject":"BME","credits":1}
,{"_id": "BME 595","subid":[],"name":"PHD RESEARCH","terms":["Fall","Spring"],"prereqs":[],"subject":"BME","credits":12}
,{"_id": "BME 595A","subid":[],"name":"PHD RESEARCH IN ABSENTIA","terms":["Fall","Spring","Spring"],"prereqs":[],"subject":"BME","credits":12}
,{"_id": "BME 895","subid":[],"name":"CONT OF MASTER'S ENROLLMENT","terms":["Fall","Spring"],"prereqs":[],"subject":"BME","credits":0}
,{"_id": "BME 897","subid":[],"name":"MASTER'S DISSERTATION","terms":["Fall","Summer","Spring"],"prereqs":[],"subject":"BME","credits":0}
,{"_id": "BME 899","subid":[],"name":"MASTER'S DISSERTATION","terms":["Fall","Spring"],"prereqs":[],"subject":"BME","credits":0}
,{"_id": "BME 995","subid":[],"name":"CONT OF DOCTORAL ENROLLMENT","terms":["Fall","Spring"],"prereqs":[],"subject":"BME","credits":0}
,{"_id": "BME 997","subid":[],"name":"DOCTORAL DISSERTATION","terms":["Fall","Spring"],"prereqs":[],"subject":"BME","credits":0}
,{"_id": "BME 999","subid":[],"name":"DOCTORAL DISSERTATION","terms":["Fall","Spring"],"prereqs":[],"subject":"BME","credits":0}
,{"_id": "BME 498","subid":[],"name":"CMTI SUMMER ROTATION","terms":["Summer"],"prereqs":[],"subject":"BME","credits":0}
,{"_id": "BME 099","subid":[],"name":"BIOMATL'S &AMP; COMPUTATION LAB","terms":["Spring"],"prereqs":[],"subject":"BME","credits":0}
,{"_id": "BME 210","subid":[],"name":"BIOSYSTEMS &AMP; CIRCUITS","terms":["Spring"],"prereqs":["PHYS 122","MTH 162","BME 201","MTH 165"],"subject":"BME","credits":4}
,{"_id": "BME 212","subid":["BME 412","ME 212","ME 412","MSC 486"],"name":"VISCO IN BIO TISSUES","terms":["Spring"],"prereqs":["ME 225","CHE 243","ME 226","BME 201"],"subject":"BME","credits":4}
,{"_id": "BME 216","subid":["BCSC 266","BME 416","LING 216","LING 416"],"name":"SPEECH ON THE BRAIN","terms":["Spring"],"prereqs":[],"subject":"BME","credits":4}
,{"_id": "BME 221","subid":[],"name":"BIOMEDICAL COMPUTATION &AMP; STATISTICS","terms":["Spring"],"prereqs":["BME 201"],"subject":"BME","credits":4}
,{"_id": "BME 243","subid":[],"name":"FINITE ELEMENT ANALYSIS &AMP; PRINCIPLES OF SCIENTIFIC ANIMATION FOR BIOENGINEERS","terms":["Spring"],"prereqs":[],"subject":"BME","credits":2}
,{"_id": "BME 245","subid":[],"name":"BIOMATERIALS","terms":["Spring"],"prereqs":["BME 099","BME 221","BME 245","CHEM 131","CHEM 132","PHYS 121","PHYS 122","MTH 161","MTH 162","BIOL 110"],"subject":"BME","credits":4}
,{"_id": "BME 258","subid":["BME 459"],"name":"HUMAN ANATOMY","terms":["Spring"],"prereqs":["BIOL 110"],"subject":"BME","credits":4}
,{"_id": "BME 262","subid":["BME 462","CHE 262","CHE 462","MSC 462"],"name":"CELL &AMP; TISSUE ENGINEERING","terms":["Spring"],"prereqs":["BME 260","CHE 225","ME 123","CHE 244","BME 211","BME 411","BIOL 202","BIOL 210"],"subject":"BME","credits":4}
,{"_id": "BME 270","subid":[],"name":"BIOMEDICAL MICROSCOPY","terms":["Spring"],"prereqs":["PHYS 122"],"subject":"BME","credits":4}
,{"_id": "BME 272","subid":["BME 472","OPT 272","OPT 472"],"name":"ADVANCED BIOMEDICAL MICROSCOPY","terms":["Spring"],"prereqs":["OPT 261","BME 270"],"subject":"BME","credits":4}
,{"_id": "BME 296","subid":[],"name":"BME DESIGN PROJECT","terms":["Spring"],"prereqs":["BME 295","BME 260"],"subject":"BME","credits":4}
,{"_id": "BME 404","subid":["ME 404"],"name":"COMPUTATIONAL METHODS","terms":["Spring"],"prereqs":[],"subject":"BME","credits":4}
,{"_id": "BME 413","subid":["BCSC 571","CSC 414","CVSC 535","ECE 411","NSCI 416","OPT 438"],"name":"SELECTED TOPICS IN AUGMENTED AND VIRTUAL REALITY","terms":["Spring"],"prereqs":["THE 202","ECE 410","NSCI 415","CSC 413","CVSC 534"],"subject":"BME","credits":4}
,{"_id": "BME 415","subid":["NSC 415"],"name":"NEUROSCIENCE OF NEUROPROSTHETICS","terms":["Spring"],"prereqs":[],"subject":"BME","credits":4}
,{"_id": "BME 432","subid":[],"name":"FDA &AMP; IP COMMERCIALIZATION","terms":["Spring"],"prereqs":[],"subject":"BME","credits":2}
,{"_id": "BME 494","subid":[],"name":"MASTERS INTERNSHIP","terms":["Spring"],"prereqs":[],"subject":"BME","credits":1}
,{"_id": "BME 589","subid":[],"name":"WRITING PROPOSALS IN BME","terms":["Spring"],"prereqs":[],"subject":"BME","credits":2}
,{"_id": "BME 897A","subid":[],"name":"MASTERS IN-ABSENTIA","terms":["Spring"],"prereqs":[],"subject":"BME","credits":0}
,{"_id": "BME 899B","subid":[],"name":"MASTER'S DISSERTATION IN ABSENTIA","terms":["Spring"],"prereqs":[],"subject":"BME","credits":0}
,{"_id": "BME 999A","subid":[],"name":"DOCTORAL DISSERTATION IN ABSENTIA","terms":["Spring"],"prereqs":[],"subject":"BME","credits":0}
,{"_id": "BUS 221","subid":[],"name":"OPERATIONS &AMP; STRATEGY","terms":["Fall","Spring"],"prereqs":[],"subject":"BUS","credits":4}
,{"_id": "BUS 201","subid":[],"name":"IMPACTFUL PRESENTATIONS","terms":["Spring"],"prereqs":[],"subject":"BUS","credits":4}
,{"_id": "BUS 217","subid":[],"name":"PRINCIPLES OF BUSINESS LEADERSHIP","terms":["Spring"],"prereqs":[],"subject":"BUS","credits":4}
,{"_id": "BUS 389","subid":[],"name":"BUSINESS RESEARCH","terms":["Spring"],"prereqs":[],"subject":"BUS","credits":4}
,{"_id": "CASC 015","subid":[],"name":"EXPLORATIONS IN US CULTURE","terms":["Fall"],"prereqs":[],"subject":"CASC","credits":0}
,{"_id": "CASC 030","subid":[],"name":"DEVELOPING INTEGRITY IN ACADEMIC LIFE","terms":["Fall"],"prereqs":[],"subject":"CASC","credits":0}
,{"_id": "CASC 104","subid":[],"name":"DESIGNING YOUR LIFE","terms":["Fall"],"prereqs":[],"subject":"CASC","credits":1}
,{"_id": "CASC 120","subid":[],"name":"EXPLORING INTERCULTURAL COMPETENCE","terms":["Fall"],"prereqs":[],"subject":"CASC","credits":2}
,{"_id": "CASC 142","subid":[],"name":"STRATEGIES FOR ACADEMIC SUCCESS","terms":["Fall","Spring"],"prereqs":[],"subject":"CASC","credits":1}
,{"_id": "CASC 145","subid":[],"name":"NAVIGATING THE ACADEMY","terms":["Fall","Spring"],"prereqs":[],"subject":"CASC","credits":1}
,{"_id": "CASC 148","subid":[],"name":"EXPLORING YOUR RESEARCH ID","terms":["Fall"],"prereqs":[],"subject":"CASC","credits":2}
,{"_id": "CASC 149","subid":[],"name":"CULTURE OF THE ACADEMY II","terms":["Fall"],"prereqs":[],"subject":"CASC","credits":2}
,{"_id": "CASC 206A","subid":[],"name":"ADVANCED A C-E SCHOLARSHIP","terms":["Fall"],"prereqs":[],"subject":"CASC","credits":1}
,{"_id": "CASC 312","subid":[],"name":"SUPPORTIVE PRACTICES PEER ED","terms":["Fall","Spring"],"prereqs":[],"subject":"CASC","credits":1}
,{"_id": "CASC 352","subid":["CASC 353","CASC 354","CASC 355"],"name":"WORKSHOP LEADER 1 CHE 113","terms":["Fall","Fall","Spring"],"prereqs":[],"subject":"CASC","credits":2}
,{"_id": "CASC 358","subid":[],"name":"THE LEADERSHIP EXPERIENCE","terms":["Fall"],"prereqs":[],"subject":"CASC","credits":2}
,{"_id": "CASC 370","subid":[],"name":"APPLIED LDRSHP IN STUDNT GOV","terms":["Fall"],"prereqs":[],"subject":"CASC","credits":4}
,{"_id": "CASC 390","subid":[],"name":"SUPERVISED TEACHING-CASC 370","terms":["Fall"],"prereqs":[],"subject":"CASC","credits":4}
,{"_id": "CASC 390A","subid":[],"name":"SUPERVISED TEACHING - CASC350","terms":["Fall"],"prereqs":[],"subject":"CASC","credits":4}
,{"_id": "CASC 392A","subid":[],"name":"E5 PRACTICUM","terms":["Fall"],"prereqs":[],"subject":"CASC","credits":1}
,{"_id": "CASC 396","subid":[],"name":"REMS SEMINAR","terms":["Fall"],"prereqs":[],"subject":"CASC","credits":1}
,{"_id": "CASC 401","subid":[],"name":"NAVIGATING THE GRADUATE ACADEMY","terms":["Fall"],"prereqs":[],"subject":"CASC","credits":1}
,{"_id": "CASC 394I","subid":[],"name":"SPECIAL INTERNSHIP","terms":["Summer","Spring"],"prereqs":[],"subject":"CASC","credits":0}
,{"_id": "CASC 505","subid":[],"name":"INTERNPHD PROGRAM","terms":["Summer"],"prereqs":[],"subject":"CASC","credits":0}
,{"_id": "CASC 010","subid":[],"name":"WRITING WORKSHOP","terms":["Spring"],"prereqs":[],"subject":"CASC","credits":0}
,{"_id": "CASC 016","subid":[],"name":"COMMUNICATION WORKSHOP II","terms":["Spring"],"prereqs":[],"subject":"CASC","credits":0}
,{"_id": "CASC 109","subid":[],"name":"INTENSIVE ACADEMIC WRIT SEMR","terms":["Spring"],"prereqs":[],"subject":"CASC","credits":4}
,{"_id": "CASC 152","subid":["RELC 121"],"name":"BRIDGING THE GAP: DIALOGUE ACROSS DIFFERENCE","terms":["Spring"],"prereqs":[],"subject":"CASC","credits":4}
,{"_id": "CASC 161","subid":[],"name":"BUILDING IMPACTFUL IDEAS","terms":["Spring"],"prereqs":[],"subject":"CASC","credits":2}
,{"_id": "CASC 170","subid":[],"name":"INT'L STUDENT SUCCESS","terms":["Spring"],"prereqs":[],"subject":"CASC","credits":2}
,{"_id": "CASC 202","subid":[],"name":"INTRO TO COM-ENGAGED SCHLSHP","terms":["Spring"],"prereqs":[],"subject":"CASC","credits":2}
,{"_id": "CASC 206B","subid":[],"name":"ADVANCED SEMINAR B CEL","terms":["Spring"],"prereqs":[],"subject":"CASC","credits":1}
,{"_id": "CASC 303","subid":[],"name":"ECOREPS: INTRO LEADERSHIP &AMP; SUSTAINABILITY","terms":["Spring"],"prereqs":[],"subject":"CASC","credits":2}
,{"_id": "CASC 319","subid":[],"name":"STUDY ZONE LEADER TRAINING","terms":["Spring"],"prereqs":[],"subject":"CASC","credits":1}
,{"_id": "CASC 351","subid":[],"name":"LEADERSHIP IN THE COLLEGE COMMUNITY I","terms":["Spring"],"prereqs":[],"subject":"CASC","credits":1}
,{"_id": "CASC 360","subid":[],"name":"LEADERSHIP IN A DIVERSE WORLD","terms":["Spring"],"prereqs":[],"subject":"CASC","credits":2}
,{"_id": "CASC 394A","subid":[],"name":"EUROPN HLTH SCIENCE INTRNSHP","terms":["Spring"],"prereqs":[],"subject":"CASC","credits":8}
,{"_id": "CASC 394B","subid":[],"name":"EUROPEAN BUSINESS INTERNSHIP","terms":["Spring"],"prereqs":[],"subject":"CASC","credits":8}
,{"_id": "CASC 397","subid":[],"name":"SENIOR SCHOLARS PROGRAM","terms":["Spring"],"prereqs":[],"subject":"CASC","credits":16}
,{"_id": "CASC 397K","subid":[],"name":"E5 PRACTICUM","terms":["Spring"],"prereqs":[],"subject":"CASC","credits":1}
,{"_id": "CASC 504","subid":[],"name":"PHD CAREERS &AMP; INTERNSHIP PREP","terms":["Spring"],"prereqs":[],"subject":"CASC","credits":2}
,{"_id": "CGRK 101","subid":[],"name":"NEW TESTMNT&AMP;CLASSICAL GREEK","terms":["Fall"],"prereqs":[],"subject":"CGRK","credits":5}
,{"_id": "CGRK 103","subid":[],"name":"INTERMEDIATE GREEK 1","terms":["Fall"],"prereqs":[],"subject":"CGRK","credits":4}
,{"_id": "CGRK 203","subid":[],"name":"EURIPIDES� MEDEA","terms":["Fall"],"prereqs":[],"subject":"CGRK","credits":4}
,{"_id": "CGRK 394","subid":[],"name":"INTERNSHIP","terms":["Fall"],"prereqs":[],"subject":"CGRK","credits":0}
,{"_id": "CGRK 102","subid":[],"name":"NEW TESTMNT-CLASS GRK II","terms":["Spring"],"prereqs":[],"subject":"CGRK","credits":4}
,{"_id": "CGRK 222","subid":[],"name":"HERODOTUS","terms":["Spring"],"prereqs":[],"subject":"CGRK","credits":4}
,{"_id": "CGRK 392","subid":[],"name":"PRACTICUM","terms":["Spring"],"prereqs":[],"subject":"CGRK","credits":4}
,{"_id": "CHE 150","subid":[],"name":"INTRO TO SUSTAINABLE ENERGY","terms":["Fall"],"prereqs":[],"subject":"CHE","credits":4}
,{"_id": "CHE 244","subid":["CHE 444"],"name":"HEAT &AMP; MASS TRANSFER","terms":["Fall"],"prereqs":[],"subject":"CHE","credits":4}
,{"_id": "CHE 246","subid":[],"name":"LAB IN CHE PRINCIPLES","terms":["Fall"],"prereqs":[],"subject":"CHE","credits":4}
,{"_id": "CHE 258","subid":["CHE 458","MSC 458","TEC 458"],"name":"ELECTROCHEM BATT &AMP; FUEL CELL","terms":["Fall"],"prereqs":[],"subject":"CHE","credits":4}
,{"_id": "CHE 272","subid":[],"name":"CHE PROCESS CONTROL","terms":["Fall"],"prereqs":[],"subject":"CHE","credits":4}
,{"_id": "CHE 287","subid":["CHE 487","CHEM 487","TEC 487"],"name":"SURFACE ANALYSIS","terms":["Fall"],"prereqs":[],"subject":"CHE","credits":4}
,{"_id": "CHE 390A","subid":[],"name":"SUPERVISED TEACHING CHE 113","terms":["Fall"],"prereqs":[],"subject":"CHE","credits":2}
,{"_id": "CHE 394","subid":[],"name":"INDEPENDENT INTERNSHIP","terms":["Fall"],"prereqs":[],"subject":"CHE","credits":4}
,{"_id": "CHE 400","subid":["MATH 281","ME 201","ME 400"],"name":"APPLIED BOUNDARY VALUE PROB","terms":["Fall"],"prereqs":[],"subject":"CHE","credits":4}
,{"_id": "CHE 413","subid":[],"name":"ENGINEERING OF SOFT MATTER","terms":["Fall"],"prereqs":[],"subject":"CHE","credits":4}
,{"_id": "CHE 414","subid":["OPT 411","PHYS 401"],"name":"MATH METH OF OPTICS &AMP; PHY","terms":["Fall"],"prereqs":[],"subject":"CHE","credits":4}
,{"_id": "CHE 441","subid":["TEC 441"],"name":"ADV TRANSPORT PHENOMENA","terms":["Fall"],"prereqs":[],"subject":"CHE","credits":4}
,{"_id": "CHE 446","subid":["MSC 446","OPT 426"],"name":"LIQUID CRYSTAL MATERIALS 1: STRUCTURE, PROPERTIES AND APPLICATIONS","terms":["Fall"],"prereqs":[],"subject":"CHE","credits":2}
,{"_id": "CHE 454","subid":["MSC 454","TEC 454"],"name":"INTERFACIAL ENGINEERING","terms":["Fall"],"prereqs":[],"subject":"CHE","credits":4}
,{"_id": "CHE 495","subid":[],"name":"MASTER'S RESEARCH IN CHEM ENGR","terms":["Fall","Spring"],"prereqs":[],"subject":"CHE","credits":12}
,{"_id": "CHE 497","subid":[],"name":"TEACHING CHEM ENGR","terms":["Fall","Spring"],"prereqs":[],"subject":"CHE","credits":3}
,{"_id": "CHE 595","subid":[],"name":"PHD RESEARCH IN CHEM ENGR","terms":["Fall","Spring"],"prereqs":[],"subject":"CHE","credits":12}
,{"_id": "CHE 895","subid":[],"name":"CONT OF MASTER'S ENROLLMENT","terms":["Fall","Spring"],"prereqs":[],"subject":"CHE","credits":0}
,{"_id": "CHE 897","subid":[],"name":"MASTERS DISSERTATION","terms":["Fall","Spring"],"prereqs":[],"subject":"CHE","credits":0}
,{"_id": "CHE 995","subid":[],"name":"CONT OF DOCTORAL ENROLLMENT","terms":["Fall","Spring"],"prereqs":[],"subject":"CHE","credits":0}
,{"_id": "CHE 997","subid":[],"name":"DOCTORAL DISSERTATION","terms":["Summer","Spring"],"prereqs":[],"subject":"CHE","credits":0}
,{"_id": "CHE 999","subid":[],"name":"DOCTORAL DISSERTATION","terms":["Summer","Spring"],"prereqs":[],"subject":"CHE","credits":0}
,{"_id": "CHE 116","subid":[],"name":"NUMERICAL METHODS AND STAT","terms":["Spring"],"prereqs":["CHE 113","CHE 161","CHE 162","CHE 165"],"subject":"CHE","credits":4}
,{"_id": "CHE 226","subid":[],"name":"THERMODYNAMICS II","terms":["Spring"],"prereqs":[],"subject":"CHE","credits":4}
,{"_id": "CHE 231","subid":["CHE 431"],"name":"CHEMICAL REACTOR DESIGN","terms":["Spring"],"prereqs":["CHE 113","CHE 165","CHE 225","CHE 244"],"subject":"CHE","credits":4}
,{"_id": "CHE 243","subid":["CHE 443"],"name":"FLUID DYNAMICS","terms":["Spring"],"prereqs":[],"subject":"CHE","credits":4}
,{"_id": "CHE 250","subid":[],"name":"SEPARATION PROCESSES","terms":["Spring"],"prereqs":["CHE 113","CHE 225","CHE 244"],"subject":"CHE","credits":4}
,{"_id": "CHE 255","subid":[],"name":"CHE SENIOR DESIGN LAB LECTURE","terms":["Spring"],"prereqs":[],"subject":"CHE","credits":4}
,{"_id": "CHE 262","subid":["BME 262","BME 462","CHE 462","MSC 462"],"name":"CELL &AMP; TISSUE ENGINEERING","terms":["Spring"],"prereqs":["BME 260","CHE 225","ME 123","CHE 243","CHE 244","BME 211","BME 411","BIOL 202","BIOL 210"],"subject":"CHE","credits":4}
,{"_id": "CHE 273","subid":["CHE 473"],"name":"PROC DESIGN AND SIMULATION","terms":["Spring"],"prereqs":[],"subject":"CHE","credits":2}
,{"_id": "CHE 279","subid":[],"name":"CHEM ENGINEERING PRACTICE","terms":["Spring"],"prereqs":[],"subject":"CHE","credits":1}
,{"_id": "CHE 456","subid":["CHEM 259","CHEM 459"],"name":"ELECTROCHEM ENG FUND&AMP;APP","terms":["Spring"],"prereqs":[],"subject":"CHE","credits":4}
,{"_id": "CHE 461","subid":["MSC 461"],"name":"ADVANCED CHEMICAL KINETICS","terms":["Spring"],"prereqs":[],"subject":"CHE","credits":4}
,{"_id": "CHE 465","subid":["TEC 465"],"name":"GREEN CHEMICAL ENGINEERING","terms":["Spring"],"prereqs":[],"subject":"CHE","credits":4}
,{"_id": "CHE 491","subid":[],"name":"MASTER'S READING COURSE CHE","terms":["Spring"],"prereqs":[],"subject":"CHE","credits":5}
,{"_id": "CHE 494","subid":[],"name":"MASTERS INTERNSHIP","terms":["Spring"],"prereqs":[],"subject":"CHE","credits":1}
,{"_id": "CHE 498","subid":[],"name":"MASTER'S INDEPENDENT STUDY","terms":["Spring"],"prereqs":[],"subject":"CHE","credits":4}
,{"_id": "CHE 594","subid":[],"name":"INTERNSHIP PHD","terms":["Spring","Spring"],"prereqs":[],"subject":"CHE","credits":1}
,{"_id": "CHE 899A","subid":[],"name":"MSTRS DISSERTATN IN ABSENTIA","terms":["Spring"],"prereqs":[],"subject":"CHE","credits":0}
,{"_id": "CHE 999A","subid":[],"name":"DOCT DISSERTATN IN ABSENTIA","terms":["Spring"],"prereqs":[],"subject":"CHE","credits":0}
,{"_id": "CHE 999B","subid":[],"name":"DOC DISS IN-ABSENTIA ABROAD","terms":["Spring"],"prereqs":[],"subject":"CHE","credits":0}
,{"_id": "CHEM 131","subid":[],"name":"CHM CONCPTS, SYST, PRACT I","terms":["Fall"],"prereqs":[],"subject":"CHEM","credits":5}
,{"_id": "CHEM 137","subid":[],"name":"CHM PRINCIPLES FOR ENGINEERS","terms":["Fall"],"prereqs":[],"subject":"CHEM","credits":4}
,{"_id": "CHEM 171","subid":[],"name":"FIRST-YEAR ORGANIC CHEMISTRY","terms":["Fall"],"prereqs":[],"subject":"CHEM","credits":4}
,{"_id": "CHEM 173","subid":[],"name":"FIRST-YEAR ORGANIC CHEM LAB LECTURE","terms":["Fall"],"prereqs":["CHEM 173","CHEM 171"],"subject":"CHEM","credits":1}
,{"_id": "CHEM 203","subid":[],"name":"ORGANIC CHEMISTRY","terms":["Fall","Summer"],"prereqs":["CHEM 207","CHEM 131","CHEM 132"],"subject":"CHEM","credits":4}
,{"_id": "CHEM 207","subid":[],"name":"ORG CHM LAB LECTURE","terms":["Fall","Summer"],"prereqs":[],"subject":"CHEM","credits":1}
,{"_id": "CHEM 211","subid":["CHEM 411"],"name":"INORGANIC CHEMISTRY I","terms":["Fall"],"prereqs":["CHEM 411"],"subject":"CHEM","credits":4}
,{"_id": "CHEM 231W","subid":[],"name":"CHEMICAL INSTRUMENTATION","terms":["Fall"],"prereqs":["CHEM 231","CHEM 251","CHEM 131","CHEM 132","CHEM 203","CHEM 204","CHEM 171","CHEM 172"],"subject":"CHEM","credits":4}
,{"_id": "CHEM 251","subid":["CHEM 441"],"name":"PHYSICAL CHEMISTRY I","terms":["Fall"],"prereqs":["PHYS 113","PHYS 114","PHYS 121","PHYS 122","MTH 163","MTH 165","CHEM 441"],"subject":"CHEM","credits":4}
,{"_id": "CHEM 286","subid":["CHEM 486"],"name":"ENERGY SCIENCE TECH &AMP; SOCIETY","terms":["Fall"],"prereqs":[],"subject":"CHEM","credits":4}
,{"_id": "CHEM 393","subid":[],"name":"SENIOR RESEARCH PROJECT","terms":["Fall","Spring"],"prereqs":[],"subject":"CHEM","credits":4}
,{"_id": "CHEM 394","subid":[],"name":"INTERNSHIP","terms":["Fall"],"prereqs":[],"subject":"CHEM","credits":4}
,{"_id": "CHEM 395","subid":[],"name":"INDEPENDENT RESEARCH","terms":["Fall"],"prereqs":[],"subject":"CHEM","credits":4}
,{"_id": "CHEM 424","subid":[],"name":"PHYSICAL METHODS IN INORGANIC CHEMISTRY","terms":["Fall"],"prereqs":[],"subject":"CHEM","credits":2}
,{"_id": "CHEM 433","subid":[],"name":"ADVANCED ORGANIC CHEM I","terms":["Fall"],"prereqs":["CHEM 419","CHEM 434","CHEM 435","CHEM 171","CHEM 172","CHEM 203","CHEM 204"],"subject":"CHEM","credits":4}
,{"_id": "CHEM 451","subid":[],"name":"QUANTUM CHEMISTRY I","terms":["Fall"],"prereqs":[],"subject":"CHEM","credits":4}
,{"_id": "CHEM 456","subid":["MSC 456","OPT 429"],"name":"CHEM BONDS:FROM MOLCLS TO MAT","terms":["Fall","Spring"],"prereqs":[],"subject":"CHEM","credits":4}
,{"_id": "CHEM 458","subid":[],"name":"SPECTROSCOPY AND KINETICS","terms":["Fall"],"prereqs":["CHEM 251"],"subject":"CHEM","credits":4}
,{"_id": "CHEM 487","subid":["CHE 287","CHE 487","TEC 487"],"name":"SURFACE ANALYSIS","terms":["Fall"],"prereqs":[],"subject":"CHEM","credits":4}
,{"_id": "CHEM 495","subid":[],"name":"MASTER'S RESEARCH","terms":["Fall"],"prereqs":[],"subject":"CHEM","credits":0}
,{"_id": "CHEM 511","subid":[],"name":"CHEMISTRY SEMINAR","terms":["Fall","Spring"],"prereqs":[],"subject":"CHEM","credits":1}
,{"_id": "CHEM 585","subid":[],"name":"1ST YR GRADUATE WORKSHOP","terms":["Fall","Spring"],"prereqs":[],"subject":"CHEM","credits":1}
,{"_id": "CHEM 595B","subid":[],"name":"PHD RESEARCH IN ABSENTIA ABROAD","terms":["Fall","Spring"],"prereqs":[],"subject":"CHEM","credits":12}
,{"_id": "CHEM 895","subid":[],"name":"CONT OF MASTER'S ENROLLMENT","terms":["Fall"],"prereqs":[],"subject":"CHEM","credits":0}
,{"_id": "CHEM 995","subid":[],"name":"CONT OF DOCTORAL ENROLLMENT","terms":["Fall","Spring"],"prereqs":[],"subject":"CHEM","credits":0}
,{"_id": "CHEM 204","subid":[],"name":"ORGANIC CHEMISTRY II","terms":["Summer","Spring"],"prereqs":["CHEM 208","CHEM 210","CHEM 203"],"subject":"CHEM","credits":4}
,{"_id": "CHEM 386V","subid":[],"name":"VISITING STUDENT IN CHEMISTRY","terms":["Summer"],"prereqs":[],"subject":"CHEM","credits":0}
,{"_id": "CHEM 595","subid":[],"name":"PHD RESEARCH IN CHEMISTRY","terms":["Summer","Spring"],"prereqs":[],"subject":"CHEM","credits":12}
,{"_id": "CHEM 997","subid":[],"name":"DOCTORAL DISSERTATION","terms":["Summer","Spring"],"prereqs":[],"subject":"CHEM","credits":0}
,{"_id": "CHEM 132","subid":[],"name":"CHEM CONCEPTS, SYST, PRACT II","terms":["Spring"],"prereqs":["THE 134","CHEM 131"],"subject":"CHEM","credits":5}
,{"_id": "CHEM 172","subid":[],"name":"FIRST-YEAR ORGANIC CHEM II","terms":["Spring"],"prereqs":["CHEM 172","CHEM 171","THE 208","CHEM 210","SPAN 134","CHEM 173"],"subject":"CHEM","credits":4}
,{"_id": "CHEM 208","subid":[],"name":"ORGANIC CHEMISTRY II: LAB LECTURE","terms":["Spring"],"prereqs":["CHEM 207","CHEM 210","CHEM 134","CHEM 173","CHEM 172","CHEM 204"],"subject":"CHEM","credits":1}
,{"_id": "CHEM 210W","subid":[],"name":"ORGANIC CHEMISTRY II H:LAB LECTURE","terms":["Spring"],"prereqs":["CHEM 210","CHEM 172","CHEM 204","CHEM 134","CHEM 207","CHEM 173"],"subject":"CHEM","credits":2}
,{"_id": "CHEM 234","subid":["CHEM 234W"],"name":"ADV LABORATORY TECHNIQUES","terms":["Spring"],"prereqs":["THE 134","CHEM 211"],"subject":"CHEM","credits":4}
,{"_id": "CHEM 244W","subid":["CHEM 444","PHYS 245W","PHYS 445"],"name":"THE ADV NUCLEAR SCI EDU LAB","terms":["Spring"],"prereqs":[],"subject":"CHEM","credits":0}
,{"_id": "CHEM 252","subid":["CHEM 442"],"name":"PHYSICAL CHEMISTRY II","terms":["Spring"],"prereqs":["CHEM 131","CHEM 132","THE 113","THE 143"],"subject":"CHEM","credits":4}
,{"_id": "CHEM 259","subid":["CHE 456","CHEM 459"],"name":"ELECTROCHEM ENG FUND&AMP;APP","terms":["Spring"],"prereqs":[],"subject":"CHEM","credits":4}
,{"_id": "CHEM 262","subid":["CHEM 462"],"name":"BIOLOGICAL CHEMISTRY","terms":["Spring"],"prereqs":["CHEM 462","BIOL 250","CHEM 262","CHEM 171","CHEM 203"],"subject":"CHEM","credits":4}
,{"_id": "CHEM 275","subid":["CHEM 475"],"name":"THE CHEMISTRY OF POISONS","terms":["Spring"],"prereqs":[],"subject":"CHEM","credits":4}
,{"_id": "CHEM 422","subid":[],"name":"ORGANOMETALLIC CHEMISTRY","terms":["Spring"],"prereqs":["CHEM 423","CHEM 421"],"subject":"CHEM","credits":2}
,{"_id": "CHEM 434","subid":[],"name":"ADV PHYSICAL ORGANIC CHEM II","terms":["Spring"],"prereqs":[],"subject":"CHEM","credits":4}
,{"_id": "CHEM 436","subid":[],"name":"TRANSITION METAL CATALYSIS IN ORGANIC SYNTHESIS I","terms":["Spring"],"prereqs":["CHEM 421"],"subject":"CHEM","credits":2}
,{"_id": "CHEM 438","subid":[],"name":"ORGANIC SYNTHESIS","terms":["Spring"],"prereqs":[],"subject":"CHEM","credits":2}
,{"_id": "CHEM 446","subid":[],"name":"NANOPOROUS MATERIALS CHEMISTRY","terms":["Spring"],"prereqs":["CHEM 211","CHEM 252"],"subject":"CHEM","credits":2}
,{"_id": "CHEM 452","subid":[],"name":"QUANTUM DYNAMICS","terms":["Spring"],"prereqs":["CHEM 451"],"subject":"CHEM","credits":4}
,{"_id": "CHEM 469","subid":[],"name":"COMPUTATIONAL CHEMISTRY I","terms":["Spring"],"prereqs":[],"subject":"CHEM","credits":2}
,{"_id": "CHEM 470","subid":[],"name":"COMPUTATIONAL CHEMISTRY II","terms":["Spring"],"prereqs":[],"subject":"CHEM","credits":2}
,{"_id": "CHEM 583","subid":[],"name":"ADV CHEMISTRY SEM &AMP; COLLOQUIUM","terms":["Spring"],"prereqs":[],"subject":"CHEM","credits":0}
,{"_id": "CHEM 593","subid":[],"name":"SPECIAL TOPICS IN CHEMISTRY","terms":["Spring"],"prereqs":[],"subject":"CHEM","credits":0}
,{"_id": "CHEM 594","subid":[],"name":"INTERNSHIP","terms":["Spring"],"prereqs":[],"subject":"CHEM","credits":1}
,{"_id": "CHEM 595A","subid":[],"name":"PHD RESEARCH IN ABSENTIA","terms":["Spring"],"prereqs":[],"subject":"CHEM","credits":12}
,{"_id": "CHEM 997A","subid":[],"name":"DOCT DISSERTATN IN ABSENTIA","terms":["Spring"],"prereqs":[],"subject":"CHEM","credits":0}
,{"_id": "CHEM 999","subid":[],"name":"DOCTORAL DISSERTATION","terms":["Spring"],"prereqs":[],"subject":"CHEM","credits":0}
,{"_id": "CHEM 999A","subid":[],"name":"DOCT DISSERTATN IN ABSENTIA","terms":["Spring"],"prereqs":[],"subject":"CHEM","credits":0}
,{"_id": "CHEM 999B","subid":[],"name":"DOCTORAL DISSERTATION IN ABSENTIA ABROAD","terms":["Spring"],"prereqs":[],"subject":"CHEM","credits":0}
,{"_id": "CHIN 202","subid":[],"name":"ADVANCED  INTERMEDIATE CHINESE","terms":["Fall"],"prereqs":[],"subject":"CHIN","credits":4}
,{"_id": "CHIN 205","subid":[],"name":"ADVANCED CHINESE I","terms":["Fall"],"prereqs":[],"subject":"CHIN","credits":4}
,{"_id": "CHIN 216","subid":["CLTR 216"],"name":"WRITING DISCONTENTMENT: POLITICAL TURMOIL, SOCIAL CRITIQUE AND CIVIC RESPONSIBILITY IN LATE QING LITERATURE","terms":["Fall"],"prereqs":[],"subject":"CHIN","credits":4}
,{"_id": "CHIN 221","subid":["CLTR 269"],"name":"LABORERS, SOJOURNERS, IMMIGRANTS: CHINESE JOURNEYS TO THE AMERICAS (19TH-21ST CENTURIES)","terms":["Fall"],"prereqs":[],"subject":"CHIN","credits":4}
,{"_id": "CHIN 275","subid":["HIST 148","RELC 175"],"name":"RELIGION &AMP; CHINESE SOCIETY","terms":["Fall"],"prereqs":[],"subject":"CHIN","credits":4}
,{"_id": "CHIN 390","subid":[],"name":"SUPERVISED TEACHING CHIN 101","terms":["Fall","Spring"],"prereqs":[],"subject":"CHIN","credits":4}
,{"_id": "CHIN 102","subid":[],"name":"ELEMENTARY CHINESE II","terms":["Spring"],"prereqs":[],"subject":"CHIN","credits":6}
,{"_id": "CHIN 152","subid":[],"name":"INTERMEDIATE CHINESE II","terms":["Spring"],"prereqs":[],"subject":"CHIN","credits":6}
,{"_id": "CHIN 203","subid":[],"name":"ADV INTERMEDIATE CHINESE II","terms":["Spring"],"prereqs":[],"subject":"CHIN","credits":4}
,{"_id": "CHIN 222","subid":["CLTR 224","GSWS 222"],"name":"GENDER, SEXUALITY, AND DESIRE IN 20TH CENTURY CHINESE LITERATURE","terms":["Spring"],"prereqs":[],"subject":"CHIN","credits":4}
,{"_id": "CIS 191","subid":[],"name":"INTRODUCTION TO  PROGRAMMING FOR BUSINESS ANALYTIC","terms":["Fall","Spring"],"prereqs":[],"subject":"CIS","credits":4}
,{"_id": "CIS 211","subid":[],"name":"BUSINESS MODELING WITH EXCEL","terms":["Fall","Spring"],"prereqs":[],"subject":"CIS","credits":4}
,{"_id": "CIS 220","subid":[],"name":"BUSINESS INFORMATION SYSTEMS &AMP; ANALYTICS","terms":["Fall","Spring"],"prereqs":[],"subject":"CIS","credits":4}
,{"_id": "CIS 240","subid":[],"name":"DATA MGT/DESCR ANALYTICS-BUS","terms":["Fall"],"prereqs":[],"subject":"CIS","credits":4}
,{"_id": "CIS 242","subid":[],"name":"PREDICTIVE ANALYTICS FOR BUSINESS","terms":["Spring"],"prereqs":["CIS 191"],"subject":"CIS","credits":4}
,{"_id": "CLST 101","subid":[],"name":"INTRODUCTION TO ANTIQUITY","terms":["Fall"],"prereqs":[],"subject":"CLST","credits":4}
,{"_id": "CLST 121","subid":["HIST 121"],"name":"HISTORY OF THE ANCIENT ROMAN WORLD","terms":["Fall"],"prereqs":[],"subject":"CLST","credits":4}
,{"_id": "CLST 140","subid":["ENGL 112","RELC 140"],"name":"CLASSICAL AND SCRIPTURAL BACKGROUNDS","terms":["Fall"],"prereqs":[],"subject":"CLST","credits":4}
,{"_id": "CLST 151","subid":[],"name":"ATHENIAN DEMOCRACY","terms":["Fall"],"prereqs":[],"subject":"CLST","credits":4}
,{"_id": "CLST 224","subid":["HIST 111"],"name":"THE GREEKS AND THE PERSIAN EMPIRE","terms":["Fall"],"prereqs":[],"subject":"CLST","credits":4}
,{"_id": "CLST 110","subid":["RELC 135"],"name":"CLASSICAL MYTHOLOGY","terms":["Spring"],"prereqs":[],"subject":"CLST","credits":4}
,{"_id": "CLST 131","subid":["AHST 199","HIST 104"],"name":"ANCIENT CITIES OF THE MEDITERRANEAN","terms":["Spring"],"prereqs":[],"subject":"CLST","credits":4}
,{"_id": "CLST 134","subid":["AHST 140","ATHS 210","HIST 117"],"name":"ARCHAEOLOGICAL THOUGHT","terms":["Spring"],"prereqs":[],"subject":"CLST","credits":4}
,{"_id": "CLST 203","subid":["PHIL 201"],"name":"HISTORY OF ANCIENT PHILOSOPHY","terms":["Spring"],"prereqs":[],"subject":"CLST","credits":4}
,{"_id": "CLST 220","subid":["CLTR 204A","HIST 296"],"name":"WRITING HISTORY IN ANCIENT GREECE AND ROME","terms":["Spring"],"prereqs":[],"subject":"CLST","credits":4}
,{"_id": "CLST 230","subid":["AHST 225","CLST 230W"],"name":"GREEK ART &AMP; ARCHAEOLOGY","terms":["Spring"],"prereqs":[],"subject":"CLST","credits":4}
,{"_id": "CLST 294","subid":["RELC 294"],"name":"ANCIENT ROME IN CONTEXT","terms":["Spring"],"prereqs":[],"subject":"CLST","credits":2}
,{"_id": "CLST 389","subid":[],"name":"SENIOR CAPSTONE WORKSHOP","terms":["Spring"],"prereqs":[],"subject":"CLST","credits":1}
,{"_id": "CLST 392","subid":[],"name":"PRACTICUM","terms":["Spring"],"prereqs":[],"subject":"CLST","credits":4}
,{"_id": "CLST 393W","subid":[],"name":"SENIOR PROJECT","terms":["Spring"],"prereqs":[],"subject":"CLST","credits":4}
,{"_id": "CLTR 200","subid":[],"name":"TOPICS IN CRITICAL THINKING: FAIRY TALES","terms":["Fall","Spring"],"prereqs":[],"subject":"CLTR","credits":4}
,{"_id": "CLTR 202B","subid":["CLTR 402B","FMST 209","GRMN 247","GRMN 447","JWST 219"],"name":"HOLOCAUST: AFFECT AND ABSENCE","terms":["Fall"],"prereqs":[],"subject":"CLTR","credits":4}
,{"_id": "CLTR 204","subid":["HIST 145","JPNS 215"],"name":"MODERN JAPAN","terms":["Fall"],"prereqs":[],"subject":"CLTR","credits":4}
,{"_id": "CLTR 208A","subid":["AHST 212","HIST 146","JPNS 210","RELC 132"],"name":"VENGEANCE, LONGING, AND SALVATION: TOPICS IN TRADITIONAL JAPANESE CULTURE","terms":["Fall"],"prereqs":[],"subject":"CLTR","credits":4}
,{"_id": "CLTR 208H","subid":["AHST 216","AHST 416","CLTR 408H","JPNS 216","RELC 225"],"name":"CULTURES OF ENLIGHTENMENT: MEDITATION, MATERIALITY, AND THE LITERARY CULTURES OF JAPANESE BUDDHISM","terms":["Fall"],"prereqs":[],"subject":"CLTR","credits":4}
,{"_id": "CLTR 209A","subid":["HIST 130","RSST 128","RUSS 128"],"name":"RUSSIAN CIVILIZATION: MYTH, CULTURE, HISTORY","terms":["Fall"],"prereqs":[],"subject":"CLTR","credits":4}
,{"_id": "CLTR 210","subid":["ENGL 258","FMST 207","FMST 407","JPNS 294"],"name":"HAYAO MIYAZAKI AND PLANET GHIBLI","terms":["Fall"],"prereqs":[],"subject":"CLTR","credits":4}
,{"_id": "CLTR 212","subid":["CLTR 412","FMST 236","GRMN 212","GRMN 412"],"name":"MONSTERS, GHOSTS, &AMP; ALIENS","terms":["Fall","Spring"],"prereqs":[],"subject":"CLTR","credits":4}
,{"_id": "CLTR 216","subid":["CHIN 216"],"name":"WRITING DISCONTENTMENT: POLITICAL TURMOIL, SOCIAL CRITIQUE AND CIVIC RESPONSIBILITY IN LATE QING LITERATURE:","terms":["Fall"],"prereqs":[],"subject":"CLTR","credits":4}
,{"_id": "CLTR 221","subid":["AAAS 303","AAAS 444","CLTR 421","FREN 243","FREN 443","GSWS 244","GSWS 444"],"name":"MUTILATED BODIES: FROM TRADITIONS TO CUTTING-EDGE TECHNOLOGIES","terms":["Fall"],"prereqs":[],"subject":"CLTR","credits":4}
,{"_id": "CLTR 222C","subid":["CLTR 422C","GRMN 221","GRMN 421","GSWS 271"],"name":"GENDER, LOVE &AMP; FAMILIES","terms":["Fall"],"prereqs":[],"subject":"CLTR","credits":4}
,{"_id": "CLTR 242","subid":["CLTR 442B","ENGL 256E","FMST 240","ITAL 242"],"name":"CAPITALISM, CULTURE, CONTROVERSY: THE REVOLUTIONARY CINEMA OF PIER PAOLO PASOLINI","terms":["Fall"],"prereqs":[],"subject":"CLTR","credits":4}
,{"_id": "CLTR 247","subid":["CLTR 447A","HIST 288","ITAL 247"],"name":"POLITICS AND CULTURE IN FASCIST ITALY","terms":["Fall"],"prereqs":["THE 194"],"subject":"CLTR","credits":4}
,{"_id": "CLTR 250","subid":["CLTR 450","ENGL 243M","RSST 240","RUSS 240"],"name":"NABOKOV- UNUSUAL �MIGR�","terms":["Fall"],"prereqs":[],"subject":"CLTR","credits":4}
,{"_id": "CLTR 256B","subid":["ENGL 243A","SPAN 215"],"name":"DON QUIJOTE: THE BOOK, THE MYTH, THE IMAGE","terms":["Fall"],"prereqs":[],"subject":"CLTR","credits":4}
,{"_id": "CLTR 264D","subid":["FMST 271","FMST 471","JPNS 270"],"name":"STRAIGHTJACKET SOCIETY:  JUZO ITAMI'S CINEMA","terms":["Fall"],"prereqs":["THE 198","THE 199"],"subject":"CLTR","credits":4}
,{"_id": "CLTR 269","subid":["CHIN 221"],"name":"LABORERS, SOJOURNERS, IMMIGRANTS: CHINESE JOURNEYS TO THE AMERICAS (19TH-21ST CENTURIES)","terms":["Fall"],"prereqs":[],"subject":"CLTR","credits":4}
,{"_id": "CLTR 275A","subid":["AAAS 275","JPNS 275","MUSC 275"],"name":"HIP HOP JAPAN","terms":["Fall"],"prereqs":[],"subject":"CLTR","credits":4}
,{"_id": "CLTR 277","subid":["CLTR 477","ENGL 236A","ENGL 436A","FREN 277","FREN 477","ITAL 277","ITAL 477"],"name":"POSTMODERNISM: FICTION, PHILOSOPHY, MEDIA","terms":["Fall"],"prereqs":[],"subject":"CLTR","credits":4}
,{"_id": "CLTR 389","subid":["CLTR 489"],"name":"MLC RESEARCH SEMINAR","terms":["Fall","Spring"],"prereqs":[],"subject":"CLTR","credits":4}
,{"_id": "CLTR 393H","subid":[],"name":"HONORS THESIS","terms":["Fall"],"prereqs":[],"subject":"CLTR","credits":4}
,{"_id": "CLTR 394","subid":[],"name":"INTERNSHIP","terms":["Fall"],"prereqs":[],"subject":"CLTR","credits":4}
,{"_id": "CLTR 462","subid":["AHST 583"],"name":"ART HISTORY COLLOQUIUM","terms":["Fall"],"prereqs":[],"subject":"CLTR","credits":4}
,{"_id": "CLTR 592","subid":[],"name":"LANGUAGES LEARNING &AMP;TEACHING","terms":["Fall"],"prereqs":[],"subject":"CLTR","credits":2}
,{"_id": "CLTR 895","subid":[],"name":"CONT OF MASTER'S ENROLLMENT","terms":["Fall"],"prereqs":[],"subject":"CLTR","credits":0}
,{"_id": "CLTR 151","subid":["HIST 151"],"name":"MODERN LATIN AMERICA","terms":["Spring"],"prereqs":[],"subject":"CLTR","credits":4}
,{"_id": "CLTR 204A","subid":["CLST 220","HIST 296"],"name":"WRITING HISTORY IN ANCIENT GREECE AND ROME","terms":["Spring"],"prereqs":[],"subject":"CLTR","credits":4}
,{"_id": "CLTR 214N","subid":[],"name":"TOURIST JAPAN","terms":["Spring"],"prereqs":[],"subject":"CLTR","credits":4}
,{"_id": "CLTR 214R","subid":["RSST 214","RUSS 214"],"name":"RUSSIAN FOLKLORE","terms":["Spring"],"prereqs":[],"subject":"CLTR","credits":4}
,{"_id": "CLTR 224","subid":["CHIN 222","GSWS 222"],"name":"GENDER, SEXUALITY, AND DESIRE IN 20TH CENTURY CHINESE LITERATURE","terms":["Spring"],"prereqs":[],"subject":"CLTR","credits":4}
,{"_id": "CLTR 228A","subid":["GSWS 221","ITAL 250"],"name":"WARTIME LOVE: ITALIAN NOVELS OF THE FIFTIES AND SIXTIES","terms":["Spring"],"prereqs":[],"subject":"CLTR","credits":4}
,{"_id": "CLTR 229A","subid":["AAAS 247","AAAS 447","CLTR 429A"],"name":"BIOGRAPHIES OF EMANCIPATION IN THE BLACK WORLD","terms":["Spring"],"prereqs":[],"subject":"CLTR","credits":4}
,{"_id": "CLTR 229B","subid":["AAAS 280","AAAS 412","CLTR 429B","FREN 228","FREN 428"],"name":"HUMANITARIANISM AND SOCIAL INSECURITIES","terms":["Spring"],"prereqs":[],"subject":"CLTR","credits":4}
,{"_id": "CLTR 238A","subid":["CLTR 438A","GRMN 238","GRMN 438","GSWS 237","JWST 243"],"name":"REVOLUTIONS AND REVOLT","terms":["Spring"],"prereqs":[],"subject":"CLTR","credits":4}
,{"_id": "CLTR 240A","subid":["CLTR 440A","FREN 296","FREN 496","TH 282","TH 482"],"name":"PHILOSOPHY OF MUSIC","terms":["Spring"],"prereqs":[],"subject":"CLTR","credits":4}
,{"_id": "CLTR 242A","subid":["CLTR 442A","ENGL 232","GRMN 230","GRMN 430"],"name":"POE AND HOFFMAN","terms":["Spring"],"prereqs":[],"subject":"CLTR","credits":4}
,{"_id": "CLTR 248","subid":["FMST 230","GRMN 248","GSWS 240"],"name":"ON THE MOVE: ETHNOGRAPHIC FILMS","terms":["Spring"],"prereqs":[],"subject":"CLTR","credits":4}
,{"_id": "CLTR 252A","subid":["GRMN 229","GRMN 486"],"name":"KLEIST &AMP; KAFKA","terms":["Spring"],"prereqs":[],"subject":"CLTR","credits":4}
,{"_id": "CLTR 284","subid":["CLTR 484","ENGL 287","LTST 206","LTST 406"],"name":"TRANSLATION&AMP;WORLD LITERATURE","terms":["Spring"],"prereqs":[],"subject":"CLTR","credits":4}
,{"_id": "CLTR 289","subid":["RSST 289","RUSS 289"],"name":"DANGEROUS TEXTS","terms":["Spring"],"prereqs":[],"subject":"CLTR","credits":4}
,{"_id": "CLTR 395","subid":[],"name":"INDEPENDENT RESEARCH","terms":["Spring"],"prereqs":[],"subject":"CLTR","credits":0}
,{"_id": "CLTR 414N","subid":[],"name":"TOURIST JAPAN","terms":["Spring"],"prereqs":[],"subject":"CLTR","credits":4}
,{"_id": "CLTR 438","subid":[],"name":"ON THE MOVE: ETHNOGRAPHIC FILMS","terms":["Spring"],"prereqs":[],"subject":"CLTR","credits":4}
,{"_id": "CSC 161","subid":[],"name":"INTRODUCTION TO PROGRAMMING","terms":["Fall","Spring"],"prereqs":[],"subject":"CSC","credits":4}
,{"_id": "CSC 170","subid":[],"name":"INTRODUCTION TO WEB DEVELOPMENT","terms":["Fall","Spring"],"prereqs":[],"subject":"CSC","credits":4}
,{"_id": "CSC 171","subid":[],"name":"INTRODUCTION TO COMPUTER SCIENCE","terms":["Fall","Summer","Spring"],"prereqs":[],"subject":"CSC","credits":4}
,{"_id": "CSC 172","subid":[],"name":"DATA STRUCTURES &AMP; ALGORITHMS","terms":["Fall","Summer","Spring"],"prereqs":["CSC 171","MTH 150"],"subject":"CSC","credits":4}
,{"_id": "CSC 173","subid":[],"name":"COMPUTATION &AMP; FORMAL SYSTEMS","terms":["Fall","Spring"],"prereqs":["CSC 172","CSC 150"],"subject":"CSC","credits":4}
,{"_id": "CSC 211","subid":[],"name":"INTRODUCTION TO HCI","terms":["Fall","Spring"],"prereqs":["SPAN 172","SPAN 214"],"subject":"CSC","credits":4}
,{"_id": "CSC 214","subid":[],"name":"MOBILE APP DEVELOPMENT","terms":["Fall","Summer","Spring"],"prereqs":["CSC 172"],"subject":"CSC","credits":4}
,{"_id": "CSC 227","subid":["CSC 427","ECE 247","ECE 447","TEE 447"],"name":"INTRO TO DIP USING PYTHON","terms":["Fall"],"prereqs":["ECE 242","ECE 440","ECE 446"],"subject":"CSC","credits":4}
,{"_id": "CSC 240","subid":["DSCC 240"],"name":"DATA MINING","terms":["Fall","Spring"],"prereqs":["CSC 171","CSC 172","MTH 161","CSC 242","CSC 262","MTH 165"],"subject":"CSC","credits":4}
,{"_id": "CSC 242","subid":["BCSC 232","DSCC 242"],"name":"INTRODUCTION TO ARTIFICIAL INTELLIGENCE","terms":["Fall","Spring"],"prereqs":["CSC 172","CSC 150","CSC 173"],"subject":"CSC","credits":4}
,{"_id": "CSC 244","subid":["CSC 444","TCS 444"],"name":"MACHINE REASONING","terms":["Fall"],"prereqs":[],"subject":"CSC","credits":4}
,{"_id": "CSC 245","subid":["CSC 445"],"name":"DEEP LEARNING","terms":["Fall"],"prereqs":["MTH 164","MTH 165","CSC 172"],"subject":"CSC","credits":4}
,{"_id": "CSC 246","subid":[],"name":"MACHINE LEARNING","terms":["Fall","Spring"],"prereqs":["MTH 165","MTH 164","CSC 242"],"subject":"CSC","credits":4}
,{"_id": "CSC 247","subid":["BCSC 235","BCSC 435","CSC 447","LING 247","LING 447","TCS 447"],"name":"NATURAL LANGUAGE PROCESSING","terms":["Fall","Spring"],"prereqs":["CSC 447","CSC 242"],"subject":"CSC","credits":4}
,{"_id": "CSC 252","subid":["CSC 452","TCS 452"],"name":"COMPUTER ORGANIZATION","terms":["Fall","Spring"],"prereqs":["THE 150","CSC 172"],"subject":"CSC","credits":4}
,{"_id": "CSC 253","subid":["CSC 453","TCS 453"],"name":"COLLABORATIVE PROGRAMMING AND SOFTWARE DESIGN","terms":["Fall"],"prereqs":["CSC 453","CSC 172","CSC 253","CSC 252"],"subject":"CSC","credits":4}
,{"_id": "CSC 254","subid":["CSC 454","TCS 454"],"name":"PROGRAMMING LANGUAGE DESIGN &AMP; IMPLEMENTATION","terms":["Fall"],"prereqs":["CSC 173","CSC 252"],"subject":"CSC","credits":4}
,{"_id": "CSC 257","subid":["CSC 457","TCS 457"],"name":"COMPUTER NETWORKS","terms":["Fall"],"prereqs":["CSC 252"],"subject":"CSC","credits":4}
,{"_id": "CSC 261","subid":["CSC 461","DSCC 261","DSCC 461","TCS 461"],"name":"DATABASE SYSTEMS","terms":["Fall","Summer","Spring"],"prereqs":["CSC 172","CSC 173","CSC 252"],"subject":"CSC","credits":4}
,{"_id": "CSC 262","subid":["DSCC 262","STAT 262"],"name":"COMPUTATIONAL INTRODUCTION TO STATISTICS","terms":["Fall","Summer"],"prereqs":["THE 150","THE 142","THE 161","THE 171"],"subject":"CSC","credits":4}
,{"_id": "CSC 264","subid":["AME 277","CSC 464","ECE 277","ECE 477","TEE 477"],"name":"COMPUTER AUDITION","terms":["Fall"],"prereqs":["ECE 246","ECE 446","ECE 272","ECE 472"],"subject":"CSC","credits":4}
,{"_id": "CSC 273W","subid":[],"name":"WRITING FOR COMPUTER SCIENCE","terms":["Fall","Spring"],"prereqs":[],"subject":"CSC","credits":2}
,{"_id": "CSC 277","subid":["CSC 477"],"name":"END-TO-END DEEP LEARNING","terms":["Fall"],"prereqs":["CSC 242","CSC 298","CSC 578","CSC 266","CSC 466","CSC 249","CSC 449"],"subject":"CSC","credits":4}
,{"_id": "CSC 280","subid":["CSC 480","TCS 480"],"name":"COMPUTER MODELS &AMP;LIMITATIONS","terms":["Fall","Summer","Spring"],"prereqs":["CSC 173","MTH 150"],"subject":"CSC","credits":4}
,{"_id": "CSC 281","subid":["CSC 481","TCS 481"],"name":"INTRO TO CRYPTOGRAPHY","terms":["Fall"],"prereqs":[],"subject":"CSC","credits":4}
,{"_id": "CSC 282","subid":["CSC 482","TCS 482"],"name":"DESIGN &AMP; ANALYSIS OF EFFICIENT ALGORITHMS","terms":["Fall","Summer","Spring"],"prereqs":["CSC 172","MTH 150"],"subject":"CSC","credits":4}
,{"_id": "CSC 284","subid":["CSC 484","TCS 484"],"name":"ADVANCED ALGORITHMS","terms":["Fall"],"prereqs":[],"subject":"CSC","credits":4}
,{"_id": "CSC 287","subid":["CSC 487","TCS 487"],"name":"SAMPLING ALGORITHMS","terms":["Fall"],"prereqs":[],"subject":"CSC","credits":4}
,{"_id": "CSC 293","subid":[],"name":"CS IMPROVES: TOOLS FOR 3D PRINTED MANUFACTURING","terms":["Fall"],"prereqs":["CSC 173","CSC 252","CSC 254","CSC 242","CSC 280","CSC 282"],"subject":"CSC","credits":4}
,{"_id": "CSC 299","subid":["CSC 299W"],"name":"SOCIAL IMPLICATIONS OF COMPUTING","terms":["Fall","Summer","Spring"],"prereqs":[],"subject":"CSC","credits":4}
,{"_id": "CSC 390","subid":[],"name":"SUPERVISED TEACHING","terms":["Fall"],"prereqs":[],"subject":"CSC","credits":4}
,{"_id": "CSC 400","subid":[],"name":"PROBLEM SEMINAR","terms":["Fall"],"prereqs":[],"subject":"CSC","credits":4}
,{"_id": "CSC 413","subid":["BCSC 570","BME 410","CVSC 534","ECE 410","NSCI 415","OPT 410"],"name":"INTRODUCTION TO AUGMENTED AND VIRTUAL REALITY","terms":["Fall"],"prereqs":[],"subject":"CSC","credits":4}
,{"_id": "CSC 435","subid":["DSCC 435","ECE 412"],"name":"OPTIMIZATION FOR MACHINE LEARNING","terms":["Fall"],"prereqs":[],"subject":"CSC","credits":4}
,{"_id": "CSC 442","subid":["TCS 442"],"name":"ARTIFICIAL INTELLIGENCE","terms":["Fall"],"prereqs":[],"subject":"CSC","credits":4}
,{"_id": "CSC 446","subid":["ECE 409","TCS 446"],"name":"MACHINE LEARNING","terms":["Fall","Spring"],"prereqs":["MTH 165","MTH 164","CSC 242"],"subject":"CSC","credits":4}
,{"_id": "CSC 462","subid":["DSCC 462","TCS 462"],"name":"COMPUTATIONAL INTRODUCTION TO STATISTICS","terms":["Fall","Summer"],"prereqs":["THE 150","THE 142","THE 161","THE 171"],"subject":"CSC","credits":4}
,{"_id": "CSC 495","subid":[],"name":"ADVANCED RESEARCH CSC","terms":["Fall","Spring"],"prereqs":[],"subject":"CSC","credits":12}
,{"_id": "CSC 513","subid":["BCSC 572","BME 501","CVSC 572","ECE 501","NSCI 540","OPT 503"],"name":"PRACTICUM IN AUGMENTED AND VIRTUAL REALITY","terms":["Fall"],"prereqs":["ECE 410","BCSC 570","NSCI 415","CSC 413","CVSC 534"],"subject":"CSC","credits":4}
,{"_id": "CSC 890","subid":[],"name":"SUMMER IN RESIDENCE","terms":["Fall"],"prereqs":[],"subject":"CSC","credits":0}
,{"_id": "CSC 895","subid":[],"name":"CONT OF MASTER'S ENROLLMENT","terms":["Fall","Spring"],"prereqs":[],"subject":"CSC","credits":0}
,{"_id": "CSC 897","subid":[],"name":"MASTERS DISSERTATION","terms":["Fall","Summer","Spring"],"prereqs":[],"subject":"CSC","credits":0}
,{"_id": "CSC 899","subid":[],"name":"MASTER'S DISSERTATION","terms":["Fall","Spring"],"prereqs":[],"subject":"CSC","credits":0}
,{"_id": "CSC 995","subid":[],"name":"CONT OF DOCTORAL ENROLLMENT","terms":["Fall","Summer","Spring"],"prereqs":[],"subject":"CSC","credits":0}
,{"_id": "CSC 997","subid":[],"name":"DOCTORAL DISSERTATION","terms":["Fall","Spring"],"prereqs":[],"subject":"CSC","credits":0}
,{"_id": "CSC 999","subid":[],"name":"DOCTORAL DISSERTATION","terms":["Fall","Spring"],"prereqs":[],"subject":"CSC","credits":0}
,{"_id": "CSC 161S","subid":[],"name":"INTRODUCTION TO PROGRAMMING","terms":["Summer"],"prereqs":[],"subject":"CSC","credits":4}
,{"_id": "CSC 162","subid":["DSCC 162"],"name":"DATA STRUCTURES &AMP; ALGORITHMS IN PYTHON","terms":["Summer"],"prereqs":["CSC 161","MTH 150"],"subject":"CSC","credits":4}
,{"_id": "CSC 990","subid":[],"name":"SUMMER IN RESIDENCE","terms":["Summer"],"prereqs":[],"subject":"CSC","credits":0}
,{"_id": "CSC 186","subid":[],"name":"VIDEO GAME DEVELOPMENT","terms":["Spring"],"prereqs":[],"subject":"CSC","credits":4}
,{"_id": "CSC 200","subid":["CSC 200H"],"name":"UNDERGRADUATE PROBLEM SEMINAR","terms":["Spring"],"prereqs":[],"subject":"CSC","credits":4}
,{"_id": "CSC 210","subid":[],"name":"WEB PROGRAMMING","terms":["Spring"],"prereqs":["THE 199","CSC 172"],"subject":"CSC","credits":4}
,{"_id": "CSC 243","subid":["BCSC 257","BCSC 557","CSC 443","NSCI 257"],"name":"ADVANCED COMPUTATIONAL NEUROSCIENCE","terms":["Spring"],"prereqs":["CSC 241"],"subject":"CSC","credits":4}
,{"_id": "CSC 249","subid":["BCSC 236","BCSC 536","CSC 449","ECE 449","TCS 449"],"name":"MACHINE VISION","terms":["Spring"],"prereqs":["CSC 449","MTH 161","CSC 242","MTH 165"],"subject":"CSC","credits":4}
,{"_id": "CSC 250","subid":["CSC 450","LING 250","LING 450"],"name":"DATA SCIENCE FOR LINGUISTICS","terms":["Spring"],"prereqs":["LING 110","LING 210","LING 220","LING 225"],"subject":"CSC","credits":4}
,{"_id": "CSC 255","subid":["CSC 455","ECE 455","TCS 455"],"name":"SOFTWARE ANALYSIS &AMP; IMPROV","terms":["Spring"],"prereqs":["CSC 252","CSC 254"],"subject":"CSC","credits":4}
,{"_id": "CSC 258","subid":["CSC 458","TCS 458"],"name":"PARALLEL &AMP; DISTRIBUTED SYSTEMS","terms":["Spring"],"prereqs":["CSC 252","CSC 254","CSC 256"],"subject":"CSC","credits":4}
,{"_id": "CSC 260","subid":["CSC 460"],"name":"TECHNOLOGY &AMP; CLIMATE CHANGE","terms":["Spring"],"prereqs":["CSC 242"],"subject":"CSC","credits":4}
,{"_id": "CSC 263","subid":["CSC 463","DSCC 263","DSCC 463"],"name":"DATA MANAGEMENT SYSTEMS","terms":["Spring"],"prereqs":["CSC 173","CSC 252","CSC 261"],"subject":"CSC","credits":4}
,{"_id": "CSC 266","subid":["CSC 466"],"name":"FRONTIERS IN DEEP LEARNING","terms":["Spring"],"prereqs":[],"subject":"CSC","credits":4}
,{"_id": "CSC 278","subid":["CSC 478","TCS 478"],"name":"COMPUTER SECURITY FOUNDATIONS","terms":["Spring"],"prereqs":["CSC 252","CSC 452","ECE 200"],"subject":"CSC","credits":4}
,{"_id": "CSC 286","subid":["CSC 486","TCS 486"],"name":"COMPUTATIONAL COMPLEXITY","terms":["Spring"],"prereqs":["CSC 280"],"subject":"CSC","credits":4}
,{"_id": "CSC 289","subid":["CSC 489"],"name":"ALGORITHMIC GAME THEORY","terms":["Spring"],"prereqs":[],"subject":"CSC","credits":4}
,{"_id": "CSC 295","subid":[],"name":"QUANTUM COMPUTING SEMINAR","terms":["Spring"],"prereqs":[],"subject":"CSC","credits":4}
,{"_id": "CSC 392","subid":[],"name":"PRACTICUM","terms":["Spring"],"prereqs":[],"subject":"CSC","credits":0}
,{"_id": "CSC 402","subid":["DSCC 442","ECE 442"],"name":"NETWORK SCIENCE ANALYSIS","terms":["Spring"],"prereqs":["SPAN 164","SPAN 165"],"subject":"CSC","credits":4}
,{"_id": "CSC 404","subid":["ECE 204","ECE 404","TEE 404"],"name":"MULTIPROCESSOR ARCH","terms":["Spring"],"prereqs":["ECE 200","CSC 252"],"subject":"CSC","credits":4}
,{"_id": "CSC 414","subid":["BCSC 571","BME 413","CVSC 535","ECE 411","NSCI 416","OPT 438"],"name":"SELECTED TOPICS IN AUGMENTED AND VIRTUAL REALITY","terms":["Spring"],"prereqs":["THE 202","ECE 410","NSCI 415","CSC 413","CVSC 534"],"subject":"CSC","credits":4}
,{"_id": "CSC 491","subid":[],"name":"INDEPENDENT STUDY","terms":["Spring"],"prereqs":[],"subject":"CSC","credits":2}
,{"_id": "CSC 494","subid":[],"name":"MASTERS INTERNSHIP","terms":["Spring"],"prereqs":[],"subject":"CSC","credits":1}
,{"_id": "CSC 494T","subid":[],"name":"MASTER'S TRANSITNAL INTNSHP","terms":["Spring"],"prereqs":[],"subject":"CSC","credits":0}
,{"_id": "CSC 495A","subid":[],"name":"MASTERS RESEARCH IN ABSENTIA","terms":["Spring"],"prereqs":[],"subject":"CSC","credits":6}
,{"_id": "CSC 577","subid":[],"name":"ADVANCED TOPICS IN COMPUTER VISION","terms":["Spring"],"prereqs":[],"subject":"CSC","credits":4}
,{"_id": "CSC 579","subid":[],"name":"MACHINE-CHECKED PROOFS USING COQ","terms":["Spring"],"prereqs":[],"subject":"CSC","credits":2}
,{"_id": "CSC 594","subid":[],"name":"INTERNSHIP","terms":["Spring"],"prereqs":[],"subject":"CSC","credits":1}
,{"_id": "CSC 595","subid":[],"name":"PHD RESEARCH IN CSC","terms":["Spring"],"prereqs":[],"subject":"CSC","credits":16}
,{"_id": "CSC 595A","subid":[],"name":"PHD RESEARCH IN ABSENTIA","terms":["Spring"],"prereqs":[],"subject":"CSC","credits":15}
,{"_id": "CSC 595B","subid":[],"name":"PHD RESEARCH IN ABSENTIA ABROAD","terms":["Spring"],"prereqs":[],"subject":"CSC","credits":12}
,{"_id": "CSC 597","subid":[],"name":"COMPUTER SCIENCE COLLOQUIUM","terms":["Spring"],"prereqs":[],"subject":"CSC","credits":0}
,{"_id": "CSC 897A","subid":[],"name":"MASTERS DISSRTTN IN ABSENTIA","terms":["Spring"],"prereqs":[],"subject":"CSC","credits":0}
,{"_id": "CSC 899A","subid":[],"name":"MASTERS DISSERTATION IN ABSENTIA","terms":["Spring"],"prereqs":[],"subject":"CSC","credits":0}
,{"_id": "CSC 997A","subid":[],"name":"DOCT DISSERTATN IN ABSENTIA","terms":["Spring"],"prereqs":[],"subject":"CSC","credits":0}
,{"_id": "CTSC 299","subid":["CTSC 299W"],"name":"RESEARCH SEMINAR IN TRANSLATIONAL SCIENCES","terms":["Fall","Spring"],"prereqs":[],"subject":"CTSC","credits":4}
,{"_id": "CTSC 393H","subid":[],"name":"CTS RESEARCH HONORS","terms":["Fall"],"prereqs":[],"subject":"CTSC","credits":4}
,{"_id": "CVSC 110","subid":["BCSC 110","PSYC 110"],"name":"NEURAL FOUNDATIONS OF BEHAVIOR","terms":["Fall","Summer","Spring"],"prereqs":[],"subject":"CVSC","credits":4}
,{"_id": "CVSC 151","subid":["BCSC 151","PSYC 151"],"name":"PERCEPTION &AMP; ACTION","terms":["Fall"],"prereqs":["BCSC 110","BCSC 111"],"subject":"CVSC","credits":4}
,{"_id": "CVSC 241","subid":["BCSC 241","BCSC 541","NSC 541","NSCI 241"],"name":"NEURONS, CIRCUITS, &AMP; SYSTEMS","terms":["Fall"],"prereqs":["BCSC 240","NSCI 201"],"subject":"CVSC","credits":4}
,{"_id": "CVSC 245","subid":["BCSC 245","NSCI 245"],"name":"SENSORY &AMP; MOTOR NEUROSCIENCE","terms":["Fall"],"prereqs":["NSCI 201","BCSC 240"],"subject":"CVSC","credits":4}
,{"_id": "CVSC 528","subid":["BCSC 528"],"name":"SPECIAL TOPICS IN VISION","terms":["Fall","Spring"],"prereqs":[],"subject":"CVSC","credits":4}
,{"_id": "CVSC 534","subid":["BCSC 570","BME 410","CSC 413","ECE 410","NSCI 415","OPT 410"],"name":"INTRODUCTION TO AUGMENTED AND VIRTUAL REALITY","terms":["Fall"],"prereqs":[],"subject":"CVSC","credits":4}
,{"_id": "CVSC 572","subid":["BCSC 572","BME 501","CSC 513","ECE 501","NSCI 540","OPT 503"],"name":"PRACTICUM IN AUGMENTED AND VIRTUAL REALITY","terms":["Fall"],"prereqs":["ECE 410","BCSC 570","NSCI 415","CSC 413","CVSC 534"],"subject":"CVSC","credits":4}
,{"_id": "CVSC 208","subid":["BCSC 208","PSYC 208"],"name":"LAB IN PERCEPTION &AMP; COGNITION","terms":["Spring"],"prereqs":["STAT 212","BCSC 151","BCSC 153"],"subject":"CVSC","credits":4}
,{"_id": "CVSC 504","subid":["BCSC 504"],"name":"SENSORY SYSTEMS","terms":["Spring"],"prereqs":[],"subject":"CVSC","credits":4}
,{"_id": "CVSC 535","subid":["BCSC 571","BME 413","CSC 414","ECE 411","NSCI 416","OPT 438"],"name":"SELECTED TOPICS IN AUGMENTED AND VIRTUAL REALITY","terms":["Spring"],"prereqs":["THE 202","ECE 410","NSCI 415","CSC 413","CVSC 534"],"subject":"CVSC","credits":4}
,{"_id": "DANC 104","subid":[],"name":"CONTACT IMPROVISATION I","terms":["Fall"],"prereqs":[],"subject":"DANC","credits":2}
,{"_id": "DANC 106","subid":[],"name":"PILATES LAB","terms":["Fall","Spring"],"prereqs":[],"subject":"DANC","credits":1}
,{"_id": "DANC 114","subid":[],"name":"INTRODUCTION TO YOGA","terms":["Fall","Spring"],"prereqs":[],"subject":"DANC","credits":2}
,{"_id": "DANC 116","subid":[],"name":"INTRO TO SOMATIC BALLET","terms":["Fall"],"prereqs":[],"subject":"DANC","credits":2}
,{"_id": "DANC 130","subid":[],"name":"CONDITIONING FOR DANCER &AMP; ATHLETE","terms":["Fall"],"prereqs":[],"subject":"DANC","credits":2}
,{"_id": "DANC 140","subid":[],"name":"TAP DANCE:BEGINNING","terms":["Fall"],"prereqs":[],"subject":"DANC","credits":2}
,{"_id": "DANC 145","subid":[],"name":"BEGINNING JAZZ DANCE","terms":["Fall"],"prereqs":[],"subject":"DANC","credits":2}
,{"_id": "DANC 160","subid":[],"name":"DANCE IMPROVISATION","terms":["Fall"],"prereqs":[],"subject":"DANC","credits":2}
,{"_id": "DANC 170","subid":[],"name":"EMBODIED RESOURCING THROUGH SOMATIC PRACTICES","terms":["Fall"],"prereqs":[],"subject":"DANC","credits":4}
,{"_id": "DANC 171","subid":["AAAS 171"],"name":"CAPOEIRA:BRAZILIAN ART MOVEMENT","terms":["Fall"],"prereqs":[],"subject":"DANC","credits":2}
,{"_id": "DANC 181","subid":["AAAS 254"],"name":"WEST AFRICAN DANCE FORMS I","terms":["Fall"],"prereqs":[],"subject":"DANC","credits":2}
,{"_id": "DANC 188","subid":["AAAS 188"],"name":"HIP HOP CULTURE &AMP; BREAKING","terms":["Fall"],"prereqs":[],"subject":"DANC","credits":2}
,{"_id": "DANC 200","subid":[],"name":"ANATOMY AND KINESIOLOGY","terms":["Fall"],"prereqs":[],"subject":"DANC","credits":4}
,{"_id": "DANC 202","subid":[],"name":"DANCE &AMP; PEACEBUILDING","terms":["Fall"],"prereqs":[],"subject":"DANC","credits":4}
,{"_id": "DANC 208","subid":[],"name":"TAI CHI: MOVEMENT ART &AMP; CULTURE","terms":["Fall"],"prereqs":[],"subject":"DANC","credits":2}
,{"_id": "DANC 209","subid":[],"name":"QI GONG WAY TO HEALTH","terms":["Fall"],"prereqs":[],"subject":"DANC","credits":2}
,{"_id": "DANC 212","subid":["AAAS 210","MUSC 210","MUSC 410"],"name":"NGOMA:DRUM, DANCE, S AFRICA","terms":["Fall"],"prereqs":[],"subject":"DANC","credits":4}
,{"_id": "DANC 218","subid":[],"name":"INTO THE PRESENT MOMENT","terms":["Fall","Spring"],"prereqs":[],"subject":"DANC","credits":4}
,{"_id": "DANC 228","subid":[],"name":"DANCE HISTORY: PHILOSOPHY, AESTHETICS AND CULTURE","terms":["Fall"],"prereqs":[],"subject":"DANC","credits":4}
,{"_id": "DANC 237","subid":[],"name":"DANCE ENSEMBLE","terms":["Fall"],"prereqs":[],"subject":"DANC","credits":2}
,{"_id": "DANC 242","subid":[],"name":"LIGHTING DESIGN FOR DANCE.","terms":["Fall","Spring"],"prereqs":[],"subject":"DANC","credits":2}
,{"_id": "DANC 245","subid":["GSWS 242"],"name":"DANCE/MOVEMENT THERAPY FOUNDATIONS","terms":["Fall"],"prereqs":[],"subject":"DANC","credits":4}
,{"_id": "DANC 250A","subid":[],"name":"CONTEMPORARY DANCE: CONTEXT &AMP; PRACTICE","terms":["Fall"],"prereqs":[],"subject":"DANC","credits":4}
,{"_id": "DANC 260","subid":[],"name":"INTERDISCIPLINARY DANCE STUDIES","terms":["Fall"],"prereqs":[],"subject":"DANC","credits":2}
,{"_id": "DANC 266","subid":[],"name":"INTERMEDIATE CONTEMPORARY DANCE","terms":["Fall","Spring"],"prereqs":[],"subject":"DANC","credits":2}
,{"_id": "DANC 267","subid":[],"name":"ADVANCED CONTEMPORARY DANCE","terms":["Fall","Spring"],"prereqs":[],"subject":"DANC","credits":2}
,{"_id": "DANC 276","subid":["ENGL 279","GSWS 274","OP 280"],"name":"CONSENT IN PERFORMANCE:  ME TOO...WHERE DO WE GO FROM HERE?","terms":["Fall","Spring"],"prereqs":[],"subject":"DANC","credits":2}
,{"_id": "DANC 278","subid":[],"name":"CHOREOGRAPHY","terms":["Fall"],"prereqs":[],"subject":"DANC","credits":4}
,{"_id": "DANC 279","subid":[],"name":"DANCER AS COLLABORATOR","terms":["Fall","Spring"],"prereqs":[],"subject":"DANC","credits":1}
,{"_id": "DANC 365A","subid":[],"name":"SANSIFANYI:WEST AFRICAN DANCE &AMP; DRUM ENSEMBLE","terms":["Fall","Spring"],"prereqs":[],"subject":"DANC","credits":3}
,{"_id": "DANC 365B","subid":[],"name":"SANSIFANYI:WEST AFRICAN DANCE &AMP; DRUM ENSEMBLE","terms":["Fall","Spring"],"prereqs":["DANC 365"],"subject":"DANC","credits":3}
,{"_id": "DANC 365C","subid":[],"name":"SANSIFANYI:WEST AFRICAN DANCE &AMP; DRUM ENSEMBLE","terms":["Fall","Spring"],"prereqs":["DANC 365"],"subject":"DANC","credits":3}
,{"_id": "DANC 385","subid":[],"name":"DANCE PERFORMANCE WORKSHOP","terms":["Fall"],"prereqs":[],"subject":"DANC","credits":2}
,{"_id": "DANC 389W","subid":[],"name":"SENIOR SEMINAR A","terms":["Fall"],"prereqs":[],"subject":"DANC","credits":2}
,{"_id": "DANC 109","subid":[],"name":"COSTUME DESIGN FOR DANCE","terms":["Spring"],"prereqs":[],"subject":"DANC","credits":1}
,{"_id": "DANC 110","subid":[],"name":"BEGINNING DANCE TECHNIQUES","terms":["Spring"],"prereqs":[],"subject":"DANC","credits":2}
,{"_id": "DANC 150","subid":[],"name":"BEGINNING CONTEMPORARY DANCE TECHNIQUE","terms":["Spring"],"prereqs":[],"subject":"DANC","credits":2}
,{"_id": "DANC 187","subid":[],"name":"HIP-HOP: DANCE, CULTURE, AND HISTORY","terms":["Spring"],"prereqs":[],"subject":"DANC","credits":2}
,{"_id": "DANC 190","subid":["GSWS 190"],"name":"DANCES OF THE MIDDLE EAST: FOLKLORIC/BEDOUIN","terms":["Spring"],"prereqs":[],"subject":"DANC","credits":2}
,{"_id": "DANC 195","subid":[],"name":"WORLD DANCE:MOVEMENT AS CULTURE","terms":["Spring"],"prereqs":[],"subject":"DANC","credits":4}
,{"_id": "DANC 204","subid":[],"name":"CONTACT IMPROV &AMP; CULTURE","terms":["Spring"],"prereqs":[],"subject":"DANC","credits":4}
,{"_id": "DANC 211","subid":[],"name":"TAI CHI EXPLORATIONS","terms":["Spring"],"prereqs":[],"subject":"DANC","credits":4}
,{"_id": "DANC 225","subid":[],"name":"YOGA II","terms":["Spring"],"prereqs":[],"subject":"DANC","credits":2}
,{"_id": "DANC 230","subid":[],"name":"LIVING ANATOMY, LIVING YOGA","terms":["Spring"],"prereqs":[],"subject":"DANC","credits":4}
,{"_id": "DANC 233","subid":["DMST 230","EHUM 233","SUST 220"],"name":"CLIMATE INTERVENTIONS: PERFORMING ARTS + NEW MEDIA","terms":["Spring"],"prereqs":[],"subject":"DANC","credits":4}
,{"_id": "DANC 251","subid":[],"name":"JAZZ DANCE: CONTEXT &AMP; PRACTICE","terms":["Spring"],"prereqs":[],"subject":"DANC","credits":4}
,{"_id": "DANC 253","subid":["AAAS 234"],"name":"WEST AFRICAN DANCE: CONTEXT &AMP; PRACTICE","terms":["Spring"],"prereqs":[],"subject":"DANC","credits":4}
,{"_id": "DANC 268","subid":[],"name":"INTERMEDIATE CONTEMPORARY BALLET","terms":["Spring"],"prereqs":[],"subject":"DANC","credits":2}
,{"_id": "DANC 269","subid":[],"name":"ADVANCED CONTEMPORARY BALLET","terms":["Spring"],"prereqs":["DANC 268","DANC 252"],"subject":"DANC","credits":2}
,{"_id": "DANC 271","subid":[],"name":"CAPOEIRA II: MUSIC IN MOTION","terms":["Spring"],"prereqs":[],"subject":"DANC","credits":2}
,{"_id": "DANC 296","subid":[],"name":"ART OF TEACHING DANCE","terms":["Spring"],"prereqs":[],"subject":"DANC","credits":4}
,{"_id": "DANC 305","subid":[],"name":"DANCE AND INTERDEPENDENT COMMUNITY","terms":["Spring"],"prereqs":[],"subject":"DANC","credits":4}
,{"_id": "DANC 360W","subid":[],"name":"SENIOR SEMINAR","terms":["Spring"],"prereqs":[],"subject":"DANC","credits":4}
,{"_id": "DANC 377","subid":[],"name":"CHOR VOICE:DANCE &AMP; PHYSICS","terms":["Spring"],"prereqs":[],"subject":"DANC","credits":4}
,{"_id": "DANC 510","subid":[],"name":"CHOREOGRAPHIC VOICE: DANCE AND PHYSICS FRONTIERS","terms":["Spring"],"prereqs":[],"subject":"DANC","credits":2}
,{"_id": "DMST 101","subid":[],"name":"INTRO DIGITAL MEDIA STUDIES","terms":["Fall","Spring"],"prereqs":[],"subject":"DMST","credits":4}
,{"_id": "DMST 102","subid":[],"name":"PROGRAMMING DIGITAL MEDIA","terms":["Fall","Spring"],"prereqs":[],"subject":"DMST","credits":4}
,{"_id": "DMST 103","subid":[],"name":"ESSNTL DIGITAL MEDIA TOOLKIT","terms":["Fall","Spring"],"prereqs":[],"subject":"DMST","credits":4}
,{"_id": "DMST 104","subid":[],"name":"DESIGN IN THE DIGITAL AGE","terms":["Fall","Spring"],"prereqs":[],"subject":"DMST","credits":4}
,{"_id": "DMST 111","subid":["FMST 205","SART 151"],"name":"NEW MEDIA AND EMERGING PRACTICE","terms":["Fall","Spring"],"prereqs":[],"subject":"DMST","credits":4}
,{"_id": "DMST 112","subid":["SART 141"],"name":"INTRODUCTION TO PHOTOGRAPHY","terms":["Fall","Summer"],"prereqs":[],"subject":"DMST","credits":4}
,{"_id": "DMST 115","subid":[],"name":"VIDEO GAMES AS INTERACTIVE STORYTELLING","terms":["Fall"],"prereqs":[],"subject":"DMST","credits":4}
,{"_id": "DMST 120","subid":[],"name":"VIDEO GAME DESIGN","terms":["Fall"],"prereqs":[],"subject":"DMST","credits":4}
,{"_id": "DMST 121","subid":["AME 191","MUSC 191"],"name":"ART AND TECH OF RECORDING","terms":["Fall","Spring"],"prereqs":[],"subject":"DMST","credits":4}
,{"_id": "DMST 122","subid":["AME 192","MUSC 192"],"name":"LISTENING AND AUDIO PROD","terms":["Fall","Spring"],"prereqs":["AME 191"],"subject":"DMST","credits":4}
,{"_id": "DMST 123","subid":["AME 193","MUSC 193"],"name":"SOUND DESIGN","terms":["Fall","Spring"],"prereqs":[],"subject":"DMST","credits":4}
,{"_id": "DMST 153","subid":["AAAS 154","EHUM 153","FMST 153","MUSC 173","SART 153"],"name":"INTRODUCTION TO SOUND ART","terms":["Fall"],"prereqs":[],"subject":"DMST","credits":4}
,{"_id": "DMST 171","subid":[],"name":"GRAPHIC DESIGN 1","terms":["Fall"],"prereqs":[],"subject":"DMST","credits":4}
,{"_id": "DMST 260","subid":["WRTG 260"],"name":"WRITING ACROSS TECHNOLOGIES","terms":["Fall"],"prereqs":[],"subject":"DMST","credits":4}
,{"_id": "DMST 372","subid":[],"name":"CAPSTONE","terms":["Fall"],"prereqs":["DMST 200"],"subject":"DMST","credits":4}
,{"_id": "DMST 390","subid":[],"name":"SUPERVISED TEACHING - DMST 120","terms":["Fall"],"prereqs":[],"subject":"DMST","credits":4}
,{"_id": "DMST 394","subid":[],"name":"INTERNSHIP","terms":["Fall"],"prereqs":[],"subject":"DMST","credits":4}
,{"_id": "DMST 501","subid":[],"name":"DIG HUMANITIES-MELLON GRANT","terms":["Fall","Spring"],"prereqs":[],"subject":"DMST","credits":1}
,{"_id": "DMST 110","subid":[],"name":"VIDEO GAME HISTORY","terms":["Spring"],"prereqs":[],"subject":"DMST","credits":4}
,{"_id": "DMST 213","subid":["DMST 213W","ENGL 380","FMST 233"],"name":"COMEDY IN FILM AND TELEVISION","terms":["Spring"],"prereqs":[],"subject":"DMST","credits":4}
,{"_id": "DMST 230","subid":["DANC 233","EHUM 233","SUST 220"],"name":"CLIMATE INTERVENTIONS: PERFORMING ARTS + NEW MEDIA","terms":["Spring"],"prereqs":[],"subject":"DMST","credits":4}
,{"_id": "DMST 250","subid":["ENGL 288","WRTG 261"],"name":"WRITING IN A DIGITAL WORLD","terms":["Spring"],"prereqs":[],"subject":"DMST","credits":4}
,{"_id": "DMST 271","subid":["AHST 282"],"name":"HISTORY OF GRAPHIC DESIGN","terms":["Spring"],"prereqs":[],"subject":"DMST","credits":4}
,{"_id": "DMST 373","subid":[],"name":"CAPSTONE: DEVELOPMENT","terms":["Spring"],"prereqs":["DMST 372"],"subject":"DMST","credits":4}
,{"_id": "DMST 391","subid":[],"name":"INDEPENDENT STUDY","terms":["Spring"],"prereqs":[],"subject":"DMST","credits":4}
,{"_id": "DSCC 201","subid":["DSCC 401"],"name":"TOOLS FOR DATA SCIENCE","terms":["Fall","Spring"],"prereqs":["CSC 161","CSC 171"],"subject":"DSCC","credits":4}
,{"_id": "DSCC 229","subid":["BCSC 229","CSC 229","DSCC 449"],"name":"COMPUTER MODELS OF PERCEPTION &AMP; COGNITION","terms":["Fall"],"prereqs":["MTH 161","MTH 162","MTH 164","MTH 165","STAT 213"],"subject":"DSCC","credits":4}
,{"_id": "DSCC 240","subid":["CSC 240"],"name":"DATA MINING","terms":["Fall","Spring"],"prereqs":["CSC 171","CSC 172","MTH 161","CSC 242","CSC 262","MTH 165"],"subject":"DSCC","credits":4}
,{"_id": "DSCC 242","subid":["BCSC 232","CSC 242"],"name":"INTRODUCTION TO ARTIFICIAL INTELLIGENCE","terms":["Fall","Spring"],"prereqs":["CSC 172","CSC 150","CSC 173"],"subject":"DSCC","credits":4}
,{"_id": "DSCC 261","subid":["CSC 261","CSC 461","DSCC 461","TCS 461"],"name":"DATABASE SYSTEMS","terms":["Fall","Summer","Spring"],"prereqs":["CSC 172","CSC 173","CSC 252"],"subject":"DSCC","credits":4}
,{"_id": "DSCC 262","subid":["CSC 262","STAT 262"],"name":"COMPUTATIONAL INTRODUCTION TO STATISTICS","terms":["Fall","Summer"],"prereqs":["SPAN 150","SPAN 142","SPAN 161","SPAN 171"],"subject":"DSCC","credits":4}
,{"_id": "DSCC 275","subid":["DSCC 475"],"name":"TIME SERIES ANALYSIS &AMP; FORECASTING IN DATA SCIENCE","terms":["Fall"],"prereqs":["THE 262","STAT 212","STAT 213","THE 165","CSC 161","DSCC 201"],"subject":"DSCC","credits":4}
,{"_id": "DSCC 383W","subid":["DSCC 483"],"name":"DATA SCIENCE CAPSTONE","terms":["Fall","Spring"],"prereqs":["SPAN 240","SPAN 440","DSCC 262","DSCC 462","STAT 212","STAT 213","DSCC 261","DSCC 461","SPAN 020","SPAN 022"],"subject":"DSCC","credits":4}
,{"_id": "DSCC 390A","subid":[],"name":"SUPERVISED TEACHING - DSCC 262","terms":["Fall"],"prereqs":[],"subject":"DSCC","credits":2}
,{"_id": "DSCC 391","subid":[],"name":"INDEPENDENT STUDY","terms":["Fall"],"prereqs":[],"subject":"DSCC","credits":4}
,{"_id": "DSCC 391W","subid":[],"name":"INDEPENDENT STUDY","terms":["Fall"],"prereqs":[],"subject":"DSCC","credits":0}
,{"_id": "DSCC 395","subid":[],"name":"INDEPENDENT RESEARCH","terms":["Fall"],"prereqs":[],"subject":"DSCC","credits":4}
,{"_id": "DSCC 395W","subid":[],"name":"INDEPENDENT RESEARCH","terms":["Fall"],"prereqs":[],"subject":"DSCC","credits":4}
,{"_id": "DSCC 420","subid":["ECE 271","ECE 440","OPT 413","TEE 440"],"name":"INTRO TO RANDOM PROCESSES","terms":["Fall"],"prereqs":["ECE 242"],"subject":"DSCC","credits":4}
,{"_id": "DSCC 435","subid":["CSC 435","ECE 412"],"name":"OPTIMIZATION FOR MACHINE LEARNING","terms":["Fall"],"prereqs":[],"subject":"DSCC","credits":4}
,{"_id": "DSCC 494","subid":[],"name":"INTERNSHIP","terms":["Fall","Summer","Spring"],"prereqs":[],"subject":"DSCC","credits":1}
,{"_id": "DSCC 895","subid":[],"name":"CONT OF MASTER'S ENROLLMENT","terms":["Fall","Spring"],"prereqs":[],"subject":"DSCC","credits":0}
,{"_id": "DSCC 897","subid":[],"name":"MASTERS DISSERTATION","terms":["Fall","Spring"],"prereqs":[],"subject":"DSCC","credits":0}
,{"_id": "DSCC 899","subid":[],"name":"MASTER'S DISSERTATION","terms":["Fall","Spring"],"prereqs":[],"subject":"DSCC","credits":0}
,{"_id": "DSCC 162","subid":["CSC 162"],"name":"DATA STRUCTURES &AMP; ALGORITHMS IN PYTHON","terms":["Summer"],"prereqs":["CSC 161","MTH 150"],"subject":"DSCC","credits":4}
,{"_id": "DSCC 202","subid":["DSCC 402"],"name":"DATA SCIENCE AT SCALE","terms":["Spring"],"prereqs":["DSCC 201","DSCC 401"],"subject":"DSCC","credits":4}
,{"_id": "DSCC 210","subid":["DMST 210","DSCC 410","ENGL 268","ENGL 468"],"name":"DIGITAL IMAGING","terms":["Spring"],"prereqs":[],"subject":"DSCC","credits":4}
,{"_id": "DSCC 263","subid":["CSC 263","CSC 463","DSCC 463"],"name":"DATA MANAGEMENT SYSTEMS","terms":["Spring"],"prereqs":["CSC 173","CSC 252","CSC 261"],"subject":"DSCC","credits":4}
,{"_id": "DSCC 491","subid":[],"name":"MASTER'S READING COURSE: TOPICS IN ML/AI FOR MEDICAL DATA ANALYTICS","terms":["Spring","Spring"],"prereqs":[],"subject":"DSCC","credits":1}
,{"_id": "DSCC 495","subid":[],"name":"MASTER'S RESEARCH","terms":["Spring"],"prereqs":[],"subject":"DSCC","credits":6}
,{"_id": "DSCC 897A","subid":[],"name":"MASTERS IN-ABSENTIA","terms":["Spring"],"prereqs":[],"subject":"DSCC","credits":0}
,{"_id": "DSCC 897B","subid":[],"name":"MASTER'S IN-ABSENTIA ABROAD","terms":["Spring"],"prereqs":[],"subject":"DSCC","credits":0}
,{"_id": "DSCC 442","subid":["CSC 402","ECE 442"],"name":"NETWORK  SCIENCE ANALYTICS","terms":["Spring"],"prereqs":["SPAN 164","SPAN 165"],"subject":"DSCC","credits":4}
,{"_id": "EAS 101","subid":["BME 101"],"name":"INTRO TO BIOMEDICAL ENGR","terms":["Fall"],"prereqs":[],"subject":"EAS","credits":4}
,{"_id": "EAS 103","subid":["AME 140","ECE 140","MUSC 141"],"name":"INTRO TO AUDIO MUSIC &AMP; ENGIN","terms":["Fall"],"prereqs":[],"subject":"EAS","credits":4}
,{"_id": "EAS 104","subid":["ME 104"],"name":"THE ENGINEERING OF BRIDGES","terms":["Fall"],"prereqs":[],"subject":"EAS","credits":4}
,{"_id": "EAS 105","subid":["OPT 101"],"name":"INTRO TO OPTICS","terms":["Fall"],"prereqs":[],"subject":"EAS","credits":4}
,{"_id": "EAS 108","subid":["ECE 101"],"name":"INTRODUCTION TO ELECTRICAL AND COMPUTER ENGINEERING","terms":["Fall"],"prereqs":[],"subject":"EAS","credits":4}
,{"_id": "EAS 141","subid":[],"name":"BASIC MECHANICAL FABRICATION","terms":["Fall","Spring"],"prereqs":[],"subject":"EAS","credits":2}
,{"_id": "EAS 241","subid":["EAS 441"],"name":"ADVANCED MECHANICAL FABRICATION","terms":["Fall"],"prereqs":[],"subject":"EAS","credits":1}
,{"_id": "EAS 392","subid":[],"name":"INDUSTRY PRACTICUM","terms":["Fall","Spring"],"prereqs":[],"subject":"EAS","credits":0}
,{"_id": "EAS 145","subid":["PHIL 120"],"name":"ETHICS OF TECHNOLOGY","terms":["Spring"],"prereqs":[],"subject":"EAS","credits":4}
,{"_id": "ECE 101","subid":["EAS 108"],"name":"INTRO TO ELECTRICAL AND COMPUTER ENGINEERING","terms":["Fall"],"prereqs":[],"subject":"ECE","credits":4}
,{"_id": "ECE 140","subid":["AME 140","EAS 103","MUSC 141"],"name":"INTRO TO AUDIO MUSIC &AMP; ENGIN","terms":["Fall"],"prereqs":["AME 140"],"subject":"ECE","credits":4}
,{"_id": "ECE 210","subid":["OPT 210"],"name":"CIRCUIT ANALYSIS FOR SYSTEM THINKING","terms":["Fall","Spring"],"prereqs":[],"subject":"ECE","credits":4}
,{"_id": "ECE 213","subid":["ECE 413"],"name":"INTRODUCTION TO HARDWARE SECURITY","terms":["Fall"],"prereqs":[],"subject":"ECE","credits":4}
,{"_id": "ECE 221","subid":[],"name":"ELECTRONIC DEVICES&AMP;CIRCUITS","terms":["Fall"],"prereqs":["ECE 113","ECE 210"],"subject":"ECE","credits":4}
,{"_id": "ECE 223","subid":["ECE 423","MSC 423","TEE 423"],"name":"SEMICONDUCTOR DEVICES","terms":["Fall"],"prereqs":["ECE 221","ECE 230"],"subject":"ECE","credits":4}
,{"_id": "ECE 230","subid":[],"name":"ELECTROMAGNETIC WAVES","terms":["Fall"],"prereqs":["TEM 165","TEM 164","TEM 122","ECE 113"],"subject":"ECE","credits":4}
,{"_id": "ECE 241","subid":[],"name":"SIGNALS","terms":["Fall"],"prereqs":["MTH 165","ECE 113","ECE 210"],"subject":"ECE","credits":4}
,{"_id": "ECE 246","subid":["ECE 446","TEE 446"],"name":"DIGITAL SIGNAL PROCESSING","terms":["Fall"],"prereqs":["ECE 241"],"subject":"ECE","credits":4}
,{"_id": "ECE 247","subid":["CSC 227","CSC 427","ECE 447","TEE 447"],"name":"INTRO TO DIP USING PYTHON","terms":["Fall"],"prereqs":["ECE 242","ECE 440","ECE 446"],"subject":"ECE","credits":4}
,{"_id": "ECE 251","subid":["BME 253","BME 453","ECE 453","PHYS 257","PHYS 467","TEB 453"],"name":"ULTRASOUND IMAGING","terms":["Fall"],"prereqs":["BME 230","ECE 241"],"subject":"ECE","credits":4}
,{"_id": "ECE 261","subid":["ECE 461"],"name":"INTRO TO VLSI","terms":["Fall"],"prereqs":["ECE 112","ECE 221"],"subject":"ECE","credits":4}
,{"_id": "ECE 270","subid":[],"name":"INTRO TO PROBABILITY","terms":["Fall"],"prereqs":[],"subject":"ECE","credits":4}
,{"_id": "ECE 271","subid":["DSCC 420","ECE 440","OPT 413","TEE 440"],"name":"INTRO TO RANDOM PROCESSES","terms":["Fall"],"prereqs":["ECE 242"],"subject":"ECE","credits":4}
,{"_id": "ECE 348","subid":[],"name":"DESIGN SEMINAR","terms":["Fall"],"prereqs":[],"subject":"ECE","credits":2}
,{"_id": "ECE 386V","subid":[],"name":"VISITING STUDENT IN ECE","terms":["Fall"],"prereqs":[],"subject":"ECE","credits":0}
,{"_id": "ECE 392","subid":[],"name":"PRACTICUM","terms":["Fall"],"prereqs":[],"subject":"ECE","credits":4}
,{"_id": "ECE 394","subid":[],"name":"INTERNSHIP","terms":["Fall"],"prereqs":[],"subject":"ECE","credits":4}
,{"_id": "ECE 396","subid":[],"name":"SPECIAL PROJECTS","terms":["Fall"],"prereqs":[],"subject":"ECE","credits":4}
,{"_id": "ECE 402","subid":[],"name":"ELECTRICAL ENGINEERING FUNDAMENTALS","terms":["Fall"],"prereqs":["MTH 161","MTH 165","PHYS 121","PHYS 122"],"subject":"ECE","credits":4}
,{"_id": "ECE 403","subid":[],"name":"ADVANCED COMPUTER ARCHITECTURE FOR MACHINE LEARNING,","terms":["Fall"],"prereqs":["ECE 208","ECE 408","ECE 200","ECE 204","ECE 404","ECE 440"],"subject":"ECE","credits":4}
,{"_id": "ECE 405","subid":[],"name":"ISING MACHINES: PRINCIPLES AND PRACTICES","terms":["Fall"],"prereqs":[],"subject":"ECE","credits":4}
,{"_id": "ECE 409","subid":["CSC 446","TCS 446"],"name":"MACHINE LEARNING","terms":["Fall","Spring"],"prereqs":["MTH 165","MTH 164","CSC 242","CSC 446","CSC 246"],"subject":"ECE","credits":4}
,{"_id": "ECE 410","subid":["BCSC 570","BME 410","CSC 413","CVSC 534","NSCI 415","OPT 410"],"name":"INTRODUCTION TO AUGMENTED AND VIRTUAL REALITY","terms":["Fall"],"prereqs":[],"subject":"ECE","credits":4}
,{"_id": "ECE 426","subid":["OPT 468","TEO 468"],"name":"INTEGRATED PHOTONICS","terms":["Fall"],"prereqs":[],"subject":"ECE","credits":4}
,{"_id": "ECE 429","subid":["AME 223"],"name":"AUDIO ELECTRONICS","terms":["Fall"],"prereqs":[],"subject":"ECE","credits":4}
,{"_id": "ECE 436","subid":["MSC 437","OPT 464","TEE 436"],"name":"NANOPHOTONIC DEVICES","terms":["Fall","Spring"],"prereqs":["ECE 230","ECE 235","ECE 435","OPT 262","OPT 462","OPT 468","OPT 223","OPT 412","SPAN 237","SPAN 407"],"subject":"ECE","credits":4}
,{"_id": "ECE 439","subid":[],"name":"ELECTROACOUSTICS, AUDIO REPRODUCTION, AND SPATIAL AUDIO","terms":["Fall"],"prereqs":["ECE 433","ECE 429"],"subject":"ECE","credits":4}
,{"_id": "ECE 452","subid":[],"name":"MEDICAL IMAGING - THEORY &AMP; IMPLEMENTATION","terms":["Fall"],"prereqs":["ECE 242"],"subject":"ECE","credits":4}
,{"_id": "ECE 454","subid":[],"name":"QUANTUM INFORMATION PROCESSING","terms":["Fall"],"prereqs":["MTH 165","PHYS 122"],"subject":"ECE","credits":4}
,{"_id": "ECE 468","subid":[],"name":"ADVANCED ANALOG CMOS","terms":["Fall"],"prereqs":["ECE 113","ECE 221","ECE 222","ECE 246","ECE 446","ECE 467"],"subject":"ECE","credits":4}
,{"_id": "ECE 470","subid":[],"name":"DIGITAL AUDIO EFFECTS","terms":["Fall"],"prereqs":[],"subject":"ECE","credits":4}
,{"_id": "ECE 476","subid":["AME 264","TEE 476"],"name":"AUDIO SOFTWARE DEV II","terms":["Fall"],"prereqs":["AME 262","ECE 475"],"subject":"ECE","credits":4}
,{"_id": "ECE 477","subid":["AME 277","CSC 264","CSC 464","ECE 277","TEE 477"],"name":"COMPUTER AUDITION","terms":["Fall"],"prereqs":["ECE 246","ECE 446","ECE 272","ECE 472"],"subject":"ECE","credits":4}
,{"_id": "ECE 481","subid":[],"name":"CLINICAL IMAGING I","terms":["Fall"],"prereqs":[],"subject":"ECE","credits":4}
,{"_id": "ECE 496","subid":[],"name":"SPECIAL PROJECTS IN ECE","terms":["Fall","Spring"],"prereqs":[],"subject":"ECE","credits":6}
,{"_id": "ECE 501","subid":["BCSC 572","BME 501","CSC 513","CVSC 572","NSCI 540","OPT 503"],"name":"PRACTICUM IN AUGMENTED AND VIRTUAL REALITY","terms":["Fall"],"prereqs":["ECE 410","BCSC 570","NSCI 415","CSC 413","CVSC 534"],"subject":"ECE","credits":4}
,{"_id": "ECE 597","subid":[],"name":"ECE COLLOQUIUM","terms":["Fall","Spring"],"prereqs":[],"subject":"ECE","credits":0}
,{"_id": "ECE 895","subid":[],"name":"CONT OF MASTER'S ENROLLMENT","terms":["Fall","Spring"],"prereqs":[],"subject":"ECE","credits":0}
,{"_id": "ECE 995","subid":[],"name":"CONT OF DOCTORAL ENROLLMENT","terms":["Fall","Spring"],"prereqs":[],"subject":"ECE","credits":0}
,{"_id": "ECE 999","subid":[],"name":"DOCTORAL DISSERTATION","terms":["Fall","Spring"],"prereqs":[],"subject":"ECE","credits":0}
,{"_id": "ECE 495","subid":[],"name":"MASTER'S RESEARCH IN ECE","terms":["Summer"],"prereqs":[],"subject":"ECE","credits":12}
,{"_id": "ECE 594","subid":[],"name":"PHD RESEARCH INTERNSHIP","terms":["Summer","Spring"],"prereqs":[],"subject":"ECE","credits":1}
,{"_id": "ECE 594T","subid":[],"name":"PHD TRANSITIONAL INTERNSHIP","terms":["Summer","Spring"],"prereqs":[],"subject":"ECE","credits":0}
,{"_id": "ECE 595","subid":[],"name":"PHD RESEARCH IN ECE","terms":["Summer"],"prereqs":[],"subject":"ECE","credits":12}
,{"_id": "ECE 890","subid":[],"name":"SUMMER IN RESIDENCE - MASTER'S","terms":["Summer"],"prereqs":[],"subject":"ECE","credits":0}
,{"_id": "ECE 990","subid":[],"name":"SUMMER IN RESIDENCE","terms":["Summer"],"prereqs":[],"subject":"ECE","credits":0}
,{"_id": "ECE 997","subid":[],"name":"DOCTORAL DISSERTATION","terms":["Summer"],"prereqs":[],"subject":"ECE","credits":0}
,{"_id": "ECE 112","subid":[],"name":"LOGIC DESIGN","terms":["Spring"],"prereqs":["THE 162","THE 141","THE 171"],"subject":"ECE","credits":4}
,{"_id": "ECE 113","subid":[],"name":"CIRCUITS &AMP; SIGNALS","terms":["Spring"],"prereqs":[],"subject":"ECE","credits":4}
,{"_id": "ECE 114","subid":[],"name":"INTRO TO C/C++ PROGRAMMING","terms":["Spring"],"prereqs":[],"subject":"ECE","credits":4}
,{"_id": "ECE 200","subid":["ECE 400"],"name":"COMPUTER ORGANIZATION","terms":["Spring"],"prereqs":["ECE 114","ECE 112","CSC 171"],"subject":"ECE","credits":4}
,{"_id": "ECE 204","subid":["CSC 404","ECE 404","TEE 404"],"name":"MULTIPROCESSOR ARCH","terms":["Spring"],"prereqs":[],"subject":"ECE","credits":4}
,{"_id": "ECE 208","subid":["ECE 408","TEE 408"],"name":"THE ART OF MACHINE LEARNING","terms":["Spring"],"prereqs":["ECE 114","MTH 165","ECE 270"],"subject":"ECE","credits":4}
,{"_id": "ECE 217","subid":["ECE 417"],"name":"ROBOT MOTION PLANNING AND MANIPULATION","terms":["Spring"],"prereqs":["ECE 216"],"subject":"ECE","credits":4}
,{"_id": "ECE 222","subid":[],"name":"INTEGCIRCUITS:DEGSN&AMP;ANALYSIS","terms":["Spring"],"prereqs":["ECE 221"],"subject":"ECE","credits":4}
,{"_id": "ECE 233","subid":["AME 233","ECE 433","PHYS 233","TEE 433"],"name":"MUSICAL ACOUSTICS","terms":["Spring"],"prereqs":["THE 165","THE 164","THE 121"],"subject":"ECE","credits":4}
,{"_id": "ECE 248","subid":["EESC 225","EESC 425"],"name":"SEISMIC SIGNALS &AMP; NOISE","terms":["Spring"],"prereqs":["THE 121"],"subject":"ECE","credits":4}
,{"_id": "ECE 272","subid":["AME 272","ECE 472","TEE 472"],"name":"AUDIO SIG PROC FOR ANALYSIS","terms":["Spring"],"prereqs":[],"subject":"ECE","credits":4}
,{"_id": "ECE 280","subid":[],"name":"UNCERTAINTIES SCI PUZZLES","terms":["Spring"],"prereqs":[],"subject":"ECE","credits":2}
,{"_id": "ECE 349","subid":[],"name":"ECE DESIGN CAPSTONE","terms":["Spring"],"prereqs":[],"subject":"ECE","credits":4}
,{"_id": "ECE 411","subid":["BCSC 571","BME 413","CSC 414","CVSC 535","NSCI 416","OPT 438"],"name":"SELECTED TOPICS IN AUGMENTED AND VIRTUAL REALITY","terms":["Spring"],"prereqs":["THE 202","ECE 410","NSCI 415","CSC 413","CVSC 534"],"subject":"ECE","credits":4}
,{"_id": "ECE 421","subid":["MSC 470","OPT 421","TEO 421"],"name":"OPT PROPERTIES OF MATERIALS","terms":["Spring"],"prereqs":[],"subject":"ECE","credits":4}
,{"_id": "ECE 442","subid":["CSC 402","DSCC 442"],"name":"NETWORK SCIENCE ANALYTICS","terms":["Spring"],"prereqs":["SPAN 164","SPAN 165"],"subject":"ECE","credits":4}
,{"_id": "ECE 449","subid":["BCSC 236","BCSC 536","CSC 249","CSC 449","TCS 449"],"name":"MACHINE VISION","terms":["Spring"],"prereqs":["CSC 449","MTH 161","CSC 242","MTH 165"],"subject":"ECE","credits":4}
,{"_id": "ECE 455","subid":["CSC 255","CSC 455","TCS 455"],"name":"SOFT ANALY &AMP; IMPROV","terms":["Spring"],"prereqs":["CSC 252","CSC 254"],"subject":"ECE","credits":4}
,{"_id": "ECE 473","subid":["AME 197"],"name":"AUDIO FOR GAMING","terms":["Spring"],"prereqs":["AME 193","AME 194"],"subject":"ECE","credits":2}
,{"_id": "ECE 475","subid":["AME 262","TEE 475"],"name":"AUDIO SOFTWARE DESIGN","terms":["Spring"],"prereqs":["ECE 114"],"subject":"ECE","credits":4}
,{"_id": "ECE 480","subid":["AME 293"],"name":"ADVANCED AUDIO AMPLIFIER DESIGN","terms":["Spring"],"prereqs":["AME 295"],"subject":"ECE","credits":4}
,{"_id": "ECE 489","subid":[],"name":"MASTER'S RESEARCH SEMINAR IN AUDIO/ACOUSTICS","terms":["Spring"],"prereqs":[],"subject":"ECE","credits":1}
,{"_id": "ECE 491","subid":[],"name":"MASTER'S READING COURSE ECE","terms":["Spring"],"prereqs":[],"subject":"ECE","credits":5}
,{"_id": "ECE 492","subid":[],"name":"CLASS D AMPLIFIER DESIGN","terms":["Spring"],"prereqs":["AME 483"],"subject":"ECE","credits":2}
,{"_id": "ECE 495B","subid":[],"name":"MS RSRCH IN ABSENTIA ABROAD","terms":["Spring"],"prereqs":[],"subject":"ECE","credits":12}
,{"_id": "ECE 520","subid":[],"name":"SPIN BASED ELECTRONICS","terms":["Spring"],"prereqs":[],"subject":"ECE","credits":4}
,{"_id": "ECE 595A","subid":[],"name":"PHD RESEARCH IN ABSENTIA","terms":["Spring"],"prereqs":[],"subject":"ECE","credits":12}
,{"_id": "ECE 897A","subid":[],"name":"MASTER'S DISS IN ABSENTIA","terms":["Spring"],"prereqs":[],"subject":"ECE","credits":0}
,{"_id": "ECE 897B","subid":[],"name":"MASTER'S IN ABSENTIA","terms":["Spring"],"prereqs":[],"subject":"ECE","credits":0}
,{"_id": "ECE 997A","subid":[],"name":"DOCT DISSERTATN IN ABSENTIA","terms":["Spring"],"prereqs":[],"subject":"ECE","credits":0}
,{"_id": "ECE 999A","subid":[],"name":"DOCT DISSERTATN IN ABSENTIA","terms":["Spring"],"prereqs":[],"subject":"ECE","credits":0}
,{"_id": "ECON 108","subid":[],"name":"PRINCIPLES OF ECONOMICS","terms":["Fall","Spring"],"prereqs":[],"subject":"ECON","credits":4}
,{"_id": "ECON 207","subid":[],"name":"INTERMEDIATE MICROECONOMICS","terms":["Fall","Summer","Spring"],"prereqs":["ECON 108"],"subject":"ECON","credits":4}
,{"_id": "ECON 208W","subid":[],"name":"TOPICS IN MICROECON THEORY","terms":["Fall"],"prereqs":[],"subject":"ECON","credits":4}
,{"_id": "ECON 209","subid":[],"name":"INTERMEDIATE MACROECONOMICS","terms":["Fall","Summer","Spring"],"prereqs":[],"subject":"ECON","credits":4}
,{"_id": "ECON 211","subid":["ECON 211W"],"name":"MONEY, CREDIT &AMP; BANKING","terms":["Fall"],"prereqs":[],"subject":"ECON","credits":4}
,{"_id": "ECON 214","subid":["ECON 214W","STR 203"],"name":"ECONOMIC THEORY OF ORGANIZATIONS","terms":["Fall","Spring"],"prereqs":[],"subject":"ECON","credits":4}
,{"_id": "ECON 230","subid":[],"name":"ECONOMIC STATISTICS","terms":["Fall","Summer"],"prereqs":[],"subject":"ECON","credits":4}
,{"_id": "ECON 231W","subid":[],"name":"ECONOMETRICS","terms":["Fall","Spring"],"prereqs":["MTH 141","MTH 161","MTH 171","ECON 207","ECON 230","STAT 213","STAT 203","STAT 262"],"subject":"ECON","credits":4}
,{"_id": "ECON 237","subid":["ECON 237W"],"name":"ECONOMICS OF EDUCATION","terms":["Fall","Spring"],"prereqs":[],"subject":"ECON","credits":4}
,{"_id": "ECON 238","subid":["ECON 238W","SUST 238"],"name":"ENVIRONMENTAL ECONOMICS","terms":["Fall"],"prereqs":[],"subject":"ECON","credits":4}
,{"_id": "ECON 241","subid":["ECON 241W","STR 241"],"name":"PRICING STRATEGY","terms":["Fall"],"prereqs":["THE 207","MKT 203"],"subject":"ECON","credits":4}
,{"_id": "ECON 270","subid":["ECON 270W"],"name":"INTERNATIONAL MACROECONOMICS","terms":["Fall"],"prereqs":[],"subject":"ECON","credits":4}
,{"_id": "ECON 271","subid":["ECON 271W"],"name":"BEHAVIORAL ECONOMICS","terms":["Fall"],"prereqs":[],"subject":"ECON","credits":4}
,{"_id": "ECON 288","subid":["ECON 288W","PSCI 288"],"name":"GAME THEORY","terms":["Fall","Spring"],"prereqs":[],"subject":"ECON","credits":4}
,{"_id": "ECON 389W","subid":[],"name":"SENIOR SEMINAR","terms":["Fall"],"prereqs":[],"subject":"ECON","credits":4}
,{"_id": "ECON 390","subid":[],"name":"TEACHING ASSISTANT ECON 108","terms":["Fall"],"prereqs":[],"subject":"ECON","credits":4}
,{"_id": "ECON 394","subid":[],"name":"INTERNSHIP","terms":["Fall"],"prereqs":[],"subject":"ECON","credits":4}
,{"_id": "ECON 471","subid":[],"name":"MODERN VALUE THEORY I","terms":["Fall"],"prereqs":[],"subject":"ECON","credits":4}
,{"_id": "ECON 475","subid":[],"name":"MACROECONOMICS","terms":["Fall"],"prereqs":[],"subject":"ECON","credits":4}
,{"_id": "ECON 481","subid":[],"name":"INTRO TO MATH ECONOMICS","terms":["Fall"],"prereqs":[],"subject":"ECON","credits":4}
,{"_id": "ECON 484","subid":[],"name":"MATH STATS/ECONOMETRICS","terms":["Fall"],"prereqs":[],"subject":"ECON","credits":4}
,{"_id": "ECON 491","subid":[],"name":"MASTER'S READINGS IN ECON","terms":["Fall","Spring"],"prereqs":[],"subject":"ECON","credits":4}
,{"_id": "ECON 493","subid":[],"name":"MASTER'S ESSAY","terms":["Fall","Spring"],"prereqs":[],"subject":"ECON","credits":4}
,{"_id": "ECON 502","subid":[],"name":"DISCRETE CHOICE MODELS","terms":["Fall"],"prereqs":[],"subject":"ECON","credits":2}
,{"_id": "ECON 504","subid":[],"name":"TOPICS IN APPLIED MICRO","terms":["Fall"],"prereqs":[],"subject":"ECON","credits":2}
,{"_id": "ECON 507","subid":[],"name":"THEORY WORKSHOP I","terms":["Fall"],"prereqs":[],"subject":"ECON","credits":5}
,{"_id": "ECON 511","subid":[],"name":"INTERNATIONAL TRADE I","terms":["Fall"],"prereqs":[],"subject":"ECON","credits":2}
,{"_id": "ECON 512","subid":[],"name":"INTERNATIONAL TRADE II","terms":["Fall"],"prereqs":[],"subject":"ECON","credits":2}
,{"_id": "ECON 521","subid":[],"name":"ADVANCED ECONOMIC THEORY I","terms":["Fall"],"prereqs":[],"subject":"ECON","credits":4}
,{"_id": "ECON 524","subid":[],"name":"GAME THEORY &AMP; ECON MECH","terms":["Fall"],"prereqs":[],"subject":"ECON","credits":4}
,{"_id": "ECON 531","subid":[],"name":"MACROECONOMIC WORKSHOP","terms":["Fall"],"prereqs":[],"subject":"ECON","credits":5}
,{"_id": "ECON 534","subid":[],"name":"TOPICS IN MACROECONOMICS","terms":["Fall","Spring"],"prereqs":[],"subject":"ECON","credits":2}
,{"_id": "ECON 547","subid":[],"name":"ECONOMETRICS WORKSHOP","terms":["Fall"],"prereqs":[],"subject":"ECON","credits":5}
,{"_id": "ECON 551","subid":[],"name":"APPLIED ECONOMICS WORKSHOP","terms":["Fall"],"prereqs":[],"subject":"ECON","credits":5}
,{"_id": "ECON 571","subid":[],"name":"READINGS IN MACROECONOMICS","terms":["Fall","Spring"],"prereqs":[],"subject":"ECON","credits":2}
,{"_id": "ECON 572","subid":[],"name":"READINGS IN GAME THEORY","terms":["Fall","Spring"],"prereqs":[],"subject":"ECON","credits":2}
,{"_id": "ECON 573","subid":[],"name":"READINGS APPLIED ECONOMICS","terms":["Fall","Spring"],"prereqs":[],"subject":"ECON","credits":2}
,{"_id": "ECON 578","subid":[],"name":"READINGS IN INTL ECONOMICS","terms":["Fall","Spring"],"prereqs":[],"subject":"ECON","credits":2}
,{"_id": "ECON 588","subid":[],"name":"PROF ECONOMIC COMMUNICATION","terms":["Fall"],"prereqs":[],"subject":"ECON","credits":2}
,{"_id": "ECON 594","subid":[],"name":"RESEARCH INTERNSHIP","terms":["Fall","Summer","Spring"],"prereqs":[],"subject":"ECON","credits":0}
,{"_id": "ECON 595","subid":[],"name":"PHD RESEARCH IN ECONOMICS","terms":["Fall","Spring"],"prereqs":[],"subject":"ECON","credits":12}
,{"_id": "ECON 895","subid":[],"name":"CONT OF MASTER'S ENROLLMENT","terms":["Fall","Spring"],"prereqs":[],"subject":"ECON","credits":0}
,{"_id": "ECON 897","subid":[],"name":"MASTER'S DISSERTATION","terms":["Fall","Spring"],"prereqs":[],"subject":"ECON","credits":0}
,{"_id": "ECON 897B","subid":[],"name":"MASTER'S DISSERTATION IN ABSENTIA","terms":["Fall","Spring"],"prereqs":[],"subject":"ECON","credits":0}
,{"_id": "ECON 995","subid":[],"name":"CONT OF DOCTORAL ENROLLMENT","terms":["Fall","Spring"],"prereqs":[],"subject":"ECON","credits":0}
,{"_id": "ECON 997","subid":[],"name":"DOCTORAL DISSERTATION","terms":["Fall","Spring"],"prereqs":[],"subject":"ECON","credits":0}
,{"_id": "ECON 986V","subid":[],"name":"FULL TIME VISITING STUDENT","terms":["Summer","Spring"],"prereqs":[],"subject":"ECON","credits":0}
,{"_id": "ECON 990","subid":[],"name":"SUMMER IN RESIDENCE","terms":["Summer"],"prereqs":[],"subject":"ECON","credits":0}
,{"_id": "ECON 207H","subid":[],"name":"HONORS INTERMEDIATE MICRO","terms":["Spring"],"prereqs":[],"subject":"ECON","credits":4}
,{"_id": "ECON 220W","subid":[],"name":"FAIR ALLOCATION","terms":["Spring"],"prereqs":[],"subject":"ECON","credits":4}
,{"_id": "ECON 224","subid":["ECON 224W"],"name":"ECONOMICS OF SPORTS","terms":["Spring"],"prereqs":[],"subject":"ECON","credits":4}
,{"_id": "ECON 225","subid":["ECON 225W"],"name":"FREAKONOMICS","terms":["Spring"],"prereqs":[],"subject":"ECON","credits":4}
,{"_id": "ECON 236","subid":[],"name":"HEALTH ECONOMICS","terms":["Spring"],"prereqs":[],"subject":"ECON","credits":4}
,{"_id": "ECON 263","subid":["ECON 263W"],"name":"PUBLIC FINANCE","terms":["Spring"],"prereqs":[],"subject":"ECON","credits":4}
,{"_id": "ECON 268","subid":["ECON 268W"],"name":"ECONOMICS OF GLOBALIZATION","terms":["Spring"],"prereqs":["THE 190","ECON 108"],"subject":"ECON","credits":4}
,{"_id": "ECON 289W","subid":[],"name":"ECO RESEARCH AND COMM","terms":["Spring"],"prereqs":["ECON 207","ECON 231"],"subject":"ECON","credits":4}
,{"_id": "ECON 472","subid":[],"name":"MODERN VALUE THEORY","terms":["Spring"],"prereqs":[],"subject":"ECON","credits":4}
,{"_id": "ECON 476","subid":[],"name":"MACROECONOMICS II","terms":["Spring"],"prereqs":[],"subject":"ECON","credits":4}
,{"_id": "ECON 482","subid":[],"name":"MATH ECONOMICS","terms":["Spring"],"prereqs":[],"subject":"ECON","credits":2}
,{"_id": "ECON 485","subid":[],"name":"INTRO TO ECONOMETRICS I","terms":["Spring"],"prereqs":[],"subject":"ECON","credits":2}
,{"_id": "ECON 486","subid":[],"name":"INTRO TO ECONOMETRICS II","terms":["Spring"],"prereqs":[],"subject":"ECON","credits":2}
,{"_id": "ECON 487","subid":[],"name":"APPLIED ECONOMETRICS","terms":["Spring"],"prereqs":[],"subject":"ECON","credits":2}
,{"_id": "ECON 492","subid":[],"name":"MATHEMATICAL ECONOMICS III","terms":["Spring"],"prereqs":[],"subject":"ECON","credits":2}
,{"_id": "ECON 503","subid":[],"name":"LABOR ECONOMICS II","terms":["Spring"],"prereqs":[],"subject":"ECON","credits":2}
,{"_id": "ECON 508","subid":[],"name":"THEORY WORKSHOP II","terms":["Spring"],"prereqs":[],"subject":"ECON","credits":5}
,{"_id": "ECON 513","subid":[],"name":"INTERNATIONAL ECONOMICS I","terms":["Spring"],"prereqs":[],"subject":"ECON","credits":2}
,{"_id": "ECON 532","subid":[],"name":"MACROECONOMICS WORKSHOP II","terms":["Spring"],"prereqs":[],"subject":"ECON","credits":5}
,{"_id": "ECON 536","subid":[],"name":"TOPICS IN MACROECONOMICS III","terms":["Spring"],"prereqs":[],"subject":"ECON","credits":2}
,{"_id": "ECON 541","subid":[],"name":"TOPICS IN MICROECONOMETRICS I","terms":["Spring"],"prereqs":[],"subject":"ECON","credits":2}
,{"_id": "ECON 543","subid":[],"name":"TOPICS IN MACROECONOMETRICS I","terms":["Spring"],"prereqs":[],"subject":"ECON","credits":2}
,{"_id": "ECON 544","subid":[],"name":"TOPICS IN MACROECONOMETRICS II","terms":["Spring"],"prereqs":[],"subject":"ECON","credits":2}
,{"_id": "ECON 548","subid":[],"name":"ECONOMETRICS WORKSHOP II","terms":["Spring"],"prereqs":[],"subject":"ECON","credits":5}
,{"_id": "ECON 552","subid":[],"name":"APPLIED WORKSHOP II","terms":["Spring"],"prereqs":[],"subject":"ECON","credits":5}
,{"_id": "ECON 591","subid":[],"name":"PHD READINGS IN ECONOMICS","terms":["Spring"],"prereqs":[],"subject":"ECON","credits":10}
,{"_id": "ECON 997A","subid":[],"name":"DOCTORAL DISSERTATION IN ABSENTIA","terms":["Spring"],"prereqs":[],"subject":"ECON","credits":0}
,{"_id": "ECON 999","subid":[],"name":"DOCTORAL DISSERTATION","terms":["Spring"],"prereqs":[],"subject":"ECON","credits":0}
,{"_id": "ECON 999A","subid":[],"name":"DOCT DISSERTATN IN ABSENTIA","terms":["Spring"],"prereqs":[],"subject":"ECON","credits":0}
,{"_id": "ECON 999B","subid":[],"name":"PHD IN-ABSENTIA ABROAD","terms":["Spring"],"prereqs":[],"subject":"ECON","credits":0}
,{"_id": "EESC 101","subid":["SUST 101"],"name":"INTRODUCTION TO EARTH SCIENCES","terms":["Fall"],"prereqs":[],"subject":"EESC","credits":4}
,{"_id": "EESC 105","subid":[],"name":"INTRO TO CLIMATE CHANGE","terms":["Fall"],"prereqs":[],"subject":"EESC","credits":4}
,{"_id": "EESC 203","subid":["EESC 203W"],"name":"SEDIMENTOLOGY &AMP; STRATIGRAPHY","terms":["Fall"],"prereqs":[],"subject":"EESC","credits":4}
,{"_id": "EESC 205","subid":["EESC 405"],"name":"SOLID EARTH GEOPHYSICS","terms":["Fall"],"prereqs":[],"subject":"EESC","credits":4}
,{"_id": "EESC 209","subid":["EESC 209W"],"name":"INTRO GEOCHEMISTRY","terms":["Fall"],"prereqs":[],"subject":"EESC","credits":4}
,{"_id": "EESC 212","subid":["EESC 412"],"name":"CLIM.CHNG.PERSP-CHEM OCEAN.","terms":["Fall"],"prereqs":["CHEM 131","MTH 161"],"subject":"EESC","credits":4}
,{"_id": "EESC 221","subid":[],"name":"QUAN ENV PROBLEM SOLVING","terms":["Fall"],"prereqs":[],"subject":"EESC","credits":4}
,{"_id": "EESC 224","subid":["EESC 424"],"name":"GEOPHYSICAL FLOWS","terms":["Fall"],"prereqs":["MTH 162"],"subject":"EESC","credits":4}
,{"_id": "EESC 235","subid":["EESC 435"],"name":"PHYSICAL OCEANOGRAPHY","terms":["Fall"],"prereqs":[],"subject":"EESC","credits":4}
,{"_id": "EESC 236","subid":["EESC 236W","EESC 436"],"name":"PHYSICS OF CLIMATE","terms":["Fall"],"prereqs":["PHYS 121"],"subject":"EESC","credits":4}
,{"_id": "EESC 274W","subid":["EESC 474"],"name":"PALEOCEANOGRAPHY &AMP; CLIM CHG","terms":["Fall"],"prereqs":["THE 007"],"subject":"EESC","credits":4}
,{"_id": "EESC 390","subid":[],"name":"SUPERVISED TEACHING-EESC 213","terms":["Fall"],"prereqs":[],"subject":"EESC","credits":4}
,{"_id": "EESC 390A","subid":[],"name":"SUPERVISED TEACHING-EESC 213","terms":["Fall","Spring"],"prereqs":[],"subject":"EESC","credits":2}
,{"_id": "EESC 393W","subid":[],"name":"SENIOR THESIS","terms":["Fall","Spring"],"prereqs":[],"subject":"EESC","credits":4}
,{"_id": "EESC 394","subid":[],"name":"INTERNSHIP","terms":["Fall"],"prereqs":[],"subject":"EESC","credits":4}
,{"_id": "EESC 490","subid":[],"name":"SUPERVISED COLLEGE TEACHING","terms":["Fall","Spring"],"prereqs":[],"subject":"EESC","credits":1}
,{"_id": "EESC 493","subid":[],"name":"MASTER'S ESSAY","terms":["Fall","Spring"],"prereqs":[],"subject":"EESC","credits":5}
,{"_id": "EESC 495","subid":[],"name":"MASTER'S RESEARCH IN GEOLOGY","terms":["Fall","Spring"],"prereqs":[],"subject":"EESC","credits":12}
,{"_id": "EESC 499","subid":[],"name":"RESEARCH FRONTIERS IN GEO SC","terms":["Fall","Spring"],"prereqs":[],"subject":"EESC","credits":1}
,{"_id": "EESC 505","subid":[],"name":"FIRST-YEAR PHD RESEARCH IN GEOSCIENCES","terms":["Fall","Spring"],"prereqs":[],"subject":"EESC","credits":4}
,{"_id": "EESC 595","subid":[],"name":"PHD RESEARCH IN GEOLOGY","terms":["Fall","Spring"],"prereqs":[],"subject":"EESC","credits":15}
,{"_id": "EESC 895","subid":[],"name":"CONT OF MASTER'S ENROLLMENT","terms":["Fall","Spring"],"prereqs":[],"subject":"EESC","credits":0}
,{"_id": "EESC 897","subid":[],"name":"MASTERS DISSERTATION","terms":["Fall"],"prereqs":[],"subject":"EESC","credits":0}
,{"_id": "EESC 899","subid":[],"name":"MASTER'S DISSERTATION","terms":["Fall","Spring"],"prereqs":[],"subject":"EESC","credits":0}
,{"_id": "EESC 995","subid":[],"name":"CONT OF DOCTORAL ENROLLMENT","terms":["Fall","Spring"],"prereqs":[],"subject":"EESC","credits":0}
,{"_id": "EESC 997","subid":[],"name":"DOCTORAL DISSERTATION","terms":["Fall","Summer","Spring"],"prereqs":[],"subject":"EESC","credits":0}
,{"_id": "EESC 999","subid":[],"name":"DOCTORAL DISSERTATION","terms":["Fall","Spring"],"prereqs":[],"subject":"EESC","credits":0}
,{"_id": "EESC 251","subid":[],"name":"INTRO TO GEOGRAPHIC INFO SYSTEMS","terms":["Summer","Spring"],"prereqs":[],"subject":"EESC","credits":4}
,{"_id": "EESC 100","subid":[],"name":"INTRO TO OCEANOGRAPHY","terms":["Spring"],"prereqs":[],"subject":"EESC","credits":4}
,{"_id": "EESC 103","subid":["SUST 103"],"name":"INTRO TO ENVIRONMENTAL SCIENCE","terms":["Spring"],"prereqs":[],"subject":"EESC","credits":4}
,{"_id": "EESC 201","subid":["SUST 201"],"name":"EVOLUTION OF THE EARTH","terms":["Spring"],"prereqs":[],"subject":"EESC","credits":4}
,{"_id": "EESC 204","subid":["EESC 204W","EESC 404"],"name":"EARTH MATERIALS","terms":["Spring"],"prereqs":[],"subject":"EESC","credits":4}
,{"_id": "EESC 211","subid":["EESC 211W"],"name":"NATURE'S FURY","terms":["Spring"],"prereqs":[],"subject":"EESC","credits":4}
,{"_id": "EESC 216","subid":["EESC 216W","EESC 416"],"name":"ENVIRONMENTAL GEOCHEMISTRY","terms":["Spring"],"prereqs":[],"subject":"EESC","credits":4}
,{"_id": "EESC 218","subid":["EESC 418"],"name":"INTRO TO ATMOSPHERIC CHEMISTRY","terms":["Spring"],"prereqs":[],"subject":"EESC","credits":4}
,{"_id": "EESC 223","subid":["EESC 423"],"name":"EARTH SURFACE PROCESSES: THE SCIENCE OF SCENERY","terms":["Spring"],"prereqs":[],"subject":"EESC","credits":4}
,{"_id": "EESC 225","subid":["ECE 248","EESC 425"],"name":"SEISMIC SIGNALS &AMP; NOISE","terms":["Spring"],"prereqs":["THE 121"],"subject":"EESC","credits":4}
,{"_id": "EESC 233","subid":["EESC 433"],"name":"MARINE ECOSYS&AMP;CARBN CYC MOD","terms":["Spring"],"prereqs":[],"subject":"EESC","credits":4}
,{"_id": "EESC 255","subid":["EESC 255W","EESC 455"],"name":"PLANETARY SCI-GEOL EVOLUTN","terms":["Spring"],"prereqs":[],"subject":"EESC","credits":4}
,{"_id": "EESC 298","subid":[],"name":"INTRO TO RESEARCH: ARCHEOMAGNETISM IN AFRICA","terms":["Spring"],"prereqs":[],"subject":"EESC","credits":4}
,{"_id": "EESC 310","subid":["EESC 310W","SUST 310"],"name":"SCIENCE &AMP; SUSTAINABILITY","terms":["Spring"],"prereqs":[],"subject":"EESC","credits":4}
,{"_id": "EESC 591","subid":[],"name":"PHD READINGS IN GEOLOGY","terms":["Spring"],"prereqs":[],"subject":"EESC","credits":5}
,{"_id": "EESC 594","subid":[],"name":"PHD RESEARCH INTERNSHIP","terms":["Spring"],"prereqs":[],"subject":"EESC","credits":1}
,{"_id": "EESC 595A","subid":[],"name":"PHD RESEARCH IN ABSENTIA","terms":["Spring"],"prereqs":[],"subject":"EESC","credits":9}
,{"_id": "EESC 595B","subid":[],"name":"PHD RSRCH IN ABSENTIA ABROAD","terms":["Spring"],"prereqs":[],"subject":"EESC","credits":9}
,{"_id": "EESC 997A","subid":[],"name":"DOCTORAL DISSERTATION IN ABSENTIA","terms":["Spring"],"prereqs":[],"subject":"EESC","credits":0}
,{"_id": "EESC 999A","subid":[],"name":"DOCT DISSERTATN IN ABSENTIA","terms":["Spring"],"prereqs":[],"subject":"EESC","credits":0}
,{"_id": "EHUM 103","subid":["PHIL 103","SUST 114"],"name":"MORAL PROBLEMS","terms":["Fall","Spring"],"prereqs":[],"subject":"EHUM","credits":4}
,{"_id": "EHUM 153","subid":["AAAS 154","DMST 153","FMST 153","MUSC 173","SART 153"],"name":"INTRODUCTION TO SOUND ART","terms":["Fall"],"prereqs":[],"subject":"EHUM","credits":4}
,{"_id": "EHUM 213","subid":["AAAS 213","GSWS 213","GSWS 213W"],"name":"POLITICS OF NATURE: GENDER, RACE, AND THE ENVIRONMENT","terms":["Fall"],"prereqs":[],"subject":"EHUM","credits":4}
,{"_id": "EHUM 245","subid":["AAAS 245","ENGL 212","FMST 274","SUST 245"],"name":"RACE, COLONIALISM, AND NATURE (FORMERLY ENVIRONMENTAL LITERATURE)","terms":["Fall"],"prereqs":[],"subject":"EHUM","credits":4}
,{"_id": "EHUM 258","subid":["FMST 252","SART 252A","SART 252B","SART 252C","SUST 252"],"name":"NEW MEDIA AND EMERGING PRACTICES: ART ENVIRONMENT ACTION","terms":["Fall"],"prereqs":[],"subject":"EHUM","credits":4}
,{"_id": "EHUM 268","subid":["ENGL 310","FMST 275","SUST 241"],"name":"DECOLONIZING FOOD (FORMERLY FOOD MEDIA LITERATURE)","terms":["Fall"],"prereqs":[],"subject":"EHUM","credits":4}
,{"_id": "EHUM 284","subid":["AAAS 285","GSWS 285","RELC 284"],"name":"CIVIL DISOBEDIENCE","terms":["Fall"],"prereqs":[],"subject":"EHUM","credits":4}
,{"_id": "EHUM 301","subid":["HIST 300W","HIST 400"],"name":"HISTORY OF NATURE","terms":["Fall"],"prereqs":[],"subject":"EHUM","credits":4}
,{"_id": "EHUM 107","subid":["ITAL 107"],"name":"ITALIAN IN ITALY","terms":["Summer"],"prereqs":[],"subject":"EHUM","credits":4}
,{"_id": "EHUM 157","subid":["ITAL 157"],"name":"ITALIAN IN ITALY","terms":["Summer"],"prereqs":[],"subject":"EHUM","credits":4}
,{"_id": "EHUM 205","subid":["ANTH 205"],"name":"THEORIES &AMP; DEBATES: CULTURE VS. ONTOLOGY","terms":["Spring"],"prereqs":[],"subject":"EHUM","credits":4}
,{"_id": "EHUM 232","subid":["ANTH 232"],"name":"INDIGENOUS PEOPLE'S MOVEMENT","terms":["Spring"],"prereqs":[],"subject":"EHUM","credits":4}
,{"_id": "EHUM 233","subid":["DANC 233","DMST 230","SUST 220"],"name":"CLIMATE INTERVENTIONS: PERFORMING ARTS &AMP; NEW MEDIA'","terms":["Spring"],"prereqs":[],"subject":"EHUM","credits":4}
,{"_id": "EHUM 243","subid":["AAAS 221","ANTH 243","GSWS 236"],"name":"ENERGY AND POWER","terms":["Spring"],"prereqs":[],"subject":"EHUM","credits":4}
,{"_id": "EHUM 346","subid":["AHST 346","AHST 546"],"name":"ARCTIC VISION","terms":["Spring"],"prereqs":[],"subject":"EHUM","credits":4}
,{"_id": "ENGL 100","subid":[],"name":"GREAT BOOKS: MYTH AND LORE","terms":["Fall","Spring"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 101","subid":[],"name":"MAXIMUM ENGLISH","terms":["Fall"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 103","subid":[],"name":"ROCHESTER, NY","terms":["Fall"],"prereqs":["THE 196"],"subject":"ENGL","credits":4}
,{"_id": "ENGL 105","subid":[],"name":"INTRO TO RHETORIC","terms":["Fall"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 113","subid":[],"name":"BRITISH LITERATURE I","terms":["Fall"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 117","subid":["AHST 136","FMST 132"],"name":"INTRO TO THE ART OF FILM","terms":["Fall","Spring"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 121","subid":[],"name":"CREATIVE WRITING FICTION","terms":["Fall","Spring"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 122","subid":[],"name":"CREATIVE WRITING:POETRY","terms":["Fall","Spring"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 123","subid":[],"name":"PLAYWRITING: F23","terms":["Fall"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 124","subid":[],"name":"INTRO TO STAGE LIGHTING","terms":["Fall","Spring"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 126","subid":[],"name":"PRODUCTION EXPERIENCE: F23","terms":["Fall","Spring"],"prereqs":[],"subject":"ENGL","credits":1}
,{"_id": "ENGL 134","subid":[],"name":"PUBLIC SPEAKING","terms":["Fall"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 135","subid":[],"name":"INTRO TO DEBATE","terms":["Fall","Spring"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 145","subid":[],"name":"AUDITIONING FOR LIVE THEATRE AND FILM","terms":["Fall"],"prereqs":[],"subject":"ENGL","credits":2}
,{"_id": "ENGL 161","subid":["FMST 161","SART 161"],"name":"INTRODUCTION TO VIDEO ART","terms":["Fall"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 164","subid":[],"name":"IMPROVISATION","terms":["Fall"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 170","subid":[],"name":"TECHNICAL THEATER","terms":["Fall","Spring"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 172","subid":[],"name":"INTRO TO SOUND FOR THE STAGE","terms":["Fall","Spring"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 174","subid":[],"name":"ACTING TECHNIQUES","terms":["Fall","Spring"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 176","subid":[],"name":"MOVEMENT FOR THE ACTOR","terms":["Fall"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 180","subid":[],"name":"DIRECTING","terms":["Fall"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 184","subid":[],"name":"THEATRE AND CULTURAL CONTEXT","terms":["Fall"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 200","subid":["ENGL 400","LING 206","LING 406"],"name":"HISTORY OF THE ENGLISH LANGUAGE","terms":["Fall"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 205","subid":["AHST 195","CLTR 116","CLTR 253C","ENGL 405","HIST 135","ITAL 195","ITAL 220","RELC 197","RELC 285"],"name":"DANTE'S DIVINE COMEDY I","terms":["Fall"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 206","subid":[],"name":"HISTORICAL NOVELS: ANCIENT, MEDIEVAL, RENAISSANCE","terms":["Fall","Spring"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 210","subid":[],"name":"SHAKESPEARE","terms":["Fall"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 212","subid":["AAAS 245","EHUM 245","FMST 274","SUST 245"],"name":"RACE, COLONIALISM, AND NATURE (FORMERLY ENVIRONMENTAL LITERATURE)","terms":["Fall"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 213","subid":["ENGL 413"],"name":"REVENGE TRAGEDIES IN THE ENGLISH RENAISSANCE","terms":["Fall"],"prereqs":["THE 180","THE 200"],"subject":"ENGL","credits":4}
,{"_id": "ENGL 222","subid":["ENGL 422"],"name":"NINETEENTH-CENTURY BRITISH NOVEL","terms":["Fall"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 230","subid":["AAAS 230","ENGL 380","ENGL 430"],"name":"AFRICAN AMERICAN AUTOBIOGRAPHY","terms":["Fall"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 235","subid":[],"name":"20TH CENTURY DRAMA","terms":["Fall"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 236A","subid":["CLTR 277","CLTR 477","ENGL 436A","FREN 277","FREN 477","ITAL 277","ITAL 477"],"name":"POSTMODERNISM: FICTION, PHILOSOPHY, MEDIA","terms":["Fall"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 240","subid":["ENGL 440","GSWS 289","GSWS 488"],"name":"LANGUAGE IN SCIENCE AND RELIGION","terms":["Fall"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 243A","subid":["CLTR 256B","SPAN 215"],"name":"DON QUIJOTE: THE BOOK, THE MYTH, THE IMAGE","terms":["Fall"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 243M","subid":["CLTR 250","CLTR 450","RSST 240","RUSS 240"],"name":"NABOKOV- UNUSUAL �MIGR�","terms":["Fall"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 245","subid":["ENGL 445"],"name":"THE OUTSIDER IN LITERATURE","terms":["Fall","Spring"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 246","subid":[],"name":"READINGS, FEELINGS, AND WRITINGS","terms":["Fall"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 251","subid":[],"name":"EPIC ROMANCE FROM THE ODYSSEY TO THE LEGEND OF ZELDA","terms":["Fall"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 251A","subid":["AHST 284","AHST 484","FMST 244"],"name":"THE ROAD MOVIE","terms":["Fall"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 252","subid":["ENGL 452"],"name":"THEATER IN ENGLAND","terms":["Fall","Spring"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 255","subid":["AHST 252","ENGL 455","FMST 247"],"name":"FILM HISTORY: EARLY CINEMA","terms":["Fall"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 256E","subid":["CLTR 242","CLTR 442B","FMST 240","ITAL 242"],"name":"CAPITALISM, CULTURE, CONTROVERSY: THE REVOLUTIONARY CINEMA OF PIER PAOLO PASOLINI","terms":["Fall"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 257","subid":["AHST 254","AHST 454","ENGL 457","FMST 249"],"name":"FILM HISTORY:  1959-1989","terms":["Fall"],"prereqs":["SPAN 195","SPAN 198","THE 132"],"subject":"ENGL","credits":4}
,{"_id": "ENGL 258","subid":["CLTR 210","FMST 207","FMST 407","JPNS 294"],"name":"HAYAO MIYAZAKI AND PLANET GHIBLI","terms":["Fall"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 272","subid":[],"name":"ADVANCED ACTING","terms":["Fall","Spring"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 275","subid":["ENGL 475"],"name":"ADV CREATIVE WRITING:FICTION","terms":["Fall"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 279","subid":["DANC 276","GSWS 274","OP 280"],"name":"CONSENT AND PERFORMANCE","terms":["Fall","Spring"],"prereqs":[],"subject":"ENGL","credits":2}
,{"_id": "ENGL 282","subid":[],"name":"HUMOR WRITING","terms":["Fall"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 286","subid":[],"name":"PRESIDENTIAL RHETORIC","terms":["Fall","Spring"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 292","subid":[],"name":"PLAYS IN PERFORMANCE:  ORLANDO","terms":["Fall"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 294","subid":[],"name":"PLAYS IN PERFORMANCE:  OUR TOWN","terms":["Fall"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 296","subid":[],"name":"STAGE MANAGEMENT: F23","terms":["Fall"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 299","subid":[],"name":"PERFORMANCE LAB: OUR TOWN","terms":["Fall","Spring"],"prereqs":[],"subject":"ENGL","credits":1}
,{"_id": "ENGL 310","subid":["EHUM 268","FMST 275","SUST 241"],"name":"DECOLONIZING FOOD (FORMERLY FOOD MEDIA LITERATURE)","terms":["Fall"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 360","subid":[],"name":"SPECIAL PROJECTS: THEATER","terms":["Fall","Spring"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 390","subid":[],"name":"SUPERVISED TEACHING","terms":["Fall"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 392","subid":[],"name":"PRACTICUM THEATRE","terms":["Fall"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 394","subid":[],"name":"INTERNSHIP","terms":["Fall","Spring"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 394C","subid":[],"name":"WASHINGTON SEMESTR INTERNSHP","terms":["Fall","Spring"],"prereqs":[],"subject":"ENGL","credits":12}
,{"_id": "ENGL 396","subid":[],"name":"FORMS OF LITERARY CRITICISM","terms":["Fall"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 399","subid":[],"name":"WASHINGTON SEMESTER","terms":["Fall","Spring"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 469","subid":[],"name":"MUSEUM PRACTICE","terms":["Fall"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 470","subid":[],"name":"CURATORIAL THEORY &AMP; PRACTICE","terms":["Fall"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 471","subid":[],"name":"FILM CONSERVATION&AMP;RESTORATN","terms":["Fall"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 500","subid":[],"name":"GRADUATE COLLOQUIUM","terms":["Fall"],"prereqs":[],"subject":"ENGL","credits":1}
,{"_id": "ENGL 504","subid":[],"name":"FOREST AND CITY: FRAMING �NATURE� IN MEDIEVAL LITERATURE.","terms":["Fall","Spring"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 538","subid":[],"name":"19TH CENTURY AMERICAN LITERATURE IN A GLOBAL AGE:  PRACTICE AND THEORY","terms":["Fall"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 540","subid":[],"name":"MODERNISMS, OLD AND NEW","terms":["Fall"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 546","subid":[],"name":"BLACK FILM COLLECTIVES","terms":["Fall"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 571","subid":[],"name":"WRITING PEDAGOGY","terms":["Fall"],"prereqs":[],"subject":"ENGL","credits":5}
,{"_id": "ENGL 575","subid":[],"name":"FILM PRESERVATION PROJECT","terms":["Fall"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 580","subid":[],"name":"PEDAGOGICAL TRAINING","terms":["Fall","Spring"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 595","subid":[],"name":"PHD RESEARCH","terms":["Fall","Spring"],"prereqs":[],"subject":"ENGL","credits":15}
,{"_id": "ENGL 895","subid":[],"name":"CONT OF MASTER'S ENROLLMENT","terms":["Fall","Spring"],"prereqs":[],"subject":"ENGL","credits":0}
,{"_id": "ENGL 897","subid":[],"name":"MASTERS DISSERTATION","terms":["Fall","Summer","Spring"],"prereqs":[],"subject":"ENGL","credits":0}
,{"_id": "ENGL 995","subid":[],"name":"CONT OF DOCTORAL ENROLLMENT","terms":["Fall","Spring"],"prereqs":[],"subject":"ENGL","credits":0}
,{"_id": "ENGL 997","subid":[],"name":"DOCTORAL DISSERTATION","terms":["Fall","Summer","Spring"],"prereqs":[],"subject":"ENGL","credits":0}
,{"_id": "ENGL 999","subid":[],"name":"DOCTORAL DISSERTATION","terms":["Fall","Spring"],"prereqs":[],"subject":"ENGL","credits":0}
,{"_id": "ENGL 491","subid":[],"name":"MASTER'S READING COURSE","terms":["Summer","Spring"],"prereqs":[],"subject":"ENGL","credits":12}
,{"_id": "ENGL 594","subid":[],"name":"INTERNSHIP RESEARCH","terms":["Summer","Spring"],"prereqs":[],"subject":"ENGL","credits":1}
,{"_id": "ENGL 114","subid":[],"name":"BRITISH LITERATURE II","terms":["Spring"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 116","subid":["AAAS 156","GSWS 155"],"name":"INTRODUCTION TO AFRICAN AMERICAN LITERATURE","terms":["Spring"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 118","subid":["AHST 102","FMST 131"],"name":"INTRO TO MEDIA STUDIES","terms":["Spring"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 132","subid":[],"name":"FEATURE WRITING","terms":["Spring"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 133","subid":[],"name":"EDITING","terms":["Spring"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 136","subid":["WRTG 252"],"name":"PRINCIPLES &AMP; PRACTICES OF COPYEDITING","terms":["Spring"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 154","subid":[],"name":"INTRO TO DESIGN FOR STAGE","terms":["Spring"],"prereqs":[],"subject":"ENGL","credits":2}
,{"_id": "ENGL 165","subid":[],"name":"ACTING COMEDY","terms":["Spring"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 177","subid":[],"name":"THE ACTOR'S VOICE","terms":["Spring"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 201","subid":["ENGL 401","HIST 230","LING 207","LING 407"],"name":"OLD ENGLISH","terms":["Spring"],"prereqs":["THE 700","THE 110","THE 180"],"subject":"ENGL","credits":4}
,{"_id": "ENGL 204","subid":["ENGL 404"],"name":"CHAUCER","terms":["Spring"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 207","subid":[],"name":"SHAKESPEARE AND MODERNITY","terms":["Spring"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 208","subid":["ENGL 408"],"name":"RENAISSANCE DRAMA","terms":["Spring"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 211","subid":["ENGL 411"],"name":"MILTON","terms":["Spring"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 225","subid":["AAAS 256","ENGL 425","HIST 268A"],"name":"AMERICAN RENAISSANCE","terms":["Spring"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 241","subid":[],"name":"LYRIC POETRY","terms":["Spring"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 247","subid":["ENGL 447"],"name":"WHEN CULTURES MAKE CONTACT: SCIENCE FICTION AND ALLEGORIES OF SOCIAL CONFLICT","terms":["Spring"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 248","subid":["ENGL 448","GSWS 286"],"name":"CONTEMPORARY WOMEN'S WRITING","terms":["Spring"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 262","subid":["CLTR 212","ENGL 462","FMST 239","ITAL 243"],"name":"POSTWAR ITALIAN DIRECTORS: FELLINI, ANTONIONI,CAVANI","terms":["Spring"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 265","subid":["ENGL 465","FMST 226"],"name":"DOCUMENTARY FILM AND MEDIA","terms":["Spring"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 267","subid":["LTST 396","LTST 410"],"name":"INTRO TO LITERARY PUBLISHING","terms":["Spring"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 268","subid":["DMST 210","DSCC 210","DSCC 410","ENGL 468"],"name":"DIGITAL IMAGING","terms":["Spring"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 270","subid":[],"name":"ADVANCED TECHNICAL THEATRE","terms":["Spring"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 271","subid":[],"name":"ADVANCED PRODUCTION:  SOUND","terms":["Spring"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 276","subid":["ENGL 376","ENGL 476"],"name":"ADVANCED CREATIVE WRITING: POETRY","terms":["Spring"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 280","subid":[],"name":"HISTORY OF HIGH SCHOOL DEBATE IN THE US","terms":["Spring"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 281","subid":[],"name":"ADVANCED FEATURE WRITING","terms":["Spring"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 283","subid":[],"name":"LONGFORM NARRATIVES: ROCHESTER STORIES","terms":["Spring"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 284","subid":["ENGL 484","GSWS 283"],"name":"ORALITY, LANGUAGE &AMP; LITERACY","terms":["Spring"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 288","subid":["DMST 250","WRTG 261"],"name":"WRITING IN A DIGITAL WORLD","terms":["Spring"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 289","subid":["LTST 263","WRTG 263"],"name":"TRANSLATION: INTERPRETING &AMP; ADAPTING","terms":["Spring"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 293","subid":[],"name":"PLAYS IN PERFORMANCE:  THE AFRICAN COMPANY PRESENTS RICHARD III","terms":["Spring"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 295","subid":[],"name":"PLAYS IN PERFORMANCE:  METAMORPHOSES","terms":["Spring"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 297","subid":[],"name":"STAGE MANAGEMENT: S23","terms":["Spring"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 298","subid":[],"name":"PERFORMANCE LAB:  THE AFRICAN COMPANY PRESENTS RICHARD III","terms":["Spring"],"prereqs":[],"subject":"ENGL","credits":1}
,{"_id": "ENGL 309","subid":[],"name":"RACE AND RELIGION IN EARLY MODERN LITERATURE","terms":["Spring"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 391","subid":[],"name":"INDEPENDENT STUDY THEATRE","terms":["Spring"],"prereqs":[],"subject":"ENGL","credits":0}
,{"_id": "ENGL 395","subid":[],"name":"INDEPENDENT RESEARCH","terms":["Spring"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 398","subid":[],"name":"HONORS THESIS","terms":["Spring"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 429","subid":["AAAS 211","AMST 200","ENGL 242","HIST 264"],"name":"IDEAS OF AMERICA","terms":["Spring"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 438","subid":["ENGL 238"],"name":"MAKING MODERNISM NEW AGAIN","terms":["Spring"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 472","subid":[],"name":"MOVING IMAGE ARCHIVE MANAGEMENT","terms":["Spring"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 473","subid":[],"name":"LABORATORY WORK","terms":["Spring"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 474","subid":[],"name":"PERSONAL PROJECT","terms":["Spring"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 511","subid":[],"name":"LITERATURE AND VIOLENCE","terms":["Spring"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 521","subid":[],"name":"RACE AND RELIGION IN EARLY MODERN LITERATURE","terms":["Spring"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 551","subid":[],"name":"ORDINARY LITERATURE","terms":["Spring"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 572","subid":["WRTG 572"],"name":"PRACTICUM IN TEACHING OF WRITING","terms":["Spring"],"prereqs":[],"subject":"ENGL","credits":2}
,{"_id": "ENGL 573","subid":[],"name":"TEACHING APPRENTICESHIP","terms":["Spring"],"prereqs":[],"subject":"ENGL","credits":1}
,{"_id": "ENGL 574","subid":[],"name":"MOVING IMAGE PRESERVATION IN PRACTICE","terms":["Spring"],"prereqs":[],"subject":"ENGL","credits":4}
,{"_id": "ENGL 591","subid":[],"name":"PHD READINGS","terms":["Spring"],"prereqs":[],"subject":"ENGL","credits":15}
,{"_id": "ENGL 595A","subid":[],"name":"PHD RESEARCH IN ABSENTIA","terms":["Spring"],"prereqs":[],"subject":"ENGL","credits":15}
,{"_id": "ENGL 997A","subid":[],"name":"DOCT DISSERTATN IN ABSENTIA","terms":["Spring"],"prereqs":[],"subject":"ENGL","credits":0}
,{"_id": "ENGL 999A","subid":[],"name":"DOCT DISSERTATN IN ABSENTIA","terms":["Spring"],"prereqs":[],"subject":"ENGL","credits":0}
,{"_id": "ENGL 999B","subid":[],"name":"PHD IN-ABSENTIA ABROAD","terms":["Spring"],"prereqs":[],"subject":"ENGL","credits":0}
,{"_id": "ENT 101","subid":[],"name":"INTRO TO ENTREPRENEURSHIP","terms":["Fall"],"prereqs":[],"subject":"ENT","credits":4}
,{"_id": "ENT 394","subid":[],"name":"INTERNSHIP","terms":["Fall"],"prereqs":[],"subject":"ENT","credits":4}
,{"_id": "ENT 223","subid":[],"name":"PLANNING &AMP; GROWING A BUSINESS VENTURE","terms":["Spring"],"prereqs":[],"subject":"ENT","credits":4}
,{"_id": "ENT 227","subid":[],"name":"FUNDAMENTALS OF SOCIAL ENTREPRENEURSHIP","terms":["Spring"],"prereqs":[],"subject":"ENT","credits":4}
,{"_id": "FIN 205","subid":[],"name":"FINANCIAL MANAGEMENT","terms":["Fall","Spring"],"prereqs":["ECON 108"],"subject":"FIN","credits":4}
,{"_id": "FIN 213","subid":[],"name":"CORPORATE FINANCE","terms":["Fall"],"prereqs":["FIN 205","FIN 213"],"subject":"FIN","credits":4}
,{"_id": "FIN 224","subid":[],"name":"OPTIONS, FUTURE &AMP; DERIVATIVES","terms":["Fall"],"prereqs":["FIN 205","FIN 206"],"subject":"FIN","credits":4}
,{"_id": "FIN 241","subid":[],"name":"REAL ESTATE PRINCIPLES","terms":["Fall"],"prereqs":["FIN 205"],"subject":"FIN","credits":4}
,{"_id": "FIN 394","subid":[],"name":"INTERNSHIP","terms":["Fall"],"prereqs":[],"subject":"FIN","credits":4}
,{"_id": "FIN 206","subid":[],"name":"INVESTMENTS","terms":["Spring"],"prereqs":[],"subject":"FIN","credits":4}
,{"_id": "FIN 244","subid":[],"name":"ASSET MANAGEMENT","terms":["Spring"],"prereqs":[],"subject":"FIN","credits":4}
,{"_id": "FIN 246","subid":[],"name":"CRYPTOCURRENCIES, BLOCKCHAIN &AMP; FINTECH","terms":["Spring"],"prereqs":[],"subject":"FIN","credits":4}
,{"_id": "FMST 132","subid":["AHST 136","ENGL 117"],"name":"INTRO TO THE ART OF FILM","terms":["Fall","Spring"],"prereqs":[],"subject":"FMST","credits":4}
,{"_id": "FMST 153","subid":["AAAS 154","DMST 153","EHUM 153","MUSC 173","SART 153"],"name":"INTRODUCTION TO SOUND ART","terms":["Fall"],"prereqs":[],"subject":"FMST","credits":4}
,{"_id": "FMST 161","subid":["ENGL 161","SART 161"],"name":"INTRODUCTION TO VIDEO ART","terms":["Fall"],"prereqs":[],"subject":"FMST","credits":4}
,{"_id": "FMST 205","subid":["DMST 111","SART 151"],"name":"NEW MEDIA AND EMERGING PRACTICE","terms":["Fall","Spring"],"prereqs":[],"subject":"FMST","credits":4}
,{"_id": "FMST 207","subid":["CLTR 210","ENGL 258","FMST 407","JPNS 294"],"name":"HAYAO MIYAZAKI &AMP; PLANET GHIBLI","terms":["Fall"],"prereqs":[],"subject":"FMST","credits":4}
,{"_id": "FMST 209","subid":["CLTR 202B","CLTR 402B","GRMN 247","GRMN 447","JWST 219"],"name":"HOLOCAUST:  AFFECT AND ABSENCE","terms":["Fall"],"prereqs":[],"subject":"FMST","credits":4}
,{"_id": "FMST 224","subid":["AHST 277","ENGL 380","ENGL 462"],"name":"AMERICAN EXPERIMENTS","terms":["Fall"],"prereqs":[],"subject":"FMST","credits":4}
,{"_id": "FMST 236","subid":["CLTR 264E","JPNS 245"],"name":"JAPANESE SCIENCE FICTION AND PLANETARY POSSIBLE FUTURES","terms":["Fall","Spring"],"prereqs":[],"subject":"FMST","credits":4}
,{"_id": "FMST 240","subid":["CLTR 242","CLTR 442B","ENGL 256E","ITAL 242"],"name":"CAPITALISM, CULTURE, CONTROVERSY: THE REVOLUTIONARY CINEMA OF PIER PAOLO PASOLINI","terms":["Fall"],"prereqs":[],"subject":"FMST","credits":4}
,{"_id": "FMST 241","subid":["ENGL 263"],"name":"THE POLITICS OF TELEVISION","terms":["Fall"],"prereqs":[],"subject":"FMST","credits":4}
,{"_id": "FMST 244","subid":["AHST 284","AHST 484","ENGL 251A"],"name":"THE ROAD MOVIE","terms":["Fall"],"prereqs":[],"subject":"FMST","credits":4}
,{"_id": "FMST 247","subid":["AHST 252","ENGL 255","ENGL 455"],"name":"FILM HISTORY: EARLY CINEMA","terms":["Fall"],"prereqs":[],"subject":"FMST","credits":4}
,{"_id": "FMST 249","subid":["AHST 254","AHST 454","ENGL 257","ENGL 457"],"name":"FILM HISTORY:  1959-1989","terms":["Fall"],"prereqs":["THE 132"],"subject":"FMST","credits":4}
,{"_id": "FMST 252","subid":["EHUM 258","SART 252A","SART 252B","SART 252C","SUST 252"],"name":"NEW MEDIA AND EMERGING PRACTICES: ART ENVIRONMENT ACTION","terms":["Fall"],"prereqs":[],"subject":"FMST","credits":4}
,{"_id": "FMST 266","subid":["AAAS 206","ENGL 236"],"name":"BLACK ADAPATATIONS","terms":["Fall"],"prereqs":[],"subject":"FMST","credits":4}
,{"_id": "FMST 271","subid":["CLTR 264D","FMST 471","JPNS 270"],"name":"STRAIGHTJACKET SOCIETY:  JUZO ITAMI'S CINEMA","terms":["Fall"],"prereqs":["THE 198","THE 199"],"subject":"FMST","credits":4}
,{"_id": "FMST 274","subid":["AAAS 245","EHUM 245","ENGL 212","SUST 245"],"name":"RACE, COLONIALISM, AND NATURE (FORMERLY ENVIRONMENTAL LITERATURE)","terms":["Fall"],"prereqs":[],"subject":"FMST","credits":4}
,{"_id": "FMST 275","subid":["EHUM 268","ENGL 310","SUST 241"],"name":"DECOLONIZING FOOD (FORMERLY FOOD MEDIA LITERATURE)","terms":["Fall"],"prereqs":[],"subject":"FMST","credits":4}
,{"_id": "FMST 392","subid":[],"name":"PRACTICUM","terms":["Fall","Spring"],"prereqs":[],"subject":"FMST","credits":0}
,{"_id": "FMST 393","subid":[],"name":"CAPSTONE","terms":["Fall"],"prereqs":[],"subject":"FMST","credits":4}
,{"_id": "FMST 394","subid":[],"name":"INTERNSHIP","terms":["Fall"],"prereqs":[],"subject":"FMST","credits":4}
,{"_id": "FMST 219","subid":[],"name":"GENRE SCREENWRITING","terms":["Summer"],"prereqs":[],"subject":"FMST","credits":4}
,{"_id": "FMST 103","subid":["AHST 172","GSWS 100"],"name":"TOPICS IN GSWS: TV DREAMS AND GENDERED SCREENS","terms":["Spring"],"prereqs":[],"subject":"FMST","credits":4}
,{"_id": "FMST 131","subid":["AHST 102","ENGL 118"],"name":"INTRO TO MEDIA STUDIES","terms":["Spring"],"prereqs":[],"subject":"FMST","credits":4}
,{"_id": "FMST 211","subid":["AAAS 217","AHST 240","AHST 440"],"name":"AFRICAN AMERICAN CINEMA AND ITS CONTEXTS","terms":["Spring"],"prereqs":[],"subject":"FMST","credits":4}
,{"_id": "FMST 226","subid":["ENGL 265","ENGL 465"],"name":"DOCUMENTARY FILM AND MEDIA","terms":["Spring"],"prereqs":[],"subject":"FMST","credits":4}
,{"_id": "FMST 230","subid":["CLTR 248","GRMN 248","GSWS 240"],"name":"ON THE MOVE: ETHNOGRAPHIC FILMS","terms":["Spring"],"prereqs":[],"subject":"FMST","credits":4}
,{"_id": "FMST 260","subid":["ENGL 277"],"name":"SCREENWRITING","terms":["Spring"],"prereqs":[],"subject":"FMST","credits":4}
,{"_id": "FMST 261","subid":["MUSC 128"],"name":"FILM MUSIC","terms":["Spring"],"prereqs":[],"subject":"FMST","credits":4}
,{"_id": "FMST 277","subid":[],"name":"TOURIST JAPAN","terms":["Spring"],"prereqs":[],"subject":"FMST","credits":4}
,{"_id": "FREN 101","subid":[],"name":"ELEMENTARY FRENCH I","terms":["Fall","Spring"],"prereqs":[],"subject":"FREN","credits":4}
,{"_id": "FREN 102","subid":[],"name":"ELEMENTARY FRENCH II","terms":["Fall","Spring"],"prereqs":[],"subject":"FREN","credits":4}
,{"_id": "FREN 153","subid":[],"name":"INTERMEDIATE FRENCH","terms":["Fall","Spring"],"prereqs":["FREN 102"],"subject":"FREN","credits":4}
,{"_id": "FREN 155","subid":[],"name":"FRENCH CONVERSATION &AMP; COMPOSITION","terms":["Fall","Spring"],"prereqs":[],"subject":"FREN","credits":4}
,{"_id": "FREN 204","subid":[],"name":"CONTEMPORARY FRENCH CULTURE","terms":["Fall"],"prereqs":["FREN 200","FREN 204"],"subject":"FREN","credits":4}
,{"_id": "FREN 243","subid":["AAAS 303","AAAS 444","CLTR 221","CLTR 421","FREN 443","GSWS 244","GSWS 444"],"name":"MUTILATED BODIES: FROM TRADITIONS TO CUTTING-EDGE TECHNOLOGIES","terms":["Fall"],"prereqs":[],"subject":"FREN","credits":4}
,{"_id": "FREN 271","subid":["FREN 471"],"name":"INTRODUCTION TO THE FRANCOPHONE LITERATURE","terms":["Fall"],"prereqs":[],"subject":"FREN","credits":4}
,{"_id": "FREN 277","subid":["CLTR 277","CLTR 477","ENGL 236A","ENGL 436A","FREN 477","ITAL 277","ITAL 477"],"name":"POSTMODERNISM: FICTION, PHILOSOPHY, MEDIA","terms":["Fall"],"prereqs":[],"subject":"FREN","credits":4}
,{"_id": "FREN 392","subid":[],"name":"PRACTICUM","terms":["Fall","Spring"],"prereqs":[],"subject":"FREN","credits":4}
,{"_id": "FREN 157","subid":[],"name":"FRENCH IN FRANCE","terms":["Summer"],"prereqs":[],"subject":"FREN","credits":4}
,{"_id": "FREN 207","subid":[],"name":"FRENCH IN FRANCE","terms":["Summer"],"prereqs":[],"subject":"FREN","credits":4}
,{"_id": "FREN 200","subid":[],"name":"ADVANCED FRENCH","terms":["Spring"],"prereqs":["FREN 153"],"subject":"FREN","credits":4}
,{"_id": "FREN 202","subid":[],"name":"INTRODUCTION TO FRENCH LITERATURE","terms":["Spring"],"prereqs":["FREN 200"],"subject":"FREN","credits":4}
,{"_id": "FREN 212","subid":["FREN 412","LTST 231","LTST 431"],"name":"FRENCH LITERATURE IN TRANSLATION","terms":["Spring"],"prereqs":["FREN 200"],"subject":"FREN","credits":4}
,{"_id": "FREN 228","subid":["AAAS 280","AAAS 412","CLTR 229B","CLTR 429B","FREN 428"],"name":"HUMANITARIANISM AND SOCIAL INSECURITIES","terms":["Spring"],"prereqs":[],"subject":"FREN","credits":4}
,{"_id": "FREN 252","subid":["HIST 232","HIST 232W"],"name":"MODERN FRANCE: REVOLUTION, REACTION, AND REFORM","terms":["Spring"],"prereqs":[],"subject":"FREN","credits":4}
,{"_id": "FREN 257","subid":["FREN 457"],"name":"SEX, LIES, AND SECRETS: LIBERTINISM IN EARLY MODERN FRANCE","terms":["Spring"],"prereqs":[],"subject":"FREN","credits":4}
,{"_id": "FREN 296","subid":["CLTR 240A","CLTR 440A","FREN 496","TH 282","TH 482"],"name":"PHILOSOPHY OF MUSIC","terms":["Spring"],"prereqs":[],"subject":"FREN","credits":4}
,{"_id": "FREN 591","subid":[],"name":"INDEPENDENT STUDY","terms":["Spring","Spring"],"prereqs":[],"subject":"FREN","credits":3}
,{"_id": "FREN 591B","subid":[],"name":"PHD READINGS IN ABSENTIA ABROAD","terms":["Spring"],"prereqs":[],"subject":"FREN","credits":3}
,{"_id": "GRMN 151","subid":[],"name":"INTERMEDIATE GERMAN I","terms":["Fall"],"prereqs":[],"subject":"GRMN","credits":4}
,{"_id": "GRMN 200","subid":[],"name":"ADVANCED CONVERSATION &AMP; COMP","terms":["Fall"],"prereqs":[],"subject":"GRMN","credits":4}
,{"_id": "GRMN 203","subid":[],"name":"INTRO TO GERMAN LITERATURE","terms":["Fall"],"prereqs":[],"subject":"GRMN","credits":4}
,{"_id": "GRMN 212","subid":["CLTR 212","CLTR 412","FMST 236","GRMN 412"],"name":"MONSTERS,GHOSTS &AMP; ALIENS","terms":["Fall"],"prereqs":[],"subject":"GRMN","credits":4}
,{"_id": "GRMN 221","subid":["CLTR 222C","CLTR 422C","GRMN 421","GSWS 271"],"name":"GENDER, LOVE &AMP; FAMILIES","terms":["Fall"],"prereqs":[],"subject":"GRMN","credits":4}
,{"_id": "GRMN 247","subid":["CLTR 202B","CLTR 402B","FMST 209","GRMN 447","JWST 219"],"name":"HOLOCAUST:  AFFECT AND ABSENCE","terms":["Fall"],"prereqs":[],"subject":"GRMN","credits":4}
,{"_id": "GRMN 392","subid":[],"name":"PRACTICUM","terms":["Fall","Spring"],"prereqs":[],"subject":"GRMN","credits":0}
,{"_id": "GRMN 394","subid":[],"name":"INTERNSHIP","terms":["Fall"],"prereqs":[],"subject":"GRMN","credits":4}
,{"_id": "GRMN 207","subid":[],"name":"GERMAN IN GERMANY","terms":["Summer"],"prereqs":[],"subject":"GRMN","credits":4}
,{"_id": "GRMN 102","subid":[],"name":"ELEMENTARY GERMAN II","terms":["Spring"],"prereqs":[],"subject":"GRMN","credits":4}
,{"_id": "GRMN 152","subid":[],"name":"INTERMEDIATE GERMAN II","terms":["Spring"],"prereqs":[],"subject":"GRMN","credits":4}
,{"_id": "GRMN 202","subid":[],"name":"INTRODUCTION TO GERMAN STUDIES","terms":["Spring"],"prereqs":[],"subject":"GRMN","credits":4}
,{"_id": "GRMN 217","subid":["MUSC 207","RELC 287"],"name":"HILDEGARD OF BINGEN AND HER WORLD","terms":["Spring"],"prereqs":["THE 109","THE 117","THE 800"],"subject":"GRMN","credits":4}
,{"_id": "GRMN 229","subid":["CLTR 252A","GRMN 486"],"name":"KLEIST &AMP; KAFKA","terms":["Spring"],"prereqs":[],"subject":"GRMN","credits":4}
,{"_id": "GRMN 230","subid":["CLTR 242A","CLTR 442A","ENGL 232","GRMN 430"],"name":"POE AND HOFFMAN","terms":["Spring"],"prereqs":[],"subject":"GRMN","credits":4}
,{"_id": "GRMN 238","subid":["CLTR 238A","CLTR 438A","GRMN 438","GSWS 237","JWST 243"],"name":"REVOLUTIONS &AMP; REVOLT","terms":["Spring"],"prereqs":[],"subject":"GRMN","credits":4}
,{"_id": "GRMN 248","subid":["CLTR 248","FMST 230","GSWS 240"],"name":"ON THE MOVE: ETHNOGRAPHIC FILMS","terms":["Spring"],"prereqs":[],"subject":"GRMN","credits":4}
,{"_id": "GRMN 256","subid":[],"name":"ADVANCED STUDIES IN GERMAN: GERMAN GRAPHIC NOVELS","terms":["Spring"],"prereqs":[],"subject":"GRMN","credits":4}
,{"_id": "GRMN 395","subid":[],"name":"INDEPENDENT RESEARCH","terms":["Spring"],"prereqs":[],"subject":"GRMN","credits":4}
,{"_id": "GSWS 100","subid":["MUSC 107"],"name":"TOPICS IN GSWS: ROCKIN� BODS: POPULAR MUSIC, GENDER, AND THE BODY","terms":["Fall","Spring"],"prereqs":[],"subject":"GSWS","credits":4}
,{"_id": "GSWS 105","subid":[],"name":"SEX AND POWER","terms":["Fall","Spring"],"prereqs":[],"subject":"GSWS","credits":4}
,{"_id": "GSWS 115","subid":["ANTH 102"],"name":"INTRO TO MED ANTHROPOLOGY","terms":["Fall"],"prereqs":[],"subject":"GSWS","credits":4}
,{"_id": "GSWS 126","subid":[],"name":"WITCHCRAFT AND WITCH HUNTS, 1400-1800","terms":["Fall"],"prereqs":[],"subject":"GSWS","credits":4}
,{"_id": "GSWS 161","subid":["JWST 161","RELC 147"],"name":"WOMEN IN JUDAISM: RITUAL, EXPERIENCE, AND LEADERSHIP","terms":["Fall"],"prereqs":[],"subject":"GSWS","credits":4}
,{"_id": "GSWS 189","subid":["RELC 189"],"name":"SEXUALITY IN WORLD RELIGION","terms":["Fall"],"prereqs":[],"subject":"GSWS","credits":4}
,{"_id": "GSWS 212","subid":[],"name":"QUEER THEORY","terms":["Fall"],"prereqs":[],"subject":"GSWS","credits":4}
,{"_id": "GSWS 213","subid":["AAAS 213","EHUM 213","GSWS 213W"],"name":"POLITICS OF NATURE: GENDER, RACE, AND THE ENVIRONMENT","terms":["Fall"],"prereqs":[],"subject":"GSWS","credits":4}
,{"_id": "GSWS 215","subid":[],"name":"LGBTQ HISTORIES AND CULTURE","terms":["Fall","Spring"],"prereqs":[],"subject":"GSWS","credits":4}
,{"_id": "GSWS 234","subid":["AAAS 235","ANTH 235"],"name":"THE BLACK BODY","terms":["Fall"],"prereqs":[],"subject":"GSWS","credits":4}
,{"_id": "GSWS 242","subid":["DANC 245"],"name":"DANCE/MOVEMENT THERAPY FOUNDATIONS","terms":["Fall"],"prereqs":[],"subject":"GSWS","credits":4}
,{"_id": "GSWS 243","subid":["ENGL 243","ENGL 380","ENGL 443"],"name":"THE BRONTES","terms":["Fall"],"prereqs":[],"subject":"GSWS","credits":4}
,{"_id": "GSWS 244","subid":["AAAS 303","AAAS 444","CLTR 221","CLTR 421","FREN 243","FREN 443","GSWS 444"],"name":"MUTILATED BODIES: FROM TRADITIONS TO CUTTING-EDGE TECHNOLOGIES","terms":["Fall"],"prereqs":[],"subject":"GSWS","credits":4}
,{"_id": "GSWS 254","subid":["ENGL 206","ENGL 406"],"name":"MONSTROUS FEMININE IN THE MIDDLE AGES","terms":["Fall"],"prereqs":[],"subject":"GSWS","credits":4}
,{"_id": "GSWS 266","subid":["PSYC 267"],"name":"PSYCHOLOGY OF GENDER","terms":["Fall"],"prereqs":["PSYC 101"],"subject":"GSWS","credits":4}
,{"_id": "GSWS 271","subid":["CLTR 222C","CLTR 422C","GRMN 221","GRMN 421"],"name":"GENDER, LOVE &AMP; FAMILIES","terms":["Fall"],"prereqs":[],"subject":"GSWS","credits":4}
,{"_id": "GSWS 274","subid":["DANC 276","ENGL 279","OP 280"],"name":"CONSENT IN PERFORMANCE: ME TOO...WHERE DO WE GO FROM HERE?","terms":["Fall","Spring"],"prereqs":[],"subject":"GSWS","credits":2}
,{"_id": "GSWS 276","subid":["WRTG 266"],"name":"WORDS HAVE POWER: WRITING FOR SOCIAL CHANGE","terms":["Fall"],"prereqs":[],"subject":"GSWS","credits":4}
,{"_id": "GSWS 285","subid":["AAAS 285","EHUM 284","RELC 284"],"name":"CIVIL DISOBEDIENCE","terms":["Fall"],"prereqs":[],"subject":"GSWS","credits":4}
,{"_id": "GSWS 289","subid":["ENGL 240","ENGL 440","GSWS 488"],"name":"LANGUAGE IN SCIENCE AND RELIGION","terms":["Fall"],"prereqs":[],"subject":"GSWS","credits":4}
,{"_id": "GSWS 389H","subid":[],"name":"MAJOR SENIOR SEMINAR - HONORS","terms":["Fall"],"prereqs":[],"subject":"GSWS","credits":4}
,{"_id": "GSWS 392","subid":[],"name":"PRACTICUM IN WOMEN'S STUDIES","terms":["Fall"],"prereqs":[],"subject":"GSWS","credits":0}
,{"_id": "GSWS 394","subid":[],"name":"INTERNSHIP","terms":["Fall"],"prereqs":[],"subject":"GSWS","credits":4}
,{"_id": "GSWS 123","subid":["AHST 100"],"name":"INTRODUCTION TO VISUAL &AMP; CULTURAL STUDIES","terms":["Spring"],"prereqs":[],"subject":"GSWS","credits":4}
,{"_id": "GSWS 155","subid":["AAAS 156","ENGL 116"],"name":"INTRO AFRICAN-AMERICAN LITERATURE","terms":["Spring"],"prereqs":[],"subject":"GSWS","credits":4}
,{"_id": "GSWS 188","subid":["HIST 189"],"name":"WIVES, WITCHES AND WENCHES: WOMEN IN AMERICAN HISTORY","terms":["Spring"],"prereqs":[],"subject":"GSWS","credits":4}
,{"_id": "GSWS 190","subid":["DANC 190"],"name":"DANCES OF THE MIDDLE EAST: FOLKLORIC/BEDOUIN","terms":["Spring"],"prereqs":[],"subject":"GSWS","credits":2}
,{"_id": "GSWS 206","subid":["GSWS 406","PHLT 206"],"name":"GLOBAL POLITICS OF GENDER AND HEALTH","terms":["Spring"],"prereqs":[],"subject":"GSWS","credits":4}
,{"_id": "GSWS 209","subid":["PSYC 209"],"name":"PSYCHOLOGY OF HUMAN SEXUALITY","terms":["Spring"],"prereqs":["PSYC 101"],"subject":"GSWS","credits":4}
,{"_id": "GSWS 218","subid":[],"name":"GENDER AND DISABILITY","terms":["Spring"],"prereqs":[],"subject":"GSWS","credits":4}
,{"_id": "GSWS 221","subid":["CLTR 228A","ITAL 250"],"name":"WARTIME LOVE: ITALIAN NOVELS OF THE FIFTIES AND SIXTIES","terms":["Spring"],"prereqs":[],"subject":"GSWS","credits":4}
,{"_id": "GSWS 222","subid":["CHIN 222","CLTR 224"],"name":"GENDER, SEXUALITY, AND DESIRE IN 20TH CENTURY CHINESE LITERATURE","terms":["Spring"],"prereqs":[],"subject":"GSWS","credits":4}
,{"_id": "GSWS 232","subid":["GSWS 232W","HIST 284","HIST 284W"],"name":"BODY AND SEXUALITY","terms":["Spring"],"prereqs":[],"subject":"GSWS","credits":4}
,{"_id": "GSWS 233","subid":["AAAS 200","ANTH 233","PSCI 225","RELC 230"],"name":"CLTRL POLITICS PRISON TOWNS","terms":["Spring"],"prereqs":[],"subject":"GSWS","credits":4}
,{"_id": "GSWS 236","subid":["AAAS 221","ANTH 243","EHUM 243"],"name":"ENERGY AND POWER","terms":["Spring"],"prereqs":[],"subject":"GSWS","credits":4}
,{"_id": "GSWS 237","subid":["CLTR 238A","CLTR 438A","GRMN 238","GRMN 438","JWST 243"],"name":"REVOLUTIONS AND REVOLT","terms":["Spring"],"prereqs":[],"subject":"GSWS","credits":4}
,{"_id": "GSWS 240","subid":["CLTR 248","FMST 230","GRMN 248"],"name":"ON THE MOVE: ETHNOGRAPHIC FILMS","terms":["Spring"],"prereqs":[],"subject":"GSWS","credits":4}
,{"_id": "GSWS 241","subid":["AAAS 222","ANTH 240","MUSC 236","MUSC 436","PHLT 227"],"name":"MUSIC, ETHNOGRAPHY &AMP; HIV/AIDS","terms":["Spring"],"prereqs":[],"subject":"GSWS","credits":4}
,{"_id": "GSWS 282","subid":["AAAS 208","SPAN 282","SPAN 482"],"name":"SI EL NORTE FUERA EL SUR: LATINX LITERATURE AND THOUGHT","terms":["Spring"],"prereqs":["SPAN 200"],"subject":"GSWS","credits":4}
,{"_id": "GSWS 283","subid":["ENGL 284","ENGL 484"],"name":"ORALITY, LANGUAGE &AMP; LITERACY","terms":["Spring"],"prereqs":[],"subject":"GSWS","credits":4}
,{"_id": "GSWS 286","subid":["ENGL 248","ENGL 448"],"name":"CONTEMPORARY WOMEN'S WRITING","terms":["Spring"],"prereqs":[],"subject":"GSWS","credits":4}
,{"_id": "GSWS 393","subid":["GSWS 393H"],"name":"MAJOR SENIOR SEMINAR","terms":["Spring"],"prereqs":[],"subject":"GSWS","credits":4}
,{"_id": "HBRW 101","subid":["JWST 101"],"name":"ELEMENTARY MODERN HEBREW I","terms":["Fall"],"prereqs":[],"subject":"HBRW","credits":4}
,{"_id": "HBRW 103","subid":["JWST 103"],"name":"INTERMEDIATE MODERN HEBREW I","terms":["Fall"],"prereqs":[],"subject":"HBRW","credits":4}
,{"_id": "HBRW 394","subid":[],"name":"INTERNSHIP","terms":["Fall"],"prereqs":[],"subject":"HBRW","credits":0}
,{"_id": "HBRW 102","subid":["JWST 102"],"name":"ELEMENTARY MODERN HEBREW II","terms":["Spring"],"prereqs":[],"subject":"HBRW","credits":4}
,{"_id": "HBRW 104","subid":["JWST 104"],"name":"INTERMEDIATE MODERN HEBREW II","terms":["Spring"],"prereqs":[],"subject":"HBRW","credits":4}
,{"_id": "HIST 106","subid":[],"name":"WITCHCRAFT AND WITCH HUNTS, 1400-1800","terms":["Fall"],"prereqs":[],"subject":"HIST","credits":4}
,{"_id": "HIST 110","subid":["AAAS 106","ANTH 248"],"name":"THE MAKING OF MODERN AFRICA","terms":["Fall"],"prereqs":[],"subject":"HIST","credits":4}
,{"_id": "HIST 111","subid":["CLST 224"],"name":"THE GREEKS AND THE PERSIAN EMPIRE","terms":["Fall"],"prereqs":[],"subject":"HIST","credits":4}
,{"_id": "HIST 113","subid":[],"name":"AFRICAN AMERICANS IN SOUTH AFRICA","terms":["Fall"],"prereqs":[],"subject":"HIST","credits":4}
,{"_id": "HIST 121","subid":["CLST 121"],"name":"HISTORY OF THE ANCIENT ROMAN WORLD","terms":["Fall"],"prereqs":[],"subject":"HIST","credits":4}
,{"_id": "HIST 130","subid":["CLTR 209A","RSST 128","RUSS 128"],"name":"RUSSIAN CIVILIZATION: MYTH, CULTURE, HISTORY","terms":["Fall"],"prereqs":[],"subject":"HIST","credits":4}
,{"_id": "HIST 134","subid":["RSST 126","RSST 127","RUSS 126","RUSS 127"],"name":"RUSSIA NOW","terms":["Fall","Spring"],"prereqs":[],"subject":"HIST","credits":4}
,{"_id": "HIST 146","subid":["AHST 212","CLTR 208A","JPNS 210","RELC 132"],"name":"VENGEANCE, LONGING, AND SALVATION: TOPICS IN �TRADITIONAL� JAPANESE CULTURE","terms":["Fall"],"prereqs":[],"subject":"HIST","credits":4}
,{"_id": "HIST 148","subid":["CHIN 275","RELC 175"],"name":"RELIGION &AMP; CHINESE SOCIETY","terms":["Fall"],"prereqs":[],"subject":"HIST","credits":4}
,{"_id": "HIST 157","subid":[],"name":"HISTORY OF NATIVE AMERICA, 1800-PRESENT","terms":["Fall"],"prereqs":[],"subject":"HIST","credits":4}
,{"_id": "HIST 160","subid":[],"name":"CULTURE WARS IN MODERN AMERICA","terms":["Fall"],"prereqs":[],"subject":"HIST","credits":4}
,{"_id": "HIST 174","subid":[],"name":"AMERICAN MILITARY HISTORY","terms":["Fall"],"prereqs":[],"subject":"HIST","credits":4}
,{"_id": "HIST 196","subid":[],"name":"BLACK PAST LIVES MATTER: FREDERICK DOUGLASS'S ROCHESTER","terms":["Fall"],"prereqs":[],"subject":"HIST","credits":4}
,{"_id": "HIST 200","subid":[],"name":"GATEWAY: UNCLE TOM'S CABIN AND LITTLE WOMEN","terms":["Fall","Spring"],"prereqs":[],"subject":"HIST","credits":4}
,{"_id": "HIST 225","subid":["HIST 225W"],"name":"EUROPE AND THE GREAT WAR, 1914-1918","terms":["Fall"],"prereqs":[],"subject":"HIST","credits":4}
,{"_id": "HIST 240","subid":["HIST 440"],"name":"PUBLIC HISTORY: THEORY AND PRACTICE","terms":["Fall"],"prereqs":[],"subject":"HIST","credits":4}
,{"_id": "HIST 242","subid":["HIST 242W"],"name":"UNEQUAL, UNJUST: 100 YEARS OF RACISM IN US PUBLIC HEALTH","terms":["Fall"],"prereqs":[],"subject":"HIST","credits":4}
,{"_id": "HIST 245A","subid":["INTR 227"],"name":"WAR AND MEMORY IN EASTERN EUROPE","terms":["Fall"],"prereqs":[],"subject":"HIST","credits":4}
,{"_id": "HIST 251","subid":["AAAS 215","HIST 251W"],"name":"AFRICAN DIASPORA IN LATIN AMERICA, 1441-1804","terms":["Fall"],"prereqs":[],"subject":"HIST","credits":4}
,{"_id": "HIST 263","subid":["HIST 263W"],"name":"GLOBAL HISTORY OF FOOD","terms":["Fall"],"prereqs":[],"subject":"HIST","credits":4}
,{"_id": "HIST 265","subid":[],"name":"VICTORIAN BRAZIL: BRITISH-BRAZILIAN CULTURAL CONNECTIONS IN THE 19TH CENTURY","terms":["Fall"],"prereqs":[],"subject":"HIST","credits":4}
,{"_id": "HIST 268","subid":[],"name":"TOPICS: US HISTORY, POST-1800","terms":["Fall"],"prereqs":[],"subject":"HIST","credits":4}
,{"_id": "HIST 288","subid":["CLTR 247","CLTR 447A","ITAL 247"],"name":"POLITICS AND CULTURE IN FASCIST ITALY","terms":["Fall"],"prereqs":["THE 194"],"subject":"HIST","credits":4}
,{"_id": "HIST 289","subid":["HIST 289W","RELC 289"],"name":"VISIONARIES, MYSTICS, SAINTS-MEDIEVAL &AMP; RENAISSANCE EUR","terms":["Fall"],"prereqs":[],"subject":"HIST","credits":4}
,{"_id": "HIST 300W","subid":["EHUM 301","HIST 400"],"name":"HISTORY OF NATURE","terms":["Fall"],"prereqs":[],"subject":"HIST","credits":4}
,{"_id": "HIST 304W","subid":["HIST 404"],"name":"READINGS IN ATLANTIC HISTORY","terms":["Fall"],"prereqs":[],"subject":"HIST","credits":4}
,{"_id": "HIST 351W","subid":["HIST 451"],"name":"LIFE IN THE CITY: LATIN AMERICAN URBAN HISTORY","terms":["Fall"],"prereqs":[],"subject":"HIST","credits":4}
,{"_id": "HIST 382W","subid":["HIST 482"],"name":"APOCALYPSE NOW�&AMP; THEN: A HISTORY OF APOCALYPTIC THOUGHT","terms":["Fall"],"prereqs":[],"subject":"HIST","credits":4}
,{"_id": "HIST 389H","subid":[],"name":"SENIOR THESIS","terms":["Fall"],"prereqs":[],"subject":"HIST","credits":4}
,{"_id": "HIST 390","subid":[],"name":"SUPERVISED TEACHING","terms":["Fall"],"prereqs":[],"subject":"HIST","credits":4}
,{"_id": "HIST 394","subid":[],"name":"INTERNSHIP","terms":["Fall"],"prereqs":[],"subject":"HIST","credits":4}
,{"_id": "HIST 421","subid":[],"name":"TOPICS IN EARLY MODERN EUROPEAN HISTORY","terms":["Fall"],"prereqs":[],"subject":"HIST","credits":5}
,{"_id": "HIST 500","subid":[],"name":"PROBLEMS IN HISTORICAL ANALYSIS","terms":["Fall"],"prereqs":[],"subject":"HIST","credits":5}
,{"_id": "HIST 510","subid":[],"name":"ADVANCED HISTORICAL STUDIES (1CR)","terms":["Fall","Spring"],"prereqs":[],"subject":"HIST","credits":1}
,{"_id": "HIST 520","subid":[],"name":"ADVANCED HISTORICAL STUDIES II","terms":["Fall","Spring"],"prereqs":[],"subject":"HIST","credits":2}
,{"_id": "HIST 591","subid":[],"name":"PHD READINGS IN HISTORY","terms":["Fall","Fall","Spring"],"prereqs":[],"subject":"HIST","credits":5}
,{"_id": "HIST 592","subid":[],"name":"INDEPENDENT READING COURSE","terms":["Fall","Summer","Spring"],"prereqs":[],"subject":"HIST","credits":10}
,{"_id": "HIST 593","subid":[],"name":"APPRENTICE TEACHING","terms":["Fall","Spring"],"prereqs":[],"subject":"HIST","credits":0}
,{"_id": "HIST 895","subid":[],"name":"CONTINUATION OF MASTER'S ENROLLMENT","terms":["Fall","Spring"],"prereqs":[],"subject":"HIST","credits":0}
,{"_id": "HIST 995","subid":[],"name":"CONTINUATION OF DOCTORAL ENROLLMENT","terms":["Fall","Spring"],"prereqs":[],"subject":"HIST","credits":0}
,{"_id": "HIST 997B","subid":[],"name":"PHD DISSERTATION - IN ABSENTIA ABROAD","terms":["Fall","Spring"],"prereqs":[],"subject":"HIST","credits":0}
,{"_id": "HIST 137A","subid":[],"name":"HISTORY OF POLAND STUDY ABROAD","terms":["Summer"],"prereqs":[],"subject":"HIST","credits":3}
,{"_id": "HIST 997","subid":[],"name":"DOCTORAL DISSERTATION","terms":["Summer"],"prereqs":[],"subject":"HIST","credits":0}
,{"_id": "HIST 104","subid":["AHST 199","CLST 131"],"name":"ANCIENT CITIES OF THE MEDITERRANEAN","terms":["Spring"],"prereqs":[],"subject":"HIST","credits":4}
,{"_id": "HIST 112","subid":["AAAS 183","PSCI 224","RELC 183"],"name":"INCARCERATION NATION","terms":["Spring"],"prereqs":[],"subject":"HIST","credits":4}
,{"_id": "HIST 117","subid":["AHST 140","ATHS 210","CLST 134"],"name":"ARCHAEOLOGICAL THOUGHT","terms":["Spring"],"prereqs":[],"subject":"HIST","credits":4}
,{"_id": "HIST 151","subid":["CLTR 151"],"name":"MODERN LATIN AMERICA","terms":["Spring"],"prereqs":[],"subject":"HIST","credits":4}
,{"_id": "HIST 171","subid":["AAAS 142"],"name":"AFRICAN-AMERICAN HISTORY II SINCE 1900","terms":["Spring"],"prereqs":[],"subject":"HIST","credits":4}
,{"_id": "HIST 178","subid":[],"name":"HISTORIES OF INDIGENOUS WOMEN","terms":["Spring"],"prereqs":[],"subject":"HIST","credits":4}
,{"_id": "HIST 179","subid":[],"name":"ROCHESTER AND WESTERN NEW YORK","terms":["Spring"],"prereqs":[],"subject":"HIST","credits":4}
,{"_id": "HIST 189","subid":["GSWS 188"],"name":"WIVES, WITCHES, AND WENCHES: WOMEN IN AMERICAN HISTORY","terms":["Spring"],"prereqs":[],"subject":"HIST","credits":4}
,{"_id": "HIST 195","subid":[],"name":"PREMODERN JAPAN","terms":["Spring"],"prereqs":[],"subject":"HIST","credits":4}
,{"_id": "HIST 208","subid":["HIST 208W"],"name":"MODERN REVOLUTIONS - FRANCE, JAPAN, MEXICO, RUSSIA","terms":["Spring"],"prereqs":[],"subject":"HIST","credits":4}
,{"_id": "HIST 210","subid":["HIST 210W"],"name":"AFRICA WELCOMES CHINA IN A NEW GLOBAL ECONOMY","terms":["Spring"],"prereqs":[],"subject":"HIST","credits":4}
,{"_id": "HIST 220","subid":["AHST 232","ANTH 296","ATHS 212"],"name":"ART HISTORY AND ETHNOARCHAEOLOGY OF WEST AFRICA","terms":["Spring"],"prereqs":[],"subject":"HIST","credits":4}
,{"_id": "HIST 221","subid":[],"name":"MEDIEVAL CRUSADES: CONFLICTS ACROSS CULTURES","terms":["Spring"],"prereqs":[],"subject":"HIST","credits":4}
,{"_id": "HIST 226","subid":["HIST 226W"],"name":"EXPLORATION, SCIENCE, AND ADVENTURE","terms":["Spring"],"prereqs":[],"subject":"HIST","credits":4}
,{"_id": "HIST 228","subid":["AAAS 201","HIST 228W"],"name":"NORTH AFRICA AND THE MIDDLE EAST SINCE 1838","terms":["Spring"],"prereqs":[],"subject":"HIST","credits":4}
,{"_id": "HIST 230","subid":["ENGL 201","ENGL 401","LING 207","LING 407"],"name":"OLD ENGLISH","terms":["Spring"],"prereqs":["THE 700","THE 110","THE 180"],"subject":"HIST","credits":4}
,{"_id": "HIST 232","subid":["FREN 252","HIST 232W"],"name":"MODERN FRANCE: REVOLUTION, REACTION, AND REFORM","terms":["Spring"],"prereqs":[],"subject":"HIST","credits":4}
,{"_id": "HIST 252","subid":["HIST 252W","HIST 453"],"name":"IMMIGRATION AND THE AMERICAS","terms":["Spring"],"prereqs":[],"subject":"HIST","credits":4}
,{"_id": "HIST 264","subid":["AAAS 211","AMST 200","ENGL 242","ENGL 429"],"name":"THE IDEA OF AMERICA","terms":["Spring"],"prereqs":[],"subject":"HIST","credits":4}
,{"_id": "HIST 268A","subid":["AAAS 256","ENGL 225","ENGL 425"],"name":"AMERICAN RENAISSANCE","terms":["Spring"],"prereqs":[],"subject":"HIST","credits":4}
,{"_id": "HIST 280","subid":["ATHS 240","HIST 280W","HIST 497"],"name":"HISTORICAL ARCHAEOLOGY","terms":["Spring"],"prereqs":[],"subject":"HIST","credits":4}
,{"_id": "HIST 284","subid":["GSWS 232","GSWS 232W","HIST 284W"],"name":"BODY AND SEXUALITY","terms":["Spring"],"prereqs":[],"subject":"HIST","credits":4}
,{"_id": "HIST 285","subid":["ATHS 245","HIST 285W","HIST 485"],"name":"DIGITAL HISTORY: BUILDING A VIRTUAL ST. GEORGE'S","terms":["Spring"],"prereqs":[],"subject":"HIST","credits":4}
,{"_id": "HIST 296","subid":["CLST 220","CLTR 204A"],"name":"WRITING HISTORY IN ANCIENT GREECE AND ROME","terms":["Spring"],"prereqs":[],"subject":"HIST","credits":4}
,{"_id": "HIST 299H","subid":[],"name":"UR RESEARCH: HISTORY AND YOUR PROJECT","terms":["Spring"],"prereqs":[],"subject":"HIST","credits":2}
,{"_id": "HIST 327W","subid":["HIST 427"],"name":"REAL EXISTING SOCIALISM: 19TH AND 20TH CENTURY EUROPE","terms":["Spring"],"prereqs":[],"subject":"HIST","credits":4}
,{"_id": "HIST 346W","subid":["HIST 446"],"name":"EAST ASIA AND THE COLD WAR","terms":["Spring"],"prereqs":[],"subject":"HIST","credits":4}
,{"_id": "HIST 350W","subid":["HIST 450"],"name":"CAPTIVES: PAST, PRESENT, AND FUTURE (1500-2100)","terms":["Spring"],"prereqs":[],"subject":"HIST","credits":4}
,{"_id": "HIST 370W","subid":["HIST 470"],"name":"HISTORIES OF RACE AND REVOLT IN US LITERATURE AND FILM","terms":["Spring"],"prereqs":[],"subject":"HIST","credits":4}
,{"_id": "HIST 374W","subid":["HIST 474","PHLT 374","PSCI 316W"],"name":"PANDEMICS, POLITICS AND POLICIES IN THE US, 1918-2020","terms":["Spring"],"prereqs":[],"subject":"HIST","credits":4}
,{"_id": "HIST 393","subid":[],"name":"ADVANCED OR SENIOR PROJECT/SEMINAR/THESIS","terms":["Spring"],"prereqs":[],"subject":"HIST","credits":4}
,{"_id": "HIST 393H","subid":[],"name":"ADVANCED OR SENIOR PROJECT/SEMINAR/THESIS","terms":["Spring"],"prereqs":[],"subject":"HIST","credits":4}
,{"_id": "HIST 399H","subid":[],"name":"HONORS RESEARCH SEMINAR","terms":["Spring"],"prereqs":[],"subject":"HIST","credits":2}
,{"_id": "HIST 413","subid":[],"name":"HISTORY OF GLOBAL EXPLORATION","terms":["Spring"],"prereqs":[],"subject":"HIST","credits":5}
,{"_id": "HIST 420","subid":[],"name":"MEDIEVAL CRUSADES: CONFLICT ACROSS CULTURES","terms":["Spring"],"prereqs":[],"subject":"HIST","credits":5}
,{"_id": "HIST 502","subid":[],"name":"DISSERTATION WRITERS' SEMINAR","terms":["Spring"],"prereqs":[],"subject":"HIST","credits":5}
,{"_id": "HIST 595","subid":[],"name":"PHD RESEARCH IN HISTORY","terms":["Spring"],"prereqs":[],"subject":"HIST","credits":15}
,{"_id": "HIST 986V","subid":[],"name":"FULL TIME VISITING STUDENT","terms":["Spring"],"prereqs":[],"subject":"HIST","credits":0}
,{"_id": "HIST 999B","subid":[],"name":"PHD IN-ABSENTIA ABROAD","terms":["Spring"],"prereqs":[],"subject":"HIST","credits":0}
,{"_id": "INTR 101","subid":["PSCI 101"],"name":"INTRO/COMPARATIVE POLITICS","terms":["Fall"],"prereqs":[],"subject":"INTR","credits":4}
,{"_id": "INTR 106","subid":["PSCI 106"],"name":"INTRO TO INTERNATIONAL RELATIONS","terms":["Fall","Spring"],"prereqs":[],"subject":"INTR","credits":4}
,{"_id": "INTR 205","subid":["SUST 205"],"name":"GLOBAL SUSTAINABLE DEV","terms":["Fall"],"prereqs":[],"subject":"INTR","credits":4}
,{"_id": "INTR 227","subid":["HIST 245A"],"name":"WAR AND MEMORY IN EASTERN EUROPE","terms":["Fall"],"prereqs":[],"subject":"INTR","credits":4}
,{"_id": "INTR 249","subid":["INTR 249W","JWST 265","RELC 265","RELC 265W"],"name":"ISRAEL/PALESTINE","terms":["Fall"],"prereqs":[],"subject":"INTR","credits":4}
,{"_id": "INTR 264","subid":["INTR 264W","PSCI 264","PSCI 264W"],"name":"COMPARATIVE POLITICAL INSTITUTIONS","terms":["Fall"],"prereqs":[],"subject":"INTR","credits":4}
,{"_id": "INTR 265","subid":["PSCI 265"],"name":"CIVIL WAR AND THE INTERNATIONAL SYSTEM","terms":["Fall"],"prereqs":[],"subject":"INTR","credits":4}
,{"_id": "INTR 299","subid":["PSCI 299","WRTG 276"],"name":"COMMUNICATING YOUR PROFESSIONAL IDENTITY - LAW, POLICY, AND SOCIAL GOOD","terms":["Fall"],"prereqs":[],"subject":"INTR","credits":2}
,{"_id": "INTR 389W","subid":["PSCI 389W"],"name":"SENIOR HONORS SEM","terms":["Fall"],"prereqs":[],"subject":"INTR","credits":4}
,{"_id": "INTR 394","subid":[],"name":"INTERNSHIP","terms":["Fall"],"prereqs":[],"subject":"INTR","credits":4}
,{"_id": "INTR 394W","subid":[],"name":"INTERNSHIP","terms":["Fall"],"prereqs":[],"subject":"INTR","credits":4}
,{"_id": "INTR 221","subid":[],"name":"NATIONALISM, CENTRAL EUROPE, AND THE RUSSIA-UKRAINE WAR","terms":["Spring"],"prereqs":[],"subject":"INTR","credits":4}
,{"_id": "INTR 253","subid":["INTR 253W","PSCI 253","PSCI 253W"],"name":"COMPARATIVE POLITICAL PARTIES","terms":["Spring"],"prereqs":[],"subject":"INTR","credits":4}
,{"_id": "INTR 254","subid":["INTR 254W","PSCI 254","PSCI 254W"],"name":"FASCISM:  POLITICS, HISTORY, AND CULTURE","terms":["Spring"],"prereqs":[],"subject":"INTR","credits":4}
,{"_id": "INTR 260","subid":["INTR 260W","PSCI 260","PSCI 260W"],"name":"DEMOCRATIC EROSION","terms":["Spring"],"prereqs":[],"subject":"INTR","credits":4}
,{"_id": "INTR 268","subid":["INTR 268W","PSCI 268","PSCI 268W"],"name":"INTERNATIONAL ORGANIZATION","terms":["Spring"],"prereqs":[],"subject":"INTR","credits":4}
,{"_id": "INTR 373","subid":["INTR 373W","PSCI 373","PSCI 373W","PSCI 573"],"name":"TERRITORY AND GROUP CONFLICT","terms":["Spring"],"prereqs":[],"subject":"INTR","credits":4}
,{"_id": "INTR 393W","subid":["PSCI 393W"],"name":"SENIOR HONORS PROJECT","terms":["Spring"],"prereqs":[],"subject":"INTR","credits":4}
,{"_id": "ITAL 101","subid":[],"name":"ELEMENTARY ITALIAN I","terms":["Fall"],"prereqs":[],"subject":"ITAL","credits":4}
,{"_id": "ITAL 114","subid":[],"name":"CONVERSATIONAL ITALIAN","terms":["Fall","Spring"],"prereqs":[],"subject":"ITAL","credits":2}
,{"_id": "ITAL 151","subid":[],"name":"INTERMEDIATE ITALIAN I","terms":["Fall"],"prereqs":[],"subject":"ITAL","credits":4}
,{"_id": "ITAL 200","subid":[],"name":"ADVANCED ITALIAN COMPOSITION AND CONVERSATION","terms":["Fall"],"prereqs":[],"subject":"ITAL","credits":4}
,{"_id": "ITAL 242","subid":["CLTR 242","CLTR 442B","ENGL 256E","FMST 240"],"name":"CAPITALISM, CULTURE, CONTROVERSY: THE REVOLUTIONARY CINEMA OF PIER PAOLO PASOLINI","terms":["Fall"],"prereqs":[],"subject":"ITAL","credits":4}
,{"_id": "ITAL 247","subid":["CLTR 247","CLTR 447A","HIST 288"],"name":"POLITICS AND CULTURE IN FASCIST ITALY","terms":["Fall"],"prereqs":["THE 194"],"subject":"ITAL","credits":4}
,{"_id": "ITAL 277","subid":["CLTR 277","CLTR 477","ENGL 236A","ENGL 436A","FREN 277","FREN 477","ITAL 477"],"name":"POSTMODERNISM: FICTION, PHILOSOPHY, MEDIA","terms":["Fall"],"prereqs":[],"subject":"ITAL","credits":4}
,{"_id": "ITAL 107","subid":["EHUM 107"],"name":"ITALIAN IN ITALY","terms":["Summer"],"prereqs":[],"subject":"ITAL","credits":4}
,{"_id": "ITAL 157","subid":["EHUM 157"],"name":"ITALIAN IN ITALY","terms":["Summer"],"prereqs":[],"subject":"ITAL","credits":4}
,{"_id": "ITAL 102","subid":[],"name":"ELEMENTARY ITALIAN II","terms":["Spring"],"prereqs":[],"subject":"ITAL","credits":4}
,{"_id": "ITAL 152","subid":[],"name":"INTERMEDIATE ITALIAN II","terms":["Spring"],"prereqs":[],"subject":"ITAL","credits":4}
,{"_id": "ITAL 203","subid":[],"name":"INTRODUCTION TO ITALIAN LITERATURE","terms":["Spring"],"prereqs":[],"subject":"ITAL","credits":4}
,{"_id": "ITAL 243","subid":["CLTR 212","ENGL 262","ENGL 462","FMST 239"],"name":"POSTWAR ITALIAN DIRECTORS:  FELLINI, ANTONIONI, CAVANI","terms":["Spring"],"prereqs":[],"subject":"ITAL","credits":4}
,{"_id": "ITAL 250","subid":["CLTR 228A","GSWS 221"],"name":"WARTIME LOVE: ITALIAN NOVELS OF THE FIFTIES AND SIXTIES","terms":["Spring"],"prereqs":[],"subject":"ITAL","credits":4}
,{"_id": "JPNS 101","subid":[],"name":"ELEMENTARY JAPANESE I","terms":["Fall"],"prereqs":[],"subject":"JPNS","credits":6}
,{"_id": "JPNS 114","subid":[],"name":"INTERMEDIATE CONVERSATIONAL JAPANESE I","terms":["Fall"],"prereqs":[],"subject":"JPNS","credits":2}
,{"_id": "JPNS 151","subid":[],"name":"INTERMEDIATE JAPANESE I","terms":["Fall"],"prereqs":[],"subject":"JPNS","credits":6}
,{"_id": "JPNS 201","subid":[],"name":"ADV INTERMEDIATE JAPANESE I","terms":["Fall"],"prereqs":[],"subject":"JPNS","credits":4}
,{"_id": "JPNS 203","subid":[],"name":"ADV CONVERSATIONAL JPN I","terms":["Fall"],"prereqs":[],"subject":"JPNS","credits":2}
,{"_id": "JPNS 205","subid":[],"name":"ADVANCED JAPANESE I","terms":["Fall"],"prereqs":[],"subject":"JPNS","credits":4}
,{"_id": "JPNS 210","subid":["AHST 212","CLTR 208A","HIST 146","RELC 132"],"name":"VENGEANCE, LONGING, AND SALVATION: TOPICS IN �TRADITIONAL� JAPANESE CULTURE","terms":["Fall"],"prereqs":[],"subject":"JPNS","credits":4}
,{"_id": "JPNS 216","subid":["AHST 216","AHST 416","CLTR 208H","CLTR 408H","RELC 225"],"name":"CULTURES OF ENLIGHTENMENT: MEDITATION, MATERIALITY, AND THE LITERARY CULTURES OF JAPANESE BUDDHISM","terms":["Fall"],"prereqs":[],"subject":"JPNS","credits":4}
,{"_id": "JPNS 245","subid":["CLTR 264E","FMST 236"],"name":"JAPANESE SCIENCE FICTION AND PLANETARY POSSIBLE FUTURES","terms":["Fall","Spring"],"prereqs":[],"subject":"JPNS","credits":4}
,{"_id": "JPNS 270","subid":["CLTR 264D","FMST 271","FMST 471"],"name":"STRAIGHTJACKET SOCIETY:  JUZO ITAMI'S CINEMA","terms":["Fall"],"prereqs":["THE 198","THE 199"],"subject":"JPNS","credits":4}
,{"_id": "JPNS 275","subid":["AAAS 275","CLTR 275A","MUSC 275"],"name":"HIP HOP JAPAN","terms":["Fall"],"prereqs":[],"subject":"JPNS","credits":4}
,{"_id": "JPNS 294","subid":["CLTR 210","ENGL 258","FMST 207","FMST 407"],"name":"HAYAO MIYAZAKI AND PLANT GHIBLI","terms":["Fall"],"prereqs":[],"subject":"JPNS","credits":4}
,{"_id": "JPNS 392","subid":[],"name":"PRACTICUM IN JAPANESE","terms":["Fall","Spring"],"prereqs":[],"subject":"JPNS","credits":2}
,{"_id": "JPNS 102","subid":[],"name":"ELEMENTARY JAPANESE II","terms":["Spring"],"prereqs":[],"subject":"JPNS","credits":6}
,{"_id": "JPNS 115","subid":[],"name":"INTERMEDIATE CONVERSATIONAL JAPANESE II","terms":["Spring"],"prereqs":[],"subject":"JPNS","credits":2}
,{"_id": "JPNS 152","subid":[],"name":"INTERMEDIATE JAPANESE II","terms":["Spring"],"prereqs":[],"subject":"JPNS","credits":6}
,{"_id": "JPNS 202","subid":[],"name":"ADVANCED INTERMEDIATE JAPANESE II","terms":["Spring"],"prereqs":[],"subject":"JPNS","credits":4}
,{"_id": "JPNS 204","subid":[],"name":"ADVANCED CONVERSATIONAL JAPANESE II","terms":["Spring"],"prereqs":[],"subject":"JPNS","credits":2}
,{"_id": "JPNS 206","subid":[],"name":"ADVANCED JAPANESE II","terms":["Spring"],"prereqs":[],"subject":"JPNS","credits":4}
,{"_id": "JPNS 219A","subid":[],"name":"TOURIST JAPAN","terms":["Spring"],"prereqs":[],"subject":"JPNS","credits":4}
,{"_id": "JPNS 229","subid":[],"name":"JAPANESE CALLIGRAPHY &AMP; GRAPHOLOGY","terms":["Spring"],"prereqs":[],"subject":"JPNS","credits":4}
,{"_id": "JPNS 393","subid":[],"name":"SENIOR PROJECT","terms":["Spring"],"prereqs":[],"subject":"JPNS","credits":4}
,{"_id": "JWST 100","subid":["RELC 109"],"name":"INTRODUCTION TO JEWISH STUDIES","terms":["Fall"],"prereqs":[],"subject":"JWST","credits":4}
,{"_id": "JWST 101","subid":["HBRW 101"],"name":"ELEMENTARY MODERN HEBREW I","terms":["Fall"],"prereqs":[],"subject":"JWST","credits":4}
,{"_id": "JWST 103","subid":["HBRW 103"],"name":"INTERMEDIATE MODERN HEBREW I","terms":["Fall"],"prereqs":[],"subject":"JWST","credits":4}
,{"_id": "JWST 106","subid":["RELC 101"],"name":"INTRODUCTION TO THE HEBREW BIBLE","terms":["Fall"],"prereqs":[],"subject":"JWST","credits":4}
,{"_id": "JWST 136","subid":["RELC 136"],"name":"ANGELS, SACRED LETTERS, AND HOLLYWOOD: INTRODUCTION TO JEWISH MYSTICISM","terms":["Fall"],"prereqs":[],"subject":"JWST","credits":4}
,{"_id": "JWST 161","subid":["GSWS 161","RELC 147"],"name":"WOMEN IN JUDAISM: RITUAL, EXPERIENCE, AND LEADERSHIP","terms":["Fall"],"prereqs":[],"subject":"JWST","credits":4}
,{"_id": "JWST 177","subid":["RELC 177"],"name":"KITCHEN JUDAISM: JEWISH FOOD BEYOND THE BAGEL AND THE BIBLE","terms":["Fall"],"prereqs":[],"subject":"JWST","credits":4}
,{"_id": "JWST 219","subid":["CLTR 202B","CLTR 402B","FMST 209","GRMN 247","GRMN 447"],"name":"HOLOCAUST: AFFECT AND ABSENCE","terms":["Fall"],"prereqs":[],"subject":"JWST","credits":4}
,{"_id": "JWST 265","subid":["INTR 249","INTR 249W","RELC 265","RELC 265W"],"name":"ISRAEL/PALESTINE","terms":["Fall"],"prereqs":[],"subject":"JWST","credits":4}
,{"_id": "JWST 394","subid":[],"name":"INTERNSHIP","terms":["Fall"],"prereqs":[],"subject":"JWST","credits":4}
,{"_id": "JWST 102","subid":["HBRW 102"],"name":"ELEMENTARY MODERN HEBREW II","terms":["Spring"],"prereqs":[],"subject":"JWST","credits":4}
,{"_id": "JWST 104","subid":["HBRW 104"],"name":"INTERMEDIATE MODERN HEBREW II","terms":["Spring"],"prereqs":[],"subject":"JWST","credits":4}
,{"_id": "JWST 243","subid":["CLTR 238A","CLTR 438A","GRMN 238","GRMN 438","GSWS 237"],"name":"REVOLUTIONS AND REVOLT","terms":["Spring"],"prereqs":[],"subject":"JWST","credits":4}
,{"_id": "JWST 275","subid":["RELC 275"],"name":"PSYCHOLOGY, RELIGION, ETHICS, LOVE","terms":["Spring"],"prereqs":[],"subject":"JWST","credits":4}
,{"_id": "JWST 325","subid":["RELC 325"],"name":"RESPONDING TO THE HOLOCAUST","terms":["Spring"],"prereqs":[],"subject":"JWST","credits":4}
,{"_id": "KORE 101","subid":[],"name":"ELEMENTARY KOREAN I","terms":["Fall"],"prereqs":[],"subject":"KORE","credits":4}
,{"_id": "KORE 151","subid":[],"name":"INTERMEDIATE KOREAN I","terms":["Fall"],"prereqs":[],"subject":"KORE","credits":4}
,{"_id": "KORE 201","subid":[],"name":"ADVANCED INTERMEDIATE KOREAN I","terms":["Fall"],"prereqs":[],"subject":"KORE","credits":4}
,{"_id": "KORE 102","subid":[],"name":"ELEMENTARY KOREAN II","terms":["Spring"],"prereqs":[],"subject":"KORE","credits":4}
,{"_id": "KORE 152","subid":[],"name":"INTERMEDIATE KOREAN II","terms":["Spring"],"prereqs":[],"subject":"KORE","credits":4}
,{"_id": "KORE 202","subid":[],"name":"ADVANCED INTERMEDIATE KOREAN II","terms":["Spring"],"prereqs":[],"subject":"KORE","credits":4}
,{"_id": "LATN 102","subid":[],"name":"ELEMENTARY LATIN II","terms":["Fall"],"prereqs":[],"subject":"LATN","credits":4}
,{"_id": "LATN 221","subid":[],"name":"CICERO","terms":["Fall"],"prereqs":[],"subject":"LATN","credits":4}
,{"_id": "LATN 450","subid":[],"name":"LATIN SKILLS","terms":["Fall"],"prereqs":[],"subject":"LATN","credits":4}
,{"_id": "LATN 101","subid":[],"name":"ELEMENTARY LATIN I","terms":["Spring"],"prereqs":[],"subject":"LATN","credits":4}
,{"_id": "LATN 103","subid":[],"name":"INTERMEDIATE LATIN","terms":["Spring"],"prereqs":[],"subject":"LATN","credits":4}
,{"_id": "LATN 204","subid":[],"name":"CATULLUS","terms":["Spring"],"prereqs":[],"subject":"LATN","credits":4}
,{"_id": "LAW 205","subid":[],"name":"BUS LAW-CONTRACTS/LEGAL ENTRE","terms":["Fall"],"prereqs":[],"subject":"LAW","credits":4}
,{"_id": "LAW 250","subid":[],"name":"BUS LAW: TRANS &AMP; OTHER TOPIC","terms":["Spring"],"prereqs":[],"subject":"LAW","credits":4}
,{"_id": "LING 104","subid":["ANTH 105"],"name":"LANGUAGE &AMP; CULTURE","terms":["Fall"],"prereqs":[],"subject":"LING","credits":4}
,{"_id": "LING 107","subid":[],"name":"LANGUAGE &AMP; LANDSCAPE: WATER IS LIFE","terms":["Fall"],"prereqs":[],"subject":"LING","credits":4}
,{"_id": "LING 110","subid":[],"name":"INTRO TO LINGUISTIC ANALYSIS","terms":["Fall","Spring"],"prereqs":[],"subject":"LING","credits":4}
,{"_id": "LING 206","subid":["ENGL 200","ENGL 400","LING 406"],"name":"HISTORY OF THE ENGLISH LANGUAGE","terms":["Fall"],"prereqs":[],"subject":"LING","credits":4}
,{"_id": "LING 208","subid":["ASLA 208","BCSC 259","PSYC 259"],"name":"LANGUAGE DEVELOPMENT","terms":["Fall"],"prereqs":["BCSC 152","LING 110"],"subject":"LING","credits":4}
,{"_id": "LING 210","subid":["LING 210W","LING 410"],"name":"INTRO TO LANG SOUND SYSTEMS","terms":["Fall"],"prereqs":["THE 210","THE 410","LING 110"],"subject":"LING","credits":4}
,{"_id": "LING 217","subid":["ASLA 260","BCSC 152","PSYC 152"],"name":"LANGUAGE &AMP; PSYCHOLINGUISTICS","terms":["Fall"],"prereqs":["BCSC 110","BCSC 111"],"subject":"LING","credits":4}
,{"_id": "LING 220","subid":["LING 420"],"name":"INTRO TO GRAMMATICAL SYSTEMS","terms":["Fall","Spring"],"prereqs":[],"subject":"LING","credits":4}
,{"_id": "LING 225","subid":["LING 425"],"name":"INTRO TO SEMANTIC ANALYSIS","terms":["Fall"],"prereqs":["LING 265","LING 465","LING 110"],"subject":"LING","credits":4}
,{"_id": "LING 226","subid":["LING 426"],"name":"MORPHOLOGY","terms":["Fall"],"prereqs":[],"subject":"LING","credits":4}
,{"_id": "LING 240","subid":["LING 440"],"name":"TOPICS IN LANG. VARIATION &AMP; CHANGE","terms":["Fall"],"prereqs":["THE 110","THE 210","THE 220"],"subject":"LING","credits":4}
,{"_id": "LING 245","subid":["LING 445","PHIL 247","PHIL 247W","PHIL 447"],"name":"PHILOSOPHY OF LANGUAGE","terms":["Fall"],"prereqs":["PHIL 110"],"subject":"LING","credits":4}
,{"_id": "LING 247","subid":["BCSC 235","BCSC 435","CSC 247","CSC 447","LING 447","TCS 447"],"name":"NATURAL LANGUAGE PROCESSING","terms":["Fall","Spring"],"prereqs":["CSC 447","CSC 242"],"subject":"LING","credits":4}
,{"_id": "LING 260","subid":["LING 260W","LING 460"],"name":"SYNTACTIC THEORY","terms":["Fall"],"prereqs":[],"subject":"LING","credits":4}
,{"_id": "LING 261","subid":["LING 461"],"name":"CONSTRAINT BASED SYNTAX","terms":["Fall"],"prereqs":["THE 261","THE 461","LING 110","LING 220"],"subject":"LING","credits":4}
,{"_id": "LING 268","subid":["LING 468"],"name":"COMPUTATIONAL SEMANTICS","terms":["Fall"],"prereqs":[],"subject":"LING","credits":4}
,{"_id": "LING 270","subid":["LING 270W","LING 470"],"name":"PRESERVING DIVERSITY IN LANGUAGE AND CULTURE","terms":["Fall"],"prereqs":["LING 110"],"subject":"LING","credits":4}
,{"_id": "LING 282","subid":["LING 482"],"name":"DEEP LEARNING METHODS IN COMPUTATIONAL LINGUISTICS","terms":["Fall"],"prereqs":["LING 224","CSC 247","LING 281","CSC 248"],"subject":"LING","credits":4}
,{"_id": "LING 495","subid":[],"name":"MASTER'S RESEARCH IN LING","terms":["Fall","Spring"],"prereqs":[],"subject":"LING","credits":4}
,{"_id": "LING 501","subid":[],"name":"LINGUISTICS GRADUATE PROSEMINAR","terms":["Fall"],"prereqs":[],"subject":"LING","credits":1}
,{"_id": "LING 590","subid":[],"name":"SUPERVISED TEACHING","terms":["Fall","Spring"],"prereqs":[],"subject":"LING","credits":6}
,{"_id": "LING 595","subid":[],"name":"PHD RESEARCH IN LING","terms":["Fall","Spring"],"prereqs":[],"subject":"LING","credits":4}
,{"_id": "LING 897","subid":[],"name":"MASTER'S DISSERTATION","terms":["Fall","Summer","Spring"],"prereqs":[],"subject":"LING","credits":0}
,{"_id": "LING 494","subid":[],"name":"INTERNSHIP","terms":["Summer"],"prereqs":[],"subject":"LING","credits":1}
,{"_id": "LING 161","subid":["WRTG 250"],"name":"MODERN ENGLISH GRAMMAR","terms":["Spring"],"prereqs":[],"subject":"LING","credits":4}
,{"_id": "LING 204","subid":["LING 404"],"name":"HISTORY OF LINGUISTIC THOUGHT","terms":["Spring"],"prereqs":["LING 110","LING 210","LING 220"],"subject":"LING","credits":4}
,{"_id": "LING 207","subid":["ENGL 201","ENGL 401","HIST 230","LING 407"],"name":"OLD ENGLISH","terms":["Spring"],"prereqs":["THE 700","THE 110","THE 180"],"subject":"LING","credits":4}
,{"_id": "LING 216","subid":["BCSC 266","BME 216","BME 416","LING 416"],"name":"SPEECH ON THE BRAIN","terms":["Spring"],"prereqs":[],"subject":"LING","credits":4}
,{"_id": "LING 224","subid":["LING 424"],"name":"INTRO TO COMPUTATIONAL LING","terms":["Spring"],"prereqs":["CSC 161","LING 110"],"subject":"LING","credits":4}
,{"_id": "LING 227","subid":["LING 427"],"name":"TOPICS IN PHONETICS &AMP; PHONOLOGY","terms":["Spring"],"prereqs":["LING 110","LING 210"],"subject":"LING","credits":4}
,{"_id": "LING 230","subid":["ASLA 200","BCSC 264","BCSC 564","LING 430"],"name":"SIGN LANGUAGE STRUCTURE","terms":["Spring"],"prereqs":["THE 106"],"subject":"LING","credits":4}
,{"_id": "LING 250","subid":["CSC 250","CSC 450","LING 450"],"name":"DATA SCIENCE FOR LINGUISTICS","terms":["Spring"],"prereqs":["LING 110","LING 210","LING 220","LING 225"],"subject":"LING","credits":4}
,{"_id": "LING 266","subid":["LING 466"],"name":"INTRO TO PRAGMATICS","terms":["Spring"],"prereqs":[],"subject":"LING","credits":4}
,{"_id": "LING 389","subid":["LING 471"],"name":"SENIOR SEMINAR","terms":["Spring"],"prereqs":["LING 110","LING 210","LING 220","LING 225"],"subject":"LING","credits":4}
,{"_id": "LING 395H","subid":[],"name":"INDEPENDENT RESEARCH-HONORS","terms":["Spring"],"prereqs":[],"subject":"LING","credits":4}
,{"_id": "LING 589","subid":[],"name":"GRADUATE FIELD METHODS","terms":["Spring"],"prereqs":[],"subject":"LING","credits":4}
,{"_id": "LING 591","subid":[],"name":"PHD READING COURSE IN LING","terms":["Spring"],"prereqs":[],"subject":"LING","credits":15}
,{"_id": "LING 595A","subid":[],"name":"PHD RESEARCH IN ABSENTIA","terms":["Spring"],"prereqs":[],"subject":"LING","credits":12}
,{"_id": "LING 895","subid":[],"name":"CONT OF MASTER'S ENROLLMENT","terms":["Spring"],"prereqs":[],"subject":"LING","credits":0}
,{"_id": "LING 897A","subid":[],"name":"MASTER'S DISSERTATION IN ABSENTIA","terms":["Spring"],"prereqs":[],"subject":"LING","credits":0}
,{"_id": "LING 897B","subid":[],"name":"MASTER'S DISSERTATION - STUDY ABROAD","terms":["Spring"],"prereqs":[],"subject":"LING","credits":0}
,{"_id": "LING 997A","subid":[],"name":"DOCT DISSERTATN IN ABSENTIA","terms":["Spring"],"prereqs":[],"subject":"LING","credits":0}
,{"_id": "LING 999","subid":[],"name":"DOCTORAL DISSERTATION","terms":["Spring"],"prereqs":[],"subject":"LING","credits":0}
,{"_id": "LING 999A","subid":[],"name":"DOCT DISSERTATN IN ABSENTIA","terms":["Spring"],"prereqs":[],"subject":"LING","credits":0}
,{"_id": "LTST 401","subid":[],"name":"TRANSLATION PORTFOLIO","terms":["Fall"],"prereqs":[],"subject":"LTST","credits":4}
,{"_id": "LTST 231","subid":["FREN 212","FREN 412","LTST 431"],"name":"FRENCH LITERATURE IN TRANSLATION","terms":["Spring"],"prereqs":["FREN 200"],"subject":"LTST","credits":4}
,{"_id": "LTST 263","subid":["ENGL 289","WRTG 263"],"name":"TRANSLATION: INTERPRETING &AMP; ADAPTING","terms":["Spring"],"prereqs":[],"subject":"LTST","credits":4}
,{"_id": "LTST 395","subid":[],"name":"INDEPENDENT RESEARCH","terms":["Spring"],"prereqs":[],"subject":"LTST","credits":4}
,{"_id": "LTST 396","subid":["ENGL 267","LTST 410"],"name":"INTRO TO LITERARY PUBLISHING","terms":["Spring"],"prereqs":[],"subject":"LTST","credits":4}
,{"_id": "LTST 406","subid":["CLTR 284","CLTR 484","ENGL 287","LTST 206"],"name":"TRANSLATION&AMP;WORLD LITERATURE","terms":["Spring"],"prereqs":[],"subject":"LTST","credits":4}
,{"_id": "LTST 491","subid":[],"name":"MASTER'S READING COURSE","terms":["Spring"],"prereqs":[],"subject":"LTST","credits":0}
,{"_id": "MATH 140","subid":[],"name":"FOUNDATIONS OF CALCULUS","terms":["Fall"],"prereqs":[],"subject":"MATH","credits":4}
,{"_id": "MATH 141","subid":[],"name":"CALCULUS I","terms":["Fall","Summer","Spring"],"prereqs":[],"subject":"MATH","credits":4}
,{"_id": "MATH 142","subid":[],"name":"CALCULUS II","terms":["Fall","Summer","Spring"],"prereqs":["SPAN 141","THE 143","THE 162"],"subject":"MATH","credits":4}
,{"_id": "MATH 143","subid":[],"name":"CALCULUS III","terms":["Fall","Summer","Spring"],"prereqs":["MTH 141","MTH 142","MTH 162"],"subject":"MATH","credits":4}
,{"_id": "MATH 150","subid":[],"name":"DISCRETE MATHEMATICS","terms":["Fall","Summer","Spring"],"prereqs":[],"subject":"MATH","credits":4}
,{"_id": "MATH 150A","subid":[],"name":"DISCRETE MATH MODULE 171Q","terms":["Fall","Spring"],"prereqs":["THE 150"],"subject":"MATH","credits":1}
,{"_id": "MATH 162","subid":[],"name":"CALCULUS IIA","terms":["Fall","Summer","Spring"],"prereqs":["SPAN 161","SPAN 164","SPAN 165","SPAN 162","SPAN 143","THE 142"],"subject":"MATH","credits":4}
,{"_id": "MATH 164","subid":[],"name":"MULTIDIMENSIONAL CALCULUS","terms":["Fall","Summer","Spring"],"prereqs":["MTH 143","MTH 162","MTH 172","MTH 164"],"subject":"MATH","credits":4}
,{"_id": "MATH 165","subid":[],"name":"LINEAR ALGEBRA W/DIFF. EQU","terms":["Fall","Summer","Spring"],"prereqs":["MTH 143","MTH 162","MTH 172","MTH 164","MTH 165","MTH 163"],"subject":"MATH","credits":4}
,{"_id": "MATH 171","subid":[],"name":"HONORS CALCULUS I","terms":["Fall"],"prereqs":[],"subject":"MATH","credits":5}
,{"_id": "MATH 173","subid":[],"name":"HONORS CALCULUS III","terms":["Fall"],"prereqs":["MTH 172","MTH 161","MTH 165","MTH 235"],"subject":"MATH","credits":5}
,{"_id": "MATH 190","subid":[],"name":"TOPICS IN PROBLEM SOLVING","terms":["Fall"],"prereqs":[],"subject":"MATH","credits":1}
,{"_id": "MATH 200","subid":[],"name":"TRANSITION TO HIGHER MATH","terms":["Fall","Spring"],"prereqs":["MTH 162","MTH 200","MTH 172","MTH 235"],"subject":"MATH","credits":4}
,{"_id": "MATH 200WM","subid":[],"name":"TRANSITION TO HIGHER MATH","terms":["Fall"],"prereqs":[],"subject":"MATH","credits":0}
,{"_id": "MATH 201","subid":["STAT 201"],"name":"INTRO TO PROBABILITY","terms":["Fall","Summer","Spring"],"prereqs":["MTH 201","MTH 162"],"subject":"MATH","credits":4}
,{"_id": "MATH 203","subid":["STAT 203"],"name":"INTRO TO MATH STATISTICS","terms":["Fall","Spring"],"prereqs":["SPAN 203","SPAN 201"],"subject":"MATH","credits":4}
,{"_id": "MATH 208","subid":[],"name":"OPERATIONS RESEARCH I","terms":["Fall"],"prereqs":["SPAN 162","SPAN 165","SPAN 173"],"subject":"MATH","credits":4}
,{"_id": "MATH 210","subid":[],"name":"INTRO TO FINANCIAL MATHEMTCS","terms":["Fall","Spring"],"prereqs":["FIN 205","FIN 206","FIN 143","FIN 162","STAT 211","STAT 212","STAT 213","STAT 230","STAT 201","FIN 210"],"subject":"MATH","credits":4}
,{"_id": "MATH 215","subid":[],"name":"FRACTALS &AMP; CHAOTIC DYNAMICS","terms":["Fall"],"prereqs":["SPAN 171","SPAN 162","SPAN 200"],"subject":"MATH","credits":4}
,{"_id": "MATH 230","subid":[],"name":"NUMBER THEORY WITH APPL","terms":["Fall"],"prereqs":["MTH 172","MTH 200","MTH 235"],"subject":"MATH","credits":4}
,{"_id": "MATH 235","subid":[],"name":"LINEAR ALGEBRA","terms":["Fall","Summer","Spring"],"prereqs":["MTH 165","MTH 200"],"subject":"MATH","credits":4}
,{"_id": "MATH 235WM","subid":[],"name":"LINEAR ALGEBRA","terms":["Fall"],"prereqs":[],"subject":"MATH","credits":0}
,{"_id": "MATH 237","subid":[],"name":"INTRO TO ALGEBRA II","terms":["Fall"],"prereqs":["SPAN 236"],"subject":"MATH","credits":4}
,{"_id": "MATH 238","subid":[],"name":"COMBINATORIAL MATH.","terms":["Fall"],"prereqs":["MTH 200","MTH 235","MTH 171"],"subject":"MATH","credits":4}
,{"_id": "MATH 255","subid":[],"name":"DIFFERENTIAL GEOMETRY","terms":["Fall"],"prereqs":["SPAN 164","SPAN 235","SPAN 174"],"subject":"MATH","credits":4}
,{"_id": "MATH 265","subid":[],"name":"FUNCTIONS OF REAL VARIABLE I","terms":["Fall"],"prereqs":["MTH 164","MTH 235","MTH 200","MTH 174"],"subject":"MATH","credits":4}
,{"_id": "MATH 265H","subid":[],"name":"FUNCTNS OF REAL VAR I (HON)","terms":["Fall"],"prereqs":["MTH 164","MTH 235","MTH 200","MTH 174","SPAN 265"],"subject":"MATH","credits":4}
,{"_id": "MATH 265WM","subid":[],"name":"FUNCTIONS OF REAL VARIABLES I","terms":["Fall"],"prereqs":[],"subject":"MATH","credits":0}
,{"_id": "MATH 280","subid":[],"name":"NUMERICAL ANALYSIS","terms":["Fall"],"prereqs":["MTH 235","MTH 173"],"subject":"MATH","credits":4}
,{"_id": "MATH 281","subid":["CHE 400","ME 201","ME 400"],"name":"APPLIED BOUNDARY VALUE PROBLEMS","terms":["Fall"],"prereqs":[],"subject":"MATH","credits":4}
,{"_id": "MATH 390","subid":[],"name":"SUPERVISED TEACHING: MATH 217","terms":["Fall"],"prereqs":[],"subject":"MATH","credits":4}
,{"_id": "MATH 394","subid":[],"name":"INTERNSHIP","terms":["Fall"],"prereqs":[],"subject":"MATH","credits":4}
,{"_id": "MATH 430","subid":[],"name":"NUMBER THEORY","terms":["Fall"],"prereqs":["SPAN 436","SPAN 437"],"subject":"MATH","credits":4}
,{"_id": "MATH 436","subid":[],"name":"ALGEBRA I","terms":["Fall"],"prereqs":[],"subject":"MATH","credits":4}
,{"_id": "MATH 440","subid":[],"name":"GENERAL TOPOLOGY","terms":["Fall"],"prereqs":[],"subject":"MATH","credits":4}
,{"_id": "MATH 443","subid":[],"name":"ALGEBRAIC TOPOLOGY","terms":["Fall"],"prereqs":[],"subject":"MATH","credits":4}
,{"_id": "MATH 463","subid":[],"name":"PARTIAL DIFFERENTIAL EQUATIONS","terms":["Fall"],"prereqs":[],"subject":"MATH","credits":4}
,{"_id": "MATH 471","subid":[],"name":"ANALYSIS I","terms":["Fall"],"prereqs":["MTH 265"],"subject":"MATH","credits":4}
,{"_id": "MATH 472","subid":[],"name":"ANALYSIS III","terms":["Fall"],"prereqs":["MTH 467","MTH 471"],"subject":"MATH","credits":4}
,{"_id": "MATH 483","subid":[],"name":"2ND YEAR GRAD ORIENTATION","terms":["Fall"],"prereqs":[],"subject":"MATH","credits":1}
,{"_id": "MATH 492","subid":[],"name":"GRAD PROFESSIONAL SEMINAR","terms":["Fall"],"prereqs":[],"subject":"MATH","credits":1}
,{"_id": "MATH 504","subid":[],"name":"STOCHASTIC PROCESS","terms":["Fall"],"prereqs":[],"subject":"MATH","credits":4}
,{"_id": "MATH 530","subid":[],"name":"ELLIP CURVES &AMP; ELLIP L-SERIES","terms":["Fall"],"prereqs":[],"subject":"MATH","credits":4}
,{"_id": "MATH 557","subid":[],"name":"TOPICS IN DIFF GEOMETRY","terms":["Fall"],"prereqs":[],"subject":"MATH","credits":4}
,{"_id": "MATH 591","subid":[],"name":"PHD READINGS IN MATH","terms":["Fall","Spring"],"prereqs":[],"subject":"MATH","credits":5}
,{"_id": "MATH 594","subid":[],"name":"INTERNSHIP","terms":["Fall","Summer","Spring"],"prereqs":[],"subject":"MATH","credits":1}
,{"_id": "MATH 595","subid":[],"name":"PHD RESEARCH IN MATH","terms":["Fall","Spring"],"prereqs":[],"subject":"MATH","credits":12}
,{"_id": "MATH 895","subid":[],"name":"CONT OF MASTER'S ENROLLMENT","terms":["Fall","Spring"],"prereqs":[],"subject":"MATH","credits":0}
,{"_id": "MATH 897","subid":[],"name":"MASTER'S DISSERTATION","terms":["Fall","Spring"],"prereqs":[],"subject":"MATH","credits":0}
,{"_id": "MATH 899","subid":[],"name":"MASTER'S DISSERTATION","terms":["Fall","Spring"],"prereqs":[],"subject":"MATH","credits":0}
,{"_id": "MATH 995","subid":[],"name":"CONT OF DOCTORAL ENROLLMENT","terms":["Fall","Spring"],"prereqs":[],"subject":"MATH","credits":0}
,{"_id": "MATH 997","subid":[],"name":"DOCTORAL DISSERTATION","terms":["Fall","Summer","Spring"],"prereqs":[],"subject":"MATH","credits":0}
,{"_id": "MATH 999","subid":[],"name":"DOCTORAL DISSERTATION","terms":["Fall","Spring"],"prereqs":[],"subject":"MATH","credits":0}
,{"_id": "MATH 161","subid":[],"name":"CALCULUS IA","terms":["Summer","Spring"],"prereqs":[],"subject":"MATH","credits":4}
,{"_id": "MATH 172","subid":[],"name":"HONORS CALCULUS II","terms":["Spring"],"prereqs":["MTH 171"],"subject":"MATH","credits":5}
,{"_id": "MATH 174","subid":[],"name":"HONORS CALCULUS IV","terms":["Spring"],"prereqs":[],"subject":"MATH","credits":5}
,{"_id": "MATH 202","subid":[],"name":"INTRO TO STOCH PROC","terms":["Spring"],"prereqs":["MTH 201"],"subject":"MATH","credits":4}
,{"_id": "MATH 209","subid":[],"name":"OPERATIONS RESEARCH II:  STOCHASTIC MODELS AND QUEUEING","terms":["Spring"],"prereqs":["SPAN 201","SPAN 202"],"subject":"MATH","credits":4}
,{"_id": "MATH 218","subid":[],"name":"INTRO MATH MOD-SOC&AMP;LIFE SCI","terms":["Spring"],"prereqs":["MTH 162","MTH 143","MTH 172"],"subject":"MATH","credits":4}
,{"_id": "MATH 225","subid":["PHIL 215","PHIL 415"],"name":"INTERMEDIATE LOGIC","terms":["Spring"],"prereqs":[],"subject":"MATH","credits":4}
,{"_id": "MATH 233","subid":[],"name":"MATHEMATICAL CRYPTOGRAPH","terms":["Spring"],"prereqs":["SPAN 162","SPAN 171","SPAN 230"],"subject":"MATH","credits":4}
,{"_id": "MATH 236","subid":["MATH 236W"],"name":"INTRO TO ALGEBRA I","terms":["Spring"],"prereqs":["MTH 235","MTH 173"],"subject":"MATH","credits":4}
,{"_id": "MATH 236HW","subid":["MATH 236H"],"name":"INTRO TO ALGEBRA I (HONORS)","terms":["Spring"],"prereqs":[],"subject":"MATH","credits":4}
,{"_id": "MATH 240","subid":["MATH 240W"],"name":"INTRO TO TOPOLOGY","terms":["Spring"],"prereqs":["MTH 173","MTH 164","MTH 235","MTH 200"],"subject":"MATH","credits":4}
,{"_id": "MATH 240H","subid":["MATH 240HW"],"name":"INTRO TO TOPOLOGY (HONORS)","terms":["Spring"],"prereqs":["SPAN 173","SPAN 164","SPAN 235","SPAN 200","SPAN 240"],"subject":"MATH","credits":4}
,{"_id": "MATH 248","subid":[],"name":"THEORY OF GRAPHS","terms":["Spring"],"prereqs":["SPAN 173","SPAN 235","SPAN 200","SPAN 165"],"subject":"MATH","credits":4}
,{"_id": "MATH 250","subid":[],"name":"INTRO TO GEOMETRY","terms":["Spring"],"prereqs":["MTH 165","MTH 200","MTH 235","MTH 173"],"subject":"MATH","credits":4}
,{"_id": "MATH 263","subid":[],"name":"QUALITATIVE THEORY OF ODES","terms":["Spring"],"prereqs":["SPAN 165","SPAN 173"],"subject":"MATH","credits":4}
,{"_id": "MATH 282","subid":[],"name":"INTRO TO COMPLEX VAR WITH APP","terms":["Spring"],"prereqs":["SPAN 164","SPAN 174","SPAN 200","SPAN 235","SPAN 281"],"subject":"MATH","credits":4}
,{"_id": "MATH 285","subid":[],"name":"METHODS OF APPLIED MATH","terms":["Spring"],"prereqs":["SPAN 164","SPAN 165","SPAN 174"],"subject":"MATH","credits":4}
,{"_id": "MATH 287","subid":["OPT 287"],"name":"MATH METHODS IN OPT &AMP; PHYSICS","terms":["Spring"],"prereqs":[],"subject":"MATH","credits":4}
,{"_id": "MATH 300W","subid":[],"name":"HISTORY OF MATHEMATICS I","terms":["Spring"],"prereqs":["MTH 161","THE 170","MTH 200","MTH 391"],"subject":"MATH","credits":4}
,{"_id": "MATH 403","subid":[],"name":"THEORY OF PROBABILITY","terms":["Spring"],"prereqs":["SPAN 471"],"subject":"MATH","credits":4}
,{"_id": "MATH 437","subid":[],"name":"ALGEBRA II","terms":["Spring"],"prereqs":["SPAN 436"],"subject":"MATH","credits":4}
,{"_id": "MATH 453","subid":[],"name":"DIFFERENTIABLE MANIFOLDS","terms":["Spring"],"prereqs":["SPAN 265"],"subject":"MATH","credits":4}
,{"_id": "MATH 467","subid":[],"name":"ANALYSIS II","terms":["Spring"],"prereqs":["MTH 471"],"subject":"MATH","credits":4}
,{"_id": "MATH 486","subid":[],"name":"GUIDED INDEPENDENT STUDY","terms":["Spring"],"prereqs":[],"subject":"MATH","credits":1}
,{"_id": "MATH 506","subid":[],"name":"TOPIC-ANALYSIS &AMP; FUNC ANALYSIS","terms":["Spring"],"prereqs":[],"subject":"MATH","credits":4}
,{"_id": "MATH 535","subid":[],"name":"COMMUTATIVE ALGEBRA","terms":["Spring"],"prereqs":[],"subject":"MATH","credits":4}
,{"_id": "MATH 538","subid":[],"name":"ALGEBRAIC GEOMETRY I","terms":["Spring"],"prereqs":[],"subject":"MATH","credits":4}
,{"_id": "MATH 589","subid":[],"name":"TOPICS IN INVERSE PROBLEMS","terms":["Spring"],"prereqs":["MTH 471","MTH 467","MTH 472"],"subject":"MATH","credits":4}
,{"_id": "MATH 595A","subid":[],"name":"PHD RESEARCH IN ABSENTIA","terms":["Spring"],"prereqs":[],"subject":"MATH","credits":12}
,{"_id": "MATH 997A","subid":[],"name":"DOCT DISSERTATN IN ABSENTIA","terms":["Spring"],"prereqs":[],"subject":"MATH","credits":0}
,{"_id": "MATH 997B","subid":[],"name":"DOCTORAL DISSERTATION IN ABSENTIA ABROAD","terms":["Spring"],"prereqs":[],"subject":"MATH","credits":0}
,{"_id": "MATH 999A","subid":[],"name":"DOCT DISSERTATN IN ABSENTIA","terms":["Spring"],"prereqs":[],"subject":"MATH","credits":0}
,{"_id": "MATH 999B","subid":[],"name":"IN-ABSENTIA ABROAD","terms":["Spring"],"prereqs":[],"subject":"MATH","credits":0}
,{"_id": "ME 091","subid":[],"name":"SOLAR SPLASH","terms":["Fall"],"prereqs":[],"subject":"ME","credits":2}
,{"_id": "ME 1001","subid":[],"name":"RESEARCH ASSISTANTSHIP","terms":["Fall"],"prereqs":[],"subject":"ME","credits":0}
,{"_id": "ME 104","subid":["EAS 104"],"name":"THE ENGINEERING OF BRIDGES","terms":["Fall"],"prereqs":[],"subject":"ME","credits":4}
,{"_id": "ME 110","subid":[],"name":"INTRO TO CAD AND DRAWING","terms":["Fall","Spring"],"prereqs":[],"subject":"ME","credits":2}
,{"_id": "ME 120","subid":[],"name":"ENGINEERING MECHANICS I","terms":["Fall","Spring"],"prereqs":[],"subject":"ME","credits":4}
,{"_id": "ME 121","subid":[],"name":"ENGINEERING MECHANICS II","terms":["Fall"],"prereqs":[],"subject":"ME","credits":4}
,{"_id": "ME 145","subid":["OPT 145"],"name":"CNC GRIND FOR PRECISION MFG","terms":["Fall"],"prereqs":[],"subject":"ME","credits":2}
,{"_id": "ME 160","subid":[],"name":"ENGINEERING COMPUTATION I","terms":["Fall"],"prereqs":[],"subject":"ME","credits":2}
,{"_id": "ME 201","subid":["CHE 400","MATH 281","ME 400"],"name":"APPLIED BOUNDARY VALUE PROBLEMS","terms":["Fall"],"prereqs":[],"subject":"ME","credits":4}
,{"_id": "ME 204","subid":[],"name":"MECHANICAL DESIGN","terms":["Fall"],"prereqs":[],"subject":"ME","credits":4}
,{"_id": "ME 213","subid":[],"name":"MECHANICAL SYSTEMS","terms":["Fall"],"prereqs":[],"subject":"ME","credits":4}
,{"_id": "ME 224","subid":["OPT 243"],"name":"OPTICAL FAB. AND TESTING","terms":["Fall"],"prereqs":[],"subject":"ME","credits":4}
,{"_id": "ME 225","subid":["PHYS 255"],"name":"INTRO FLUID DYNAMICS","terms":["Fall"],"prereqs":[],"subject":"ME","credits":4}
,{"_id": "ME 245","subid":["ME 445","OPT 245","OPT 445","TME 445"],"name":"PRECISION INSTRUMENT DESIGN","terms":["Fall"],"prereqs":[],"subject":"ME","credits":4}
,{"_id": "ME 254","subid":["BME 486","ME 441","TME 441"],"name":"FINITE ELEMENTS METHODS","terms":["Fall"],"prereqs":[],"subject":"ME","credits":4}
,{"_id": "ME 280","subid":["MSC 202","MSC 480"],"name":"INTRO TO MATERIALS SCIENCE","terms":["Fall"],"prereqs":[],"subject":"ME","credits":4}
,{"_id": "ME 434","subid":["PHYS 454","TME 434"],"name":"INTRO TO PLASMA PHYSICS I","terms":["Fall"],"prereqs":[],"subject":"ME","credits":4}
,{"_id": "ME 495","subid":[],"name":"MASTER'S RESEARCH IN ME","terms":["Fall","Spring"],"prereqs":[],"subject":"ME","credits":6}
,{"_id": "ME 497","subid":[],"name":"RESEARCH SEMINAR IN ME","terms":["Fall","Spring"],"prereqs":[],"subject":"ME","credits":0}
,{"_id": "ME 537","subid":["PHYS 453"],"name":"INTRODUCTION TO HIGH ENERGY DENSITY PHYSICS","terms":["Fall"],"prereqs":[],"subject":"ME","credits":4}
,{"_id": "ME 595","subid":[],"name":"PHD RESEARCH IN ME","terms":["Fall","Summer","Spring"],"prereqs":[],"subject":"ME","credits":12}
,{"_id": "ME 897","subid":[],"name":"MASTERS DISSERTATION","terms":["Fall","Spring","Spring"],"prereqs":[],"subject":"ME","credits":0}
,{"_id": "ME 997","subid":[],"name":"DOCTORAL DISSERTATION","terms":["Fall","Summer","Spring"],"prereqs":[],"subject":"ME","credits":0}
,{"_id": "ME 999","subid":[],"name":"DOCTORAL DISSERTATION","terms":["Fall","Spring"],"prereqs":[],"subject":"ME","credits":0}
,{"_id": "ME 090","subid":[],"name":"UR SAE BAJA TEAM","terms":["Spring"],"prereqs":[],"subject":"ME","credits":2}
,{"_id": "ME 123","subid":[],"name":"THERMODYNAMICS","terms":["Spring"],"prereqs":["THE 162","THE 121"],"subject":"ME","credits":4}
,{"_id": "ME 205","subid":[],"name":"ADVANCED MECHANICAL DESIGN","terms":["Spring"],"prereqs":["ME 204"],"subject":"ME","credits":4}
,{"_id": "ME 212","subid":["BME 212","BME 412","ME 412","MSC 486"],"name":"VISCO IN BIO TISSUES","terms":["Spring"],"prereqs":["ME 225","CHE 243","ME 226","BME 201"],"subject":"ME","credits":4}
,{"_id": "ME 222","subid":["ME 424","MSC 424","TME 424"],"name":"ROBUST DESIGN/QUALITY","terms":["Spring"],"prereqs":[],"subject":"ME","credits":4}
,{"_id": "ME 223","subid":[],"name":"HEAT TRANSFER","terms":["Spring"],"prereqs":[],"subject":"ME","credits":4}
,{"_id": "ME 226","subid":[],"name":"INTRO TO SOLID MECHANICS","terms":["Spring"],"prereqs":[],"subject":"ME","credits":4}
,{"_id": "ME 232","subid":["ME 432","MSC 432","OPT 232","OPT 432","TME 432"],"name":"OPTO-MECHANICAL","terms":["Spring"],"prereqs":[],"subject":"ME","credits":4}
,{"_id": "ME 241","subid":[],"name":"MECHANICS LAB LECTURE","terms":["Spring"],"prereqs":[],"subject":"ME","credits":4}
,{"_id": "ME 251","subid":[],"name":"HEAT POWER APPLICATION","terms":["Spring"],"prereqs":["ME 123","ME 225"],"subject":"ME","credits":4}
,{"_id": "ME 260","subid":[],"name":"ENGINEERING COMPUTATION II","terms":["Spring"],"prereqs":[],"subject":"ME","credits":2}
,{"_id": "ME 396","subid":[],"name":"MECHANICAL ENGINEERING SOPHOMORE SEMINAR","terms":["Spring"],"prereqs":[],"subject":"ME","credits":1}
,{"_id": "ME 404","subid":["BME 404"],"name":"COMPUTATIONAL METHODS","terms":["Spring"],"prereqs":[],"subject":"ME","credits":4}
,{"_id": "ME 435","subid":["PHYS 455","TME 435"],"name":"INTRO TO PLASMA PHYSICS II","terms":["Spring"],"prereqs":[],"subject":"ME","credits":4}
,{"_id": "ME 436","subid":["TME 436"],"name":"COMPRESSIBLE FLOW","terms":["Spring"],"prereqs":[],"subject":"ME","credits":4}
,{"_id": "ME 444","subid":["TME 444"],"name":"CONTINUUM MECHANICS","terms":["Spring"],"prereqs":[],"subject":"ME","credits":4}
,{"_id": "ME 450","subid":[],"name":"INTRODUCTION TO QUANTUM THEORY OF MATERIALS","terms":["Spring"],"prereqs":[],"subject":"ME","credits":4}
,{"_id": "ME 451","subid":[],"name":"CHARACTERIZATION METHODS IN MATERIALS","terms":["Spring"],"prereqs":[],"subject":"ME","credits":4}
,{"_id": "ME 465","subid":["MSC 465","OPT 465","PHYS 435","TEO 465"],"name":"PRINCIPLES OF LASERS","terms":["Spring"],"prereqs":[],"subject":"ME","credits":4}
,{"_id": "ME 488","subid":[],"name":"COMPUTATIONAL METHODS FOR HIGH-ENERGY-DENSITY PHYSICS","terms":["Spring"],"prereqs":[],"subject":"ME","credits":4}
,{"_id": "ME 532","subid":["PHYS 552"],"name":"MAGNETOHYDRODYNAMICS","terms":["Spring"],"prereqs":[],"subject":"ME","credits":4}
,{"_id": "ME 535","subid":["PHYS 553"],"name":"LASER PLASMA INTERACTIONS","terms":["Spring"],"prereqs":[],"subject":"ME","credits":4}
,{"_id": "ME 899","subid":[],"name":"MASTER'S DISSERTATION","terms":["Spring"],"prereqs":[],"subject":"ME","credits":0}
,{"_id": "ME 995","subid":[],"name":"CONT OF DOCTORAL ENROLLMENT","terms":["Spring"],"prereqs":[],"subject":"ME","credits":0}
,{"_id": "MKT 203","subid":[],"name":"PRINCIPLES OF MARKETING","terms":["Fall","Spring"],"prereqs":[],"subject":"MKT","credits":4}
,{"_id": "MKT 212","subid":[],"name":"MARKETING RESEARCH &AMP; ANALYTICS","terms":["Fall"],"prereqs":["MKT 203"],"subject":"MKT","credits":4}
,{"_id": "MKT 213","subid":[],"name":"MARKETING PROJECTS","terms":["Fall","Spring"],"prereqs":["MKT 203","MKT 212"],"subject":"MKT","credits":4}
,{"_id": "MKT 235","subid":[],"name":"PRODUCT &AMP; BRAND STRATEGY","terms":["Fall"],"prereqs":["MKT 203"],"subject":"MKT","credits":4}
,{"_id": "MKT 394","subid":[],"name":"INTERNSHIP","terms":["Fall"],"prereqs":[],"subject":"MKT","credits":4}
,{"_id": "MKT 233","subid":[],"name":"ADVERTISING &AMP; PROMOTIONAL STRATEGY","terms":["Spring"],"prereqs":[],"subject":"MKT","credits":4}
,{"_id": "MKT 237","subid":[],"name":"DIGITAL MARKETING STRATEGIES","terms":["Spring"],"prereqs":[],"subject":"MKT","credits":4}
,{"_id": "MKT 390","subid":[],"name":"SUPERVISED TEACHING- MKT 203","terms":["Spring"],"prereqs":[],"subject":"MKT","credits":2}
,{"_id": "MSC 202","subid":["ME 280","MSC 480"],"name":"INTRO TO MATERIALS SCIENCE","terms":["Fall"],"prereqs":[],"subject":"MSC","credits":4}
,{"_id": "MSC 423","subid":["ECE 223","ECE 423","TEE 423"],"name":"SEMICONDUCTOR DEVICES","terms":["Fall"],"prereqs":[],"subject":"MSC","credits":4}
,{"_id": "MSC 437","subid":["ECE 436","OPT 464","TEE 436"],"name":"NANOPHOTONIC DEVICES","terms":["Fall","Spring"],"prereqs":[],"subject":"MSC","credits":4}
,{"_id": "MSC 446","subid":["CHE 446","OPT 426"],"name":"LIQUID CRYSTAL MATERIALS 1","terms":["Fall"],"prereqs":[],"subject":"MSC","credits":2}
,{"_id": "MSC 454","subid":["CHE 454","TEC 454"],"name":"INTERFACIAL ENGINEERING","terms":["Fall"],"prereqs":[],"subject":"MSC","credits":4}
,{"_id": "MSC 456","subid":["CHEM 456","OPT 429"],"name":"CHEM BONDS:FROM MOLCLS TO MAT","terms":["Fall","Spring"],"prereqs":[],"subject":"MSC","credits":4}
,{"_id": "MSC 458","subid":["CHE 258","CHE 458","TEC 458"],"name":"ELECTROCHEM&AMP;ENGG &AMP; FUEL CELL","terms":["Fall"],"prereqs":[],"subject":"MSC","credits":4}
,{"_id": "MSC 478","subid":[],"name":"MACHINE LEARNING MOLECULE &AMP; MATLS","terms":["Fall"],"prereqs":[],"subject":"MSC","credits":4}
,{"_id": "MSC 495","subid":[],"name":"MASTER RESEARCH","terms":["Fall","Spring"],"prereqs":[],"subject":"MSC","credits":10}
,{"_id": "MSC 496","subid":[],"name":"MSC GRADUATE SEMINAR","terms":["Fall","Spring"],"prereqs":[],"subject":"MSC","credits":0}
,{"_id": "MSC 595","subid":[],"name":"RESEARCH IN MATERIALS SCIENCE","terms":["Fall","Spring"],"prereqs":[],"subject":"MSC","credits":12}
,{"_id": "MSC 895","subid":[],"name":"CONT OF MASTER'S ENROLLMENT","terms":["Fall","Spring"],"prereqs":[],"subject":"MSC","credits":0}
,{"_id": "MSC 899","subid":[],"name":"MASTER'S DISSERTATION","terms":["Fall","Spring"],"prereqs":[],"subject":"MSC","credits":0}
,{"_id": "MSC 995","subid":[],"name":"CONT OF DOCTORAL ENROLLMENT","terms":["Fall","Spring"],"prereqs":[],"subject":"MSC","credits":0}
,{"_id": "MSC 997","subid":[],"name":"DOCTORAL DISSERTATION","terms":["Fall","Summer","Spring"],"prereqs":[],"subject":"MSC","credits":0}
,{"_id": "MSC 897","subid":[],"name":"MASTER'S DISSERTATION","terms":["Summer"],"prereqs":[],"subject":"MSC","credits":0}
,{"_id": "MSC 307","subid":["MSC 507","OPT 307","OPT 407"],"name":"SEM PRACTICUM","terms":["Spring"],"prereqs":[],"subject":"MSC","credits":4}
,{"_id": "MSC 418","subid":["PHYS 418"],"name":"STATISTICAL MECHANICS","terms":["Spring"],"prereqs":[],"subject":"MSC","credits":4}
,{"_id": "MSC 424","subid":["ME 222","ME 424","TME 424"],"name":"ROBUST DESIGN/QUALITY","terms":["Spring"],"prereqs":[],"subject":"MSC","credits":4}
,{"_id": "MSC 432","subid":["ME 232","ME 432","OPT 232","OPT 432","TME 432"],"name":"OPTO-MECHANICAL","terms":["Spring"],"prereqs":[],"subject":"MSC","credits":4}
,{"_id": "MSC 461","subid":["CHE 461"],"name":"ADVANCED CHEMICAL KINETICS","terms":["Spring"],"prereqs":[],"subject":"MSC","credits":4}
,{"_id": "MSC 462","subid":["BME 262","BME 462","CHE 262","CHE 462"],"name":"CELL &AMP; TISSUE ENGINEERING","terms":["Spring"],"prereqs":["BME 260","CHE 225","ME 123","CHE 243","CHE 244","BME 211","BME 411","BIOL 202","BIOL 210"],"subject":"MSC","credits":4}
,{"_id": "MSC 465","subid":["ME 465","OPT 465","PHYS 435","TEO 465"],"name":"PRINCIPLES OF LASERS","terms":["Spring"],"prereqs":[],"subject":"MSC","credits":4}
,{"_id": "MSC 470","subid":["ECE 421","OPT 421","TEO 421"],"name":"OPT PROPERTIES OF MATERIALS","terms":["Spring"],"prereqs":[],"subject":"MSC","credits":4}
,{"_id": "MSC 486","subid":["BME 212","BME 412","ME 212","ME 412"],"name":"VISCO IN BIO TISSUES","terms":["Spring"],"prereqs":["ME 225","CHE 243","ME 226","BME 201"],"subject":"MSC","credits":4}
,{"_id": "MSC 594","subid":[],"name":"RESEARCH INTERNSHIP","terms":["Spring"],"prereqs":[],"subject":"MSC","credits":1}
,{"_id": "MSC 595A","subid":[],"name":"PHD RESEARCH IN ABSENTIA","terms":["Spring"],"prereqs":[],"subject":"MSC","credits":12}
,{"_id": "MSC 999A","subid":[],"name":"DOCT DISSERTATN IN ABSENTIA","terms":["Spring"],"prereqs":[],"subject":"MSC","credits":0}
,{"_id": "MUSC 100","subid":[],"name":"EXPERIENCING MUSIC","terms":["Fall"],"prereqs":[],"subject":"MUSC","credits":4}
,{"_id": "MUSC 101","subid":[],"name":"ELEMENTS OF MUSIC","terms":["Fall","Spring"],"prereqs":[],"subject":"MUSC","credits":4}
,{"_id": "MUSC 104","subid":[],"name":"CARILLON","terms":["Fall","Spring"],"prereqs":["MUSC 104"],"subject":"MUSC","credits":2}
,{"_id": "MUSC 107","subid":["GSWS 100"],"name":"TOPICS IN GSWS: ROCKIN� BODS: POPULAR MUSIC, GENDER, AND THE BODY","terms":["Fall"],"prereqs":[],"subject":"MUSC","credits":4}
,{"_id": "MUSC 109","subid":[],"name":"MUSICIANSHIP I: LITERACY SKILLS","terms":["Fall","Spring"],"prereqs":[],"subject":"MUSC","credits":1}
,{"_id": "MUSC 110","subid":[],"name":"INTRO TO MUSIC THEORY","terms":["Fall","Spring"],"prereqs":["THE 101","THE 110"],"subject":"MUSC","credits":4}
,{"_id": "MUSC 111","subid":[],"name":"THEORY I","terms":["Fall"],"prereqs":["THE 101","THE 110"],"subject":"MUSC","credits":4}
,{"_id": "MUSC 113","subid":[],"name":"MUSICIANSHIP II","terms":["Fall","Spring"],"prereqs":[],"subject":"MUSC","credits":1}
,{"_id": "MUSC 114","subid":[],"name":"MUSICIANSHIP III","terms":["Fall","Spring"],"prereqs":[],"subject":"MUSC","credits":1}
,{"_id": "MUSC 115","subid":[],"name":"MUSICIANSHIP IV","terms":["Fall","Spring"],"prereqs":[],"subject":"MUSC","credits":1}
,{"_id": "MUSC 116","subid":[],"name":"KEYBOARD SKILLS I","terms":["Fall","Spring"],"prereqs":[],"subject":"MUSC","credits":2}
,{"_id": "MUSC 117","subid":[],"name":"KEYBOARD SKILLS II","terms":["Fall","Spring"],"prereqs":[],"subject":"MUSC","credits":2}
,{"_id": "MUSC 121","subid":["AAAS 121","ANTH 213"],"name":"WORLD MUSIC IN CONTEXT","terms":["Fall"],"prereqs":[],"subject":"MUSC","credits":4}
,{"_id": "MUSC 122","subid":[],"name":"VOICE CLASS","terms":["Fall","Spring"],"prereqs":[],"subject":"MUSC","credits":1}
,{"_id": "MUSC 124","subid":[],"name":"SIGNED, SEALED AND DELIVERED","terms":["Fall"],"prereqs":[],"subject":"MUSC","credits":2}
,{"_id": "MUSC 130","subid":[],"name":"THE BEATLES, BRITISH INVASION &AMP; PSYCHEDELIA","terms":["Fall"],"prereqs":[],"subject":"MUSC","credits":4}
,{"_id": "MUSC 134","subid":[],"name":"MUSICAL STYLE &AMP; GENRE","terms":["Fall","Spring"],"prereqs":["MUSC 112"],"subject":"MUSC","credits":4}
,{"_id": "MUSC 136A","subid":[],"name":"EXPLORING CLASSICAL MUSIC","terms":["Fall"],"prereqs":[],"subject":"MUSC","credits":4}
,{"_id": "MUSC 138","subid":[],"name":"INTRO THE ART OF CONDUCTING","terms":["Fall"],"prereqs":["THE 112","THE 211"],"subject":"MUSC","credits":4}
,{"_id": "MUSC 141","subid":["AME 140","EAS 103","ECE 140"],"name":"INTRO TO AUDIO MUSIC &AMP; ENGIN","terms":["Fall"],"prereqs":[],"subject":"MUSC","credits":4}
,{"_id": "MUSC 150","subid":["ENS 120C","ENS 420C","ENS 421C"],"name":"TREBLE CHORUS","terms":["Fall"],"prereqs":[],"subject":"MUSC","credits":1}
,{"_id": "MUSC 152","subid":[],"name":"UNIVERSITY CHAMBER SINGERS","terms":["Fall","Spring"],"prereqs":[],"subject":"MUSC","credits":1}
,{"_id": "MUSC 153","subid":[],"name":"SYMPHONY ORCHESTRA","terms":["Fall","Spring"],"prereqs":[],"subject":"MUSC","credits":1}
,{"_id": "MUSC 154","subid":[],"name":"CHAMBER ORCHESTRA","terms":["Fall","Spring"],"prereqs":[],"subject":"MUSC","credits":1}
,{"_id": "MUSC 155","subid":[],"name":"CHAMBER ENSEMBLES","terms":["Fall","Spring"],"prereqs":[],"subject":"MUSC","credits":1}
,{"_id": "MUSC 156","subid":[],"name":"WIND SYMPHONY","terms":["Fall","Spring"],"prereqs":[],"subject":"MUSC","credits":1}
,{"_id": "MUSC 157","subid":[],"name":"JAZZ ENSEMBLE","terms":["Fall","Spring"],"prereqs":[],"subject":"MUSC","credits":1}
,{"_id": "MUSC 157A","subid":[],"name":"JAZZ COMBO","terms":["Fall","Spring"],"prereqs":[],"subject":"MUSC","credits":1}
,{"_id": "MUSC 158","subid":[],"name":"GOSPEL CHOIR","terms":["Fall","Spring"],"prereqs":[],"subject":"MUSC","credits":1}
,{"_id": "MUSC 159","subid":["ENS 214","ENS 401","ENS 414"],"name":"GAMELAN ENSEMBLE","terms":["Fall"],"prereqs":[],"subject":"MUSC","credits":1}
,{"_id": "MUSC 160","subid":[],"name":"CONCERT CHOIR","terms":["Fall","Spring"],"prereqs":[],"subject":"MUSC","credits":1}
,{"_id": "MUSC 163","subid":[],"name":"MUSICAL THEATER SKILLS","terms":["Fall","Spring"],"prereqs":[],"subject":"MUSC","credits":4}
,{"_id": "MUSC 165","subid":[],"name":"INTRODUCTORY MBIRA ENSEMBLE","terms":["Fall"],"prereqs":[],"subject":"MUSC","credits":1}
,{"_id": "MUSC 167","subid":[],"name":"THE ART OF THE PIANO","terms":["Fall"],"prereqs":[],"subject":"MUSC","credits":4}
,{"_id": "MUSC 168","subid":["AAAS 168","ENS 215"],"name":"WEST AFRICAN DRUMMING BEG","terms":["Fall"],"prereqs":[],"subject":"MUSC","credits":1}
,{"_id": "MUSC 170","subid":[],"name":"BRASS CHOIR","terms":["Fall","Spring"],"prereqs":[],"subject":"MUSC","credits":1}
,{"_id": "MUSC 173","subid":["AAAS 154","DMST 153","EHUM 153","FMST 153","SART 153"],"name":"INTRODUCTION TO SOUND ART","terms":["Fall"],"prereqs":[],"subject":"MUSC","credits":4}
,{"_id": "MUSC 180","subid":[],"name":"ROCK REPERTORY ENSEMBLE","terms":["Fall","Spring"],"prereqs":[],"subject":"MUSC","credits":1}
,{"_id": "MUSC 181","subid":[],"name":"BEYOND THE CLASSICS","terms":["Fall","Spring"],"prereqs":[],"subject":"MUSC","credits":2}
,{"_id": "MUSC 183","subid":[],"name":"INTRO TO CLASSICAL GUITAR","terms":["Fall"],"prereqs":[],"subject":"MUSC","credits":2}
,{"_id": "MUSC 184","subid":[],"name":"SANSIFANYI ENSEMBLE","terms":["Fall","Spring"],"prereqs":["THE 168","THE 146","THE 181","THE 182","THE 283","THE 253","THE 285"],"subject":"MUSC","credits":1}
,{"_id": "MUSC 191","subid":["AME 191","DMST 121"],"name":"ART AND TECH OF RECORDING","terms":["Fall","Spring"],"prereqs":[],"subject":"MUSC","credits":4}
,{"_id": "MUSC 192","subid":["AME 192","DMST 122"],"name":"CRITICAL LISTENING AND AUDIO PRODUCTION","terms":["Fall","Spring"],"prereqs":["AME 191"],"subject":"MUSC","credits":4}
,{"_id": "MUSC 193","subid":["AME 193","DMST 123"],"name":"SOUND DESIGN","terms":["Fall","Spring"],"prereqs":[],"subject":"MUSC","credits":4}
,{"_id": "MUSC 201","subid":[],"name":"BASIC JAZZ THEORY &AMP; IMPROV I","terms":["Fall"],"prereqs":[],"subject":"MUSC","credits":2}
,{"_id": "MUSC 204","subid":[],"name":"CARILLON","terms":["Fall","Spring"],"prereqs":["MUSC 204","MUSC 104"],"subject":"MUSC","credits":4}
,{"_id": "MUSC 210","subid":["AAAS 210","DANC 212","MUSC 410"],"name":"NGOMA:DRUM, DANCE, S AFRICA","terms":["Fall"],"prereqs":[],"subject":"MUSC","credits":4}
,{"_id": "MUSC 211","subid":[],"name":"THEORY III","terms":["Fall"],"prereqs":[],"subject":"MUSC","credits":4}
,{"_id": "MUSC 221","subid":[],"name":"HISTORY OF WESTERN MUSIC TO 1600","terms":["Fall"],"prereqs":["THE 111"],"subject":"MUSC","credits":4}
,{"_id": "MUSC 223","subid":[],"name":"HISTORY OF WESTERN MUSIC 1800 - PRESENT","terms":["Fall"],"prereqs":[],"subject":"MUSC","credits":4}
,{"_id": "MUSC 237","subid":["ALC 235","ALC 435"],"name":"EXPLORING TECHNOLOGICAL APPLICATIONS IN MUSIC","terms":["Fall"],"prereqs":[],"subject":"MUSC","credits":1}
,{"_id": "MUSC 275","subid":["AAAS 275","CLTR 275A","JPNS 275"],"name":"HIP HOP JAPAN","terms":["Fall"],"prereqs":[],"subject":"MUSC","credits":4}
,{"_id": "MUSC 390","subid":[],"name":"SUPERVISED TEACHING","terms":["Fall"],"prereqs":[],"subject":"MUSC","credits":4}
,{"_id": "MUSC 394","subid":[],"name":"INTERNSHIP","terms":["Fall"],"prereqs":[],"subject":"MUSC","credits":4}
,{"_id": "MUSC 112","subid":[],"name":"THEORY II","terms":["Spring"],"prereqs":["MUSC 111"],"subject":"MUSC","credits":4}
,{"_id": "MUSC 119","subid":[],"name":"BEG PIANO CLASS","terms":["Spring"],"prereqs":[],"subject":"MUSC","credits":2}
,{"_id": "MUSC 127A","subid":["AAAS 124"],"name":"AMERICAN PROTEST MUSIC","terms":["Spring"],"prereqs":[],"subject":"MUSC","credits":4}
,{"_id": "MUSC 128","subid":["FMST 261"],"name":"FILM MUSIC","terms":["Spring"],"prereqs":[],"subject":"MUSC","credits":4}
,{"_id": "MUSC 129","subid":[],"name":"MUSIC OF THE ROLLING STONES","terms":["Spring"],"prereqs":[],"subject":"MUSC","credits":4}
,{"_id": "MUSC 132","subid":[],"name":"STARMAKERS: INSIDE PUB","terms":["Spring"],"prereqs":[],"subject":"MUSC","credits":2}
,{"_id": "MUSC 136","subid":[],"name":"EXPLORING CLASSICAL MUSIC","terms":["Spring"],"prereqs":[],"subject":"MUSC","credits":4}
,{"_id": "MUSC 139","subid":["AAAS 140","RELC 168"],"name":"RELIGION AND BLACK POP MUSIC","terms":["Spring"],"prereqs":[],"subject":"MUSC","credits":4}
,{"_id": "MUSC 143","subid":[],"name":"STORY &AMP; NARRATIVE IN SYMPHONIC MUSIC","terms":["Spring"],"prereqs":[],"subject":"MUSC","credits":4}
,{"_id": "MUSC 162","subid":["BCSC 260","TH 260","TH 460"],"name":"MUSIC &AMP; THE MIND","terms":["Spring"],"prereqs":["THE 101","THE 110","THE 111"],"subject":"MUSC","credits":4}
,{"_id": "MUSC 164","subid":["JCM 152"],"name":"JAZZ PERFORMANCE WORKSHOP","terms":["Spring"],"prereqs":[],"subject":"MUSC","credits":2}
,{"_id": "MUSC 171","subid":[],"name":"ARRANGING","terms":["Spring"],"prereqs":[],"subject":"MUSC","credits":4}
,{"_id": "MUSC 194","subid":["AME 194","AME 461"],"name":"AUDIO FOR VISUAL MEDIA","terms":["Spring"],"prereqs":["AME 193"],"subject":"MUSC","credits":4}
,{"_id": "MUSC 202","subid":[],"name":"JAZZ THEORY &AMP; IMPROV II","terms":["Spring"],"prereqs":[],"subject":"MUSC","credits":2}
,{"_id": "MUSC 207","subid":["GRMN 217","RELC 287"],"name":"HILDEGARD OF BINGEN AND HER WORLD","terms":["Spring"],"prereqs":["THE 109","THE 117","THE 800"],"subject":"MUSC","credits":4}
,{"_id": "MUSC 212C","subid":[],"name":"ANALYSIS OF 20TH &AMP; 21ST CENTURY MUSIC","terms":["Spring"],"prereqs":[],"subject":"MUSC","credits":4}
,{"_id": "MUSC 222","subid":[],"name":"HISTORY OF WESTERN MUSIC 1600-1800","terms":["Spring"],"prereqs":[],"subject":"MUSC","credits":4}
,{"_id": "MUSC 236","subid":["AAAS 222","ANTH 240","GSWS 241","MUSC 436","PHLT 227"],"name":"MUSIC, ETHNOGRAPHY &AMP; HIV/AIDS","terms":["Spring"],"prereqs":[],"subject":"MUSC","credits":4}
,{"_id": "MUSC 395","subid":[],"name":"INDEPENDENT RESEARCH","terms":["Spring"],"prereqs":[],"subject":"MUSC","credits":0}
,{"_id": "NAVS 063","subid":["NAVS 065","NAVS 093","NAVS 094","NAVS 222","NAVS 265"],"name":"NAVAL SCIENCE LAB","terms":["Fall"],"prereqs":[],"subject":"NAVS","credits":0}
,{"_id": "NAVS 098","subid":[],"name":"NAVIGATION","terms":["Spring"],"prereqs":[],"subject":"NAVS","credits":0}
,{"_id": "NAVS 249","subid":[],"name":"NAVAL SHIPS SYSTEMS II","terms":["Spring"],"prereqs":[],"subject":"NAVS","credits":4}
,{"_id": "NAVS 250","subid":[],"name":"SEAPOWER MARITIME AFFAIRS","terms":["Spring"],"prereqs":[],"subject":"NAVS","credits":4}
,{"_id": "NAVS 251","subid":[],"name":"EVOLUTION OF WARFARE","terms":["Spring"],"prereqs":[],"subject":"NAVS","credits":4}
,{"_id": "NAVS 266","subid":[],"name":"LEADERSHIP &AMP; ETHICS","terms":["Spring"],"prereqs":[],"subject":"NAVS","credits":4}
,{"_id": "NAVS 391","subid":[],"name":"INTRO TO NAVAL SCIENCE/INDSTDY","terms":["Spring"],"prereqs":[],"subject":"NAVS","credits":4}
,{"_id": "NSCI 201","subid":["BCSC 240"],"name":"BASIC NEUROBIOLOGY","terms":["Fall"],"prereqs":["NSCI 201","BIOL 110","BIOL 112"],"subject":"NSCI","credits":4}
,{"_id": "NSCI 201P","subid":[],"name":"BASIC NEUROBIOLOGY LAB","terms":["Fall"],"prereqs":["NSCI 201","BCSC 240","BIOL 110","BIOL 112"],"subject":"NSCI","credits":1}
,{"_id": "NSCI 241","subid":["BCSC 241","BCSC 541","CVSC 241","NSC 541"],"name":"NEURONS, CIRCUITS, &AMP; SYSTEMS","terms":["Fall"],"prereqs":["BCSC 240","NSCI 201"],"subject":"NSCI","credits":4}
,{"_id": "NSCI 243","subid":["BCSC 243","BCSC 543"],"name":"NEUROCHEMICAL FOUNDATIONS OF BEHAVIOR","terms":["Fall"],"prereqs":["BCSC 240","NSCI 201","BIOL 250"],"subject":"NSCI","credits":4}
,{"_id": "NSCI 245","subid":["BCSC 245","CVSC 245"],"name":"SENSORY &AMP; MOTOR NEUROSCIENCE","terms":["Fall"],"prereqs":["NSC 201","NSC 240"],"subject":"NSCI","credits":4}
,{"_id": "NSCI 280","subid":["BCSC 280","BCSC 580"],"name":"ADVANCED TOPICS IN COGNITIVE NEUROSCIENCE","terms":["Fall"],"prereqs":["STAT 212","STAT 213","BCSC 153","NSCI 201","BCSC 240","CSC 229","NSCI 247","CSC 262","MTH 165"],"subject":"NSCI","credits":4}
,{"_id": "NSCI 301","subid":[],"name":"SENIOR SEMINAR IN NEUROSCIENCE","terms":["Fall"],"prereqs":[],"subject":"NSCI","credits":2}
,{"_id": "NSCI 390","subid":[],"name":"SUPERVISED TEACHING: NSCI 243","terms":["Fall"],"prereqs":[],"subject":"NSCI","credits":4}
,{"_id": "NSCI 394","subid":[],"name":"INTERNSHIP","terms":["Fall"],"prereqs":[],"subject":"NSCI","credits":4}
,{"_id": "NSCI 415","subid":["BCSC 570","BME 410","CSC 413","CVSC 534","ECE 410","OPT 410"],"name":"INTRODUCTION TO AUGMENTED AND VIRTUAL REALITY","terms":["Fall"],"prereqs":[],"subject":"NSCI","credits":4}
,{"_id": "NSCI 203","subid":["BCSC 203"],"name":"LAB IN NEUROBIOLOGY","terms":["Spring"],"prereqs":["NSCI 201","BCSC 240","STAT 212"],"subject":"NSCI","credits":4}
,{"_id": "NSCI 244","subid":["BCSC 244"],"name":"NEUROETHOLOGY","terms":["Spring"],"prereqs":["NSCI 201","BCSC 240"],"subject":"NSCI","credits":4}
,{"_id": "NSCI 246","subid":["BCSC 246","BCSC 546","PSYC 246"],"name":"BIOLOGY OF MENTAL DISORDERS","terms":["Spring"],"prereqs":["NSCI 201","BCSC 240"],"subject":"NSCI","credits":4}
,{"_id": "NSCI 249","subid":["BCSC 249"],"name":"DEVELOPMENTAL NEUROBIOLOGY","terms":["Spring"],"prereqs":["NSCI 201","BCSC 240"],"subject":"NSCI","credits":4}
,{"_id": "NSCI 250","subid":["BCSC 250"],"name":"ACQUIRED BRAIN DISORDERS","terms":["Spring"],"prereqs":["NSCI 201","BCSC 240"],"subject":"NSCI","credits":4}
,{"_id": "NSCI 252","subid":["BCSC 252"],"name":"FUNCTIONAL NEUROANATOMY","terms":["Spring"],"prereqs":["BIOL 110"],"subject":"NSCI","credits":4}
,{"_id": "NSCI 257","subid":["BCSC 257","BCSC 557","CSC 243","CSC 443"],"name":"ADVANCED COMPUTATIONAL NEUROSCIENCE","terms":["Spring"],"prereqs":["NSCI 247"],"subject":"NSCI","credits":4}
,{"_id": "NSCI 302","subid":[],"name":"SENIOR SEMINAR IN NEUROSCIENCE","terms":["Spring"],"prereqs":[],"subject":"NSCI","credits":2}
,{"_id": "OPT 101","subid":["EAS 105"],"name":"INTRO TO OPTICS","terms":["Fall"],"prereqs":[],"subject":"OPT","credits":4}
,{"_id": "OPT 201","subid":[],"name":"GEOMETRICAL OPTICS LAB","terms":["Fall"],"prereqs":[],"subject":"OPT","credits":2}
,{"_id": "OPT 203","subid":[],"name":"INSTRUMENTATION LAB LECTURE","terms":["Fall"],"prereqs":[],"subject":"OPT","credits":2}
,{"_id": "OPT 212","subid":[],"name":"MATLAB FOR OPT MAJORS II LEC","terms":["Fall"],"prereqs":["OPT 211"],"subject":"OPT","credits":2}
,{"_id": "OPT 241","subid":[],"name":"GEOMETRICAL OPTICS","terms":["Fall"],"prereqs":[],"subject":"OPT","credits":4}
,{"_id": "OPT 242","subid":[],"name":"ABERRATIONS, INTRFER METRS","terms":["Fall"],"prereqs":["OPT 241","OPT 261"],"subject":"OPT","credits":4}
,{"_id": "OPT 243","subid":["ME 224"],"name":"OPTICAL FAB. AND TESTING","terms":["Fall"],"prereqs":[],"subject":"OPT","credits":4}
,{"_id": "OPT 245","subid":["ME 245","ME 445","OPT 445","TME 445"],"name":"PRECISION INSTRUMENT DESIGN","terms":["Fall"],"prereqs":[],"subject":"OPT","credits":4}
,{"_id": "OPT 246","subid":["OPT 446"],"name":"OPTICAL INTERFERENCE COATING","terms":["Fall"],"prereqs":["OPT 262"],"subject":"OPT","credits":4}
,{"_id": "OPT 253","subid":[],"name":"QUANTUM &AMP; NANO OPT LAB","terms":["Fall"],"prereqs":[],"subject":"OPT","credits":4}
,{"_id": "OPT 262","subid":["PHYS 262"],"name":"ELECTROMAGNETIC THEORY","terms":["Fall"],"prereqs":[],"subject":"OPT","credits":4}
,{"_id": "OPT 310","subid":["OPT 320"],"name":"SENIOR DESIGN I","terms":["Fall"],"prereqs":[],"subject":"OPT","credits":4}
,{"_id": "OPT 390","subid":[],"name":"SUPERVISED TEACHING: OPT 201","terms":["Fall"],"prereqs":[],"subject":"OPT","credits":2}
,{"_id": "OPT 401","subid":[],"name":"HOME FIRST LABORATORY","terms":["Fall","Summer","Spring"],"prereqs":[],"subject":"OPT","credits":1}
,{"_id": "OPT 402","subid":[],"name":"HOME SECOND LABORATORY","terms":["Fall","Summer"],"prereqs":[],"subject":"OPT","credits":1}
,{"_id": "OPT 410","subid":["BCSC 570","BME 410","CSC 413","CVSC 534","ECE 410","NSCI 415"],"name":"INTRODUCTION TO AUGMENTED AND VIRTUAL REALITY","terms":["Fall"],"prereqs":[],"subject":"OPT","credits":4}
,{"_id": "OPT 411","subid":["CHE 414","PHYS 401"],"name":"MATH METHODS OF OPTICS &AMP; PHY","terms":["Fall"],"prereqs":[],"subject":"OPT","credits":4}
,{"_id": "OPT 413","subid":["DSCC 420","ECE 271","ECE 440","TEE 440"],"name":"INTRO TO RANDOM PROCESSES","terms":["Fall"],"prereqs":["ECE 242"],"subject":"OPT","credits":4}
,{"_id": "OPT 425","subid":["TEO 425"],"name":"RADIATION &AMP; DETECTORS","terms":["Fall"],"prereqs":[],"subject":"OPT","credits":4}
,{"_id": "OPT 426","subid":["CHE 446","MSC 446"],"name":"LIQUID CRYSTAL MATERIALS 1","terms":["Fall"],"prereqs":[],"subject":"OPT","credits":2}
,{"_id": "OPT 428","subid":[],"name":"OPTICAL COMMUNICATIONS","terms":["Fall"],"prereqs":[],"subject":"OPT","credits":4}
,{"_id": "OPT 429","subid":["CHEM 456","MSC 456"],"name":"CHEM BONDS:FROM MOLCLS TO MAT","terms":["Fall","Spring"],"prereqs":[],"subject":"OPT","credits":4}
,{"_id": "OPT 441","subid":["TEO 441"],"name":"GEOMETRICAL OPTICS","terms":["Fall"],"prereqs":[],"subject":"OPT","credits":4}
,{"_id": "OPT 443","subid":[],"name":"FOUNDATIONS OF MODERN OPTICAL SYSTEMS","terms":["Fall"],"prereqs":[],"subject":"OPT","credits":4}
,{"_id": "OPT 449","subid":[],"name":"INTRODUCTION TO ILLUMINATION","terms":["Fall"],"prereqs":[],"subject":"OPT","credits":4}
,{"_id": "OPT 453","subid":["PHYS 434"],"name":"QUANTUM &AMP; NANO OPT LAB (ADVANCED)","terms":["Fall"],"prereqs":[],"subject":"OPT","credits":4}
,{"_id": "OPT 456","subid":[],"name":"OPTICS LABORATORY","terms":["Fall","Spring"],"prereqs":[],"subject":"OPT","credits":4}
,{"_id": "OPT 461","subid":[],"name":"FOURIER OPTICS","terms":["Fall"],"prereqs":[],"subject":"OPT","credits":4}
,{"_id": "OPT 463","subid":["TEO 463"],"name":"WAVE OPTICS &AMP; IMAGING","terms":["Fall"],"prereqs":[],"subject":"OPT","credits":4}
,{"_id": "OPT 464","subid":["ECE 436","MSC 437","TEE 436"],"name":"NANOPHOTONIC DEVICES","terms":["Fall","Spring"],"prereqs":[],"subject":"OPT","credits":4}
,{"_id": "OPT 466","subid":[],"name":"ULTRAFAST OPTICS AND LASER-MATTER INTERACTIONS","terms":["Fall"],"prereqs":[],"subject":"OPT","credits":4}
,{"_id": "OPT 467","subid":["PHYS 437","TEO 467"],"name":"NONLINEAR OPTICS","terms":["Fall"],"prereqs":[],"subject":"OPT","credits":4}
,{"_id": "OPT 468","subid":["ECE 426","TEO 468"],"name":"INTEGRATED PHOTONICS","terms":["Fall"],"prereqs":[],"subject":"OPT","credits":4}
,{"_id": "OPT 469","subid":[],"name":"INTRODUCTION TO MODELING IN PHOTONICS","terms":["Fall"],"prereqs":[],"subject":"OPT","credits":4}
,{"_id": "OPT 470","subid":[],"name":"GRADIENT-INDEX (GRIN) OPTICAL LENS SYSTEMS","terms":["Fall"],"prereqs":["OPT 444"],"subject":"OPT","credits":4}
,{"_id": "OPT 473","subid":[],"name":"LASER ENGINEERING","terms":["Fall"],"prereqs":[],"subject":"OPT","credits":4}
,{"_id": "OPT 477","subid":[],"name":"SINGULAR OPTICS","terms":["Fall"],"prereqs":[],"subject":"OPT","credits":4}
,{"_id": "OPT 479","subid":[],"name":"THZ PHENOMENA AND TECHNOLOGY","terms":["Fall"],"prereqs":[],"subject":"OPT","credits":4}
,{"_id": "OPT 495","subid":[],"name":"MASTER'S RESEARCH IN OPTICS","terms":["Fall","Summer","Spring"],"prereqs":[],"subject":"OPT","credits":12}
,{"_id": "OPT 503","subid":["BCSC 572","BME 501","CSC 513","CVSC 572","ECE 501","NSCI 540"],"name":"PRACTICUM IN AUGMENTED AND VIRTUAL REALITY","terms":["Fall"],"prereqs":[],"subject":"OPT","credits":4}
,{"_id": "OPT 535","subid":[],"name":"SINGULAR OPTICS","terms":["Fall"],"prereqs":[],"subject":"OPT","credits":4}
,{"_id": "OPT 544","subid":[],"name":"ADVANCED LENS DESIGN","terms":["Fall"],"prereqs":[],"subject":"OPT","credits":4}
,{"_id": "OPT 551","subid":["PHYS 531"],"name":"INTRO TO QUANTUM OPTICS","terms":["Fall"],"prereqs":[],"subject":"OPT","credits":4}
,{"_id": "OPT 595","subid":[],"name":"PHD RESEARCH IN OPTICS","terms":["Fall","Spring"],"prereqs":[],"subject":"OPT","credits":12}
,{"_id": "OPT 596","subid":[],"name":"OPTICS COLLOQUIUM","terms":["Fall","Spring"],"prereqs":[],"subject":"OPT","credits":1}
,{"_id": "OPT 897","subid":[],"name":"MASTER'S DISSERTATION","terms":["Fall","Spring"],"prereqs":[],"subject":"OPT","credits":0}
,{"_id": "OPT 899","subid":[],"name":"MASTER'S DISSERTATION","terms":["Fall","Spring"],"prereqs":[],"subject":"OPT","credits":0}
,{"_id": "OPT 997","subid":[],"name":"DOCTORAL DISSERATION","terms":["Fall","Summer","Spring"],"prereqs":[],"subject":"OPT","credits":0}
,{"_id": "OPT 999","subid":[],"name":"DOCTORAL DISSERTATION","terms":["Fall","Spring"],"prereqs":[],"subject":"OPT","credits":0}
,{"_id": "OPT 403","subid":[],"name":"HOME THIRD LABORATORY","terms":["Summer"],"prereqs":[],"subject":"OPT","credits":1}
,{"_id": "OPT 454","subid":[],"name":"OPTICS LABORATORY","terms":["Summer"],"prereqs":[],"subject":"OPT","credits":3}
,{"_id": "OPT 986V","subid":[],"name":"FULL TIME VISITING STUDENT","terms":["Summer"],"prereqs":[],"subject":"OPT","credits":0}
,{"_id": "OPT 202","subid":[],"name":"PHYSICAL OPTICS LAB","terms":["Spring"],"prereqs":[],"subject":"OPT","credits":2}
,{"_id": "OPT 204","subid":[],"name":"SOURCES AND DETECTORS LAB LECTURE","terms":["Spring"],"prereqs":["OPT 225","OPT 203"],"subject":"OPT","credits":2}
,{"_id": "OPT 214","subid":[],"name":"INTRO OPT SYS. LAYOUT/ANLYS","terms":["Spring"],"prereqs":["OPT 241"],"subject":"OPT","credits":2}
,{"_id": "OPT 222","subid":["OPT 422"],"name":"COLOR TECHNOLOGY","terms":["Spring"],"prereqs":["OPT 211"],"subject":"OPT","credits":4}
,{"_id": "OPT 223","subid":[],"name":"QUANTUM THEORY","terms":["Spring"],"prereqs":[],"subject":"OPT","credits":4}
,{"_id": "OPT 225","subid":[],"name":"SOURCES AND DETECTORS","terms":["Spring"],"prereqs":[],"subject":"OPT","credits":4}
,{"_id": "OPT 232","subid":["ME 232","ME 432","MSC 432","OPT 432","TME 432"],"name":"OPTO MECHANICAL","terms":["Spring"],"prereqs":[],"subject":"OPT","credits":4}
,{"_id": "OPT 244","subid":["OPT 444"],"name":"LENS DESIGN","terms":["Spring"],"prereqs":[],"subject":"OPT","credits":4}
,{"_id": "OPT 247","subid":["OPT 447","TEO 447"],"name":"ADVANCED OPTICAL COATINGS","terms":["Spring"],"prereqs":[],"subject":"OPT","credits":4}
,{"_id": "OPT 248","subid":["BCSC 223","OPT 448","TEO 448"],"name":"VISION AND THE EYE","terms":["Spring"],"prereqs":[],"subject":"OPT","credits":4}
,{"_id": "OPT 254","subid":["PHYS 371"],"name":"NANOMETROLOGY LABORATORY","terms":["Spring"],"prereqs":[],"subject":"OPT","credits":4}
,{"_id": "OPT 265","subid":[],"name":"INTRODUCTION TO LASERS","terms":["Spring"],"prereqs":["OPT 225"],"subject":"OPT","credits":4}
,{"_id": "OPT 272","subid":["BME 272","BME 472","OPT 472"],"name":"ADVANCED BIOMEDICAL MICROSCOPY","terms":["Spring"],"prereqs":["OPT 261","BME 270"],"subject":"OPT","credits":4}
,{"_id": "OPT 287","subid":["MATH 287"],"name":"MATH METHODS IN OPT &AMP; PHYSICS","terms":["Spring"],"prereqs":[],"subject":"OPT","credits":4}
,{"_id": "OPT 307","subid":["MSC 307","MSC 507","OPT 407"],"name":"SEM PRACTICUM","terms":["Spring"],"prereqs":[],"subject":"OPT","credits":4}
,{"_id": "OPT 311","subid":["OPT 321"],"name":"OPT SENIOR DESIGN PROJECT","terms":["Spring"],"prereqs":[],"subject":"OPT","credits":4}
,{"_id": "OPT 412","subid":["TEO 412"],"name":"QUANTUM MECHANICS - OPTICS","terms":["Spring"],"prereqs":[],"subject":"OPT","credits":4}
,{"_id": "OPT 421","subid":["ECE 421","MSC 470","TEO 421"],"name":"OPT PROPERTIES OF MATERIALS","terms":["Spring"],"prereqs":[],"subject":"OPT","credits":4}
,{"_id": "OPT 423","subid":["TEO 423"],"name":"DETECTION OF OPTCL RADIATION","terms":["Spring"],"prereqs":[],"subject":"OPT","credits":4}
,{"_id": "OPT 438","subid":["BCSC 571","BME 413","CSC 414","CVSC 535","ECE 411","NSCI 416"],"name":"SELECTED TOPICS IN AUGMENTED AND VIRTUAL REALITY","terms":["Spring"],"prereqs":["THE 202","ECE 410","NSCI 415","CSC 413","CVSC 534"],"subject":"OPT","credits":4}
,{"_id": "OPT 442","subid":["TEO 442"],"name":"INSTRUMENTAL OPTICS","terms":["Spring"],"prereqs":[],"subject":"OPT","credits":4}
,{"_id": "OPT 462","subid":["TEO 462"],"name":"ELECTROMAGNETIC WAVES","terms":["Spring"],"prereqs":[],"subject":"OPT","credits":4}
,{"_id": "OPT 465","subid":["ME 465","MSC 465","PHYS 435","TEO 465"],"name":"PRINCIPLES OF LASERS","terms":["Spring"],"prereqs":[],"subject":"OPT","credits":4}
,{"_id": "OPT 481","subid":["TEM 411"],"name":"GEN MANAGEMENT OF NEW VENTURE","terms":["Spring"],"prereqs":[],"subject":"OPT","credits":4}
,{"_id": "OPT 482","subid":["TEM 441"],"name":"PRODUCT DEVELOPMENT AND TECHNOLOGY MANAGEMENT","terms":["Spring"],"prereqs":[],"subject":"OPT","credits":4}
,{"_id": "OPT 489","subid":[],"name":"THE RETINA-BRAIN INTERFACE","terms":["Spring"],"prereqs":[],"subject":"OPT","credits":4}
,{"_id": "OPT 491","subid":[],"name":"MASTER'S READING IN OPTICS LABORATORY","terms":["Spring"],"prereqs":[],"subject":"OPT","credits":4}
,{"_id": "OPT 552","subid":["PHYS 532"],"name":"QUANTUM OPTICS OF THE ELECTROMAGNETIC FIELD","terms":["Spring"],"prereqs":["PHYS 531"],"subject":"OPT","credits":4}
,{"_id": "OPT 591","subid":[],"name":"PHD READING COURSE - INVERSE PROBLEMS IN OPTICS","terms":["Spring"],"prereqs":[],"subject":"OPT","credits":2}
,{"_id": "OPT 594","subid":[],"name":"INTERNSHIP","terms":["Spring"],"prereqs":[],"subject":"OPT","credits":1}
,{"_id": "OPT 595A","subid":[],"name":"PHD RESEARCH IN ABSENTIA","terms":["Spring"],"prereqs":[],"subject":"OPT","credits":12}
,{"_id": "OPT 595B","subid":[],"name":"PHD RSRCH IN ABSENTIA ABROAD","terms":["Spring"],"prereqs":[],"subject":"OPT","credits":12}
,{"_id": "OPT 894","subid":[],"name":"CO-OP PROGRAM IN OPTICS","terms":["Spring"],"prereqs":[],"subject":"OPT","credits":0}
,{"_id": "OPT 895","subid":[],"name":"CONT OF MASTER'S ENROLLMENT","terms":["Spring"],"prereqs":[],"subject":"OPT","credits":0}
,{"_id": "OPT 897A","subid":[],"name":"MASTERS IN ABSENTIA","terms":["Spring"],"prereqs":[],"subject":"OPT","credits":0}
,{"_id": "OPT 899A","subid":[],"name":"MASTERS DISSERTATN ABSENTIA","terms":["Spring"],"prereqs":[],"subject":"OPT","credits":0}
,{"_id": "OPT 899B","subid":[],"name":"MASTER'S IN-ABSENTIA ABROAD","terms":["Spring"],"prereqs":[],"subject":"OPT","credits":0}
,{"_id": "OPT 995","subid":[],"name":"CONT OF DOCTORAL ENROLLMENT","terms":["Spring"],"prereqs":[],"subject":"OPT","credits":0}
,{"_id": "OPT 997A","subid":[],"name":"DOCT DISSERTATN IN ABSENTIA","terms":["Spring"],"prereqs":[],"subject":"OPT","credits":0}
,{"_id": "OPT 999A","subid":[],"name":"DOCT DISSERTATN IN ABSENTIA","terms":["Spring"],"prereqs":[],"subject":"OPT","credits":0}
,{"_id": "OPT 999B","subid":[],"name":"DOC DISS IN-ABSENTIA ABROAD","terms":["Spring"],"prereqs":[],"subject":"OPT","credits":0}
,{"_id": "PHIL 101","subid":[],"name":"INTRODUCTION TO PHILOSOPHY","terms":["Fall","Summer","Spring"],"prereqs":[],"subject":"PHIL","credits":4}
,{"_id": "PHIL 102","subid":[],"name":"ETHICS","terms":["Fall","Spring"],"prereqs":[],"subject":"PHIL","credits":4}
,{"_id": "PHIL 103","subid":["EHUM 103","SUST 114"],"name":"MORAL PROBLEMS","terms":["Fall","Summer","Spring"],"prereqs":[],"subject":"PHIL","credits":4}
,{"_id": "PHIL 105","subid":[],"name":"REASON AND ARGUMENT","terms":["Fall"],"prereqs":[],"subject":"PHIL","credits":4}
,{"_id": "PHIL 110","subid":[],"name":"INTRODUCTORY LOGIC","terms":["Fall","Spring"],"prereqs":[],"subject":"PHIL","credits":4}
,{"_id": "PHIL 135","subid":[],"name":"ENVIRONMENTAL ETHICS","terms":["Fall"],"prereqs":[],"subject":"PHIL","credits":4}
,{"_id": "PHIL 152","subid":[],"name":"SCIENCE AND REASON","terms":["Fall"],"prereqs":[],"subject":"PHIL","credits":4}
,{"_id": "PHIL 202","subid":[],"name":"HISTORY OF MODERN PHILOSOPHY","terms":["Fall"],"prereqs":[],"subject":"PHIL","credits":4}
,{"_id": "PHIL 218","subid":["PHIL 418"],"name":"PHILOSOPHY OF MATHEMATICS","terms":["Fall"],"prereqs":[],"subject":"PHIL","credits":4}
,{"_id": "PHIL 223","subid":["PHIL 223W","SUST 223"],"name":"SOCIAL &AMP; POLITICAL PHILOSOPHY","terms":["Fall"],"prereqs":[],"subject":"PHIL","credits":4}
,{"_id": "PHIL 229","subid":["PHIL 229W","PHIL 429"],"name":"PHILOSOPHY OF EDUCATION","terms":["Fall"],"prereqs":[],"subject":"PHIL","credits":4}
,{"_id": "PHIL 243","subid":["PHIL 243W","PHIL 443"],"name":"THEORY OF KNOWLEDGE","terms":["Fall"],"prereqs":[],"subject":"PHIL","credits":4}
,{"_id": "PHIL 247","subid":["LING 245","LING 445","PHIL 247W","PHIL 447"],"name":"PHILOSOPHY OF LANGUAGE","terms":["Fall"],"prereqs":["PHIL 110"],"subject":"PHIL","credits":4}
,{"_id": "PHIL 257","subid":["PHIL 257W","PHIL 457"],"name":"PHILOSOPHY OF ARTIFICIAL INTELLIGENCE","terms":["Fall"],"prereqs":[],"subject":"PHIL","credits":4}
,{"_id": "PHIL 261","subid":["PHIL 261W","PHIL 461"],"name":"KANT","terms":["Fall"],"prereqs":[],"subject":"PHIL","credits":4}
,{"_id": "PHIL 392","subid":[],"name":"PRACTICUM","terms":["Fall"],"prereqs":[],"subject":"PHIL","credits":4}
,{"_id": "PHIL 396","subid":[],"name":"HONORS TUTORIAL","terms":["Fall","Spring"],"prereqs":[],"subject":"PHIL","credits":4}
,{"_id": "PHIL 399","subid":[],"name":"HONORS THESIS","terms":["Fall","Spring"],"prereqs":[],"subject":"PHIL","credits":4}
,{"_id": "PHIL 428","subid":["PHIL 228","PHIL 228W","SUST 228"],"name":"PUBLIC HEALTH ETHICS","terms":["Fall"],"prereqs":[],"subject":"PHIL","credits":4}
,{"_id": "PHIL 464","subid":[],"name":"PHILOSOPHICAL READINGS IN ANCIENT GREEK","terms":["Fall"],"prereqs":[],"subject":"PHIL","credits":0}
,{"_id": "PHIL 470","subid":[],"name":"SELECTED TOPICS IN MODERN PHILOSOPHY","terms":["Fall"],"prereqs":[],"subject":"PHIL","credits":4}
,{"_id": "PHIL 491","subid":[],"name":"MASTER'S READINGS IN PHL","terms":["Fall","Spring"],"prereqs":[],"subject":"PHIL","credits":5}
,{"_id": "PHIL 517","subid":[],"name":"SELECTED TOPICS IN ETHICS","terms":["Fall","Spring"],"prereqs":[],"subject":"PHIL","credits":4}
,{"_id": "PHIL 523","subid":[],"name":"LIVING UNDER OPPRESSION","terms":["Fall"],"prereqs":[],"subject":"PHIL","credits":4}
,{"_id": "PHIL 542","subid":[],"name":"METAPHYSICS","terms":["Fall"],"prereqs":[],"subject":"PHIL","credits":4}
,{"_id": "PHIL 560","subid":[],"name":"WRITING SEMINAR","terms":["Fall","Spring"],"prereqs":[],"subject":"PHIL","credits":4}
,{"_id": "PHIL 581","subid":[],"name":"SUPERVISE INSTRUCT:LEC TO UN","terms":["Fall","Spring"],"prereqs":[],"subject":"PHIL","credits":4}
,{"_id": "PHIL 591","subid":[],"name":"PHD READINGS IN PHL","terms":["Fall","Spring"],"prereqs":[],"subject":"PHIL","credits":5}
,{"_id": "PHIL 595","subid":[],"name":"PHD RESEARCH IN PHL","terms":["Fall","Spring"],"prereqs":[],"subject":"PHIL","credits":12}
,{"_id": "PHIL 895","subid":[],"name":"CONT OF MASTER'S ENROLLMENT","terms":["Fall"],"prereqs":[],"subject":"PHIL","credits":0}
,{"_id": "PHIL 897","subid":[],"name":"MASTER'S DISSERTATION","terms":["Fall","Spring"],"prereqs":[],"subject":"PHIL","credits":0}
,{"_id": "PHIL 986V","subid":[],"name":"FULL TIME VISITING STUDENT","terms":["Fall","Summer"],"prereqs":[],"subject":"PHIL","credits":0}
,{"_id": "PHIL 995","subid":[],"name":"CONT OF DOCTORAL ENROLLMENT","terms":["Fall","Spring"],"prereqs":[],"subject":"PHIL","credits":0}
,{"_id": "PHIL 997","subid":[],"name":"DOCTORAL DISSERTATION","terms":["Fall","Spring"],"prereqs":[],"subject":"PHIL","credits":0}
,{"_id": "PHIL 999","subid":[],"name":"DOCTORAL DISSERTATION","terms":["Fall","Spring"],"prereqs":[],"subject":"PHIL","credits":0}
,{"_id": "PHIL 120","subid":["EAS 145"],"name":"ETHICS OF TECHNOLOGY","terms":["Spring"],"prereqs":[],"subject":"PHIL","credits":4}
,{"_id": "PHIL 201","subid":["CLST 203"],"name":"HISTORY OF ANCIENT PHILOSOPHY","terms":["Spring"],"prereqs":[],"subject":"PHIL","credits":4}
,{"_id": "PHIL 215","subid":["MATH 225","PHIL 415"],"name":"INTERMEDIATE LOGIC","terms":["Spring"],"prereqs":[],"subject":"PHIL","credits":4}
,{"_id": "PHIL 220","subid":["PHIL 420"],"name":"RECENT ETHICAL THEORY","terms":["Spring"],"prereqs":[],"subject":"PHIL","credits":4}
,{"_id": "PHIL 225","subid":["PHIL 225W"],"name":"ETHICAL DECISIONS IN MEDICINE","terms":["Spring"],"prereqs":[],"subject":"PHIL","credits":4}
,{"_id": "PHIL 226","subid":["PHIL 226W","PHIL 426"],"name":"PHILOSOPHY OF LAW","terms":["Spring"],"prereqs":[],"subject":"PHIL","credits":4}
,{"_id": "PHIL 235","subid":["PHIL 235W","PHIL 435"],"name":"DATA, ALGORITHMS, JUSTICE","terms":["Spring"],"prereqs":[],"subject":"PHIL","credits":4}
,{"_id": "PHIL 250","subid":["PHIL 250W","PHIL 450"],"name":"PHILOSOPHY OF ACTION","terms":["Spring"],"prereqs":[],"subject":"PHIL","credits":4}
,{"_id": "PHIL 252","subid":["PHIL 252W","PHIL 452"],"name":"PHILOSOPHY OF SCIENCE","terms":["Spring"],"prereqs":[],"subject":"PHIL","credits":4}
,{"_id": "PHIL 311","subid":["PHLT 300W"],"name":"SEMINAR IN BIOETHICS","terms":["Spring"],"prereqs":[],"subject":"PHIL","credits":4}
,{"_id": "PHIL 321","subid":[],"name":"DEATH","terms":["Spring"],"prereqs":[],"subject":"PHIL","credits":4}
,{"_id": "PHIL 393","subid":[],"name":"SEMINAR FOR MAJORS","terms":["Spring"],"prereqs":[],"subject":"PHIL","credits":4}
,{"_id": "PHIL 397","subid":[],"name":"SPECIAL PROJECTS","terms":["Spring"],"prereqs":[],"subject":"PHIL","credits":4}
,{"_id": "PHIL 398","subid":[],"name":"SPECIAL TOPICS","terms":["Spring"],"prereqs":[],"subject":"PHIL","credits":4}
,{"_id": "PHIL 495","subid":[],"name":"MASTER'S THESIS RESEARCH","terms":["Spring"],"prereqs":[],"subject":"PHIL","credits":10}
,{"_id": "PHIL 516","subid":[],"name":"SEL TOP PHL OF LANGUAGE","terms":["Spring"],"prereqs":[],"subject":"PHIL","credits":4}
,{"_id": "PHIL 595A","subid":[],"name":"PHD RESEARCH IN ABSENTIA","terms":["Spring"],"prereqs":[],"subject":"PHIL","credits":5}
,{"_id": "PHIL 997A","subid":[],"name":"DOCT DISSERTATN IN ABSENTIA","terms":["Spring"],"prereqs":[],"subject":"PHIL","credits":0}
,{"_id": "PHIL 999A","subid":[],"name":"DOCT DISSERTATN IN ABSENTIA","terms":["Spring"],"prereqs":[],"subject":"PHIL","credits":0}
,{"_id": "PHLT 103","subid":[],"name":"CONCEPTS OF EPIDEMIOLOGY","terms":["Fall"],"prereqs":[],"subject":"PHLT","credits":4}
,{"_id": "PHLT 218","subid":[],"name":"INTRODUCTION TO HEALTH POLICY MAKING","terms":["Fall"],"prereqs":[],"subject":"PHLT","credits":2}
,{"_id": "PHLT 299B","subid":[],"name":"FIELD ANALYSIS IN PUBLIC HEALTH","terms":["Fall"],"prereqs":[],"subject":"PHLT","credits":2}
,{"_id": "PHLT 389","subid":[],"name":"PUBLIC HEALTH HONORS SEMINAR","terms":["Fall","Spring"],"prereqs":[],"subject":"PHLT","credits":1}
,{"_id": "PHLT 394","subid":[],"name":"INTERNSHIP","terms":["Fall"],"prereqs":[],"subject":"PHLT","credits":4}
,{"_id": "PHLT 394C","subid":[],"name":"WASHINGTON SEMESTER INTERNSHIP","terms":["Fall","Spring"],"prereqs":[],"subject":"PHLT","credits":12}
,{"_id": "PHLT 397W","subid":[],"name":"COMMUNITY ENGAGED INTERNSHIP","terms":["Fall","Spring"],"prereqs":[],"subject":"PHLT","credits":4}
,{"_id": "PHLT 399","subid":[],"name":"WASHINGTON SEMESTER","terms":["Fall","Spring"],"prereqs":[],"subject":"PHLT","credits":4}
,{"_id": "PHLT 101","subid":["SUST 112"],"name":"INTRO TO PUBLIC HEALTH","terms":["Spring"],"prereqs":[],"subject":"PHLT","credits":4}
,{"_id": "PHLT 102","subid":[],"name":"INTRO TO PUBLIC HEALTH II","terms":["Spring"],"prereqs":[],"subject":"PHLT","credits":4}
,{"_id": "PHLT 180","subid":["RELC 180"],"name":"RELIGION AND PUBLIC HEALTH: COLLABORATION ON THE FRONT LINES","terms":["Spring"],"prereqs":[],"subject":"PHLT","credits":4}
,{"_id": "PHLT 201W","subid":["SUST 210"],"name":"ENVIRONMENTAL HEALTH","terms":["Spring"],"prereqs":[],"subject":"PHLT","credits":4}
,{"_id": "PHLT 215W","subid":["ANTH 215"],"name":"PUBLIC HEALTH ANTHROPOLOGY","terms":["Spring"],"prereqs":[],"subject":"PHLT","credits":4}
,{"_id": "PHLT 227","subid":["AAAS 222","ANTH 240","GSWS 241","MUSC 236","MUSC 436"],"name":"MUSIC, ETHNOGRAPHY &AMP; HIV/AIDS","terms":["Spring"],"prereqs":[],"subject":"PHLT","credits":4}
,{"_id": "PHLT 230","subid":["PSCI 230"],"name":"PUBLIC HEALTH LAW AND POLICY","terms":["Spring"],"prereqs":[],"subject":"PHLT","credits":4}
,{"_id": "PHLT 234W","subid":["PSCI 231W"],"name":"MATERNAL CHILD HEALTH POLICY","terms":["Spring"],"prereqs":[],"subject":"PHLT","credits":4}
,{"_id": "PHLT 238","subid":["PSCI 216"],"name":"ENVIRONMENTAL HEALTH AND JUSTICE IN THE ROCHESTER COMMUNITY","terms":["Spring"],"prereqs":[],"subject":"PHLT","credits":4}
,{"_id": "PHLT 265W","subid":["ANTH 265"],"name":"GLOBAL HEALTH","terms":["Spring"],"prereqs":[],"subject":"PHLT","credits":4}
,{"_id": "PHLT 299A","subid":[],"name":"FIELD WORK METHODS IN PUBLIC HEALTH","terms":["Spring"],"prereqs":[],"subject":"PHLT","credits":2}
,{"_id": "PHLT 300W","subid":["PHIL 311"],"name":"SEMINAR ON BIOETHICS","terms":["Spring"],"prereqs":[],"subject":"PHLT","credits":4}
,{"_id": "PHLT 374","subid":["HIST 374W","HIST 474","PSCI 316W"],"name":"PANDEMICS, POLITICS AND POLICIES","terms":["Spring"],"prereqs":[],"subject":"PHLT","credits":4}
,{"_id": "PHLT 393","subid":[],"name":"PUBLIC HEALTH RESEARCH HONORS","terms":["Spring"],"prereqs":[],"subject":"PHLT","credits":3}
,{"_id": "PHLT 394E","subid":[],"name":"EMERGENCY MEDICINE INTERNSHIP","terms":["Spring"],"prereqs":[],"subject":"PHLT","credits":4}
,{"_id": "PHLT 394F","subid":["PSCI 394F"],"name":"HEALTH POLICY INTERNSHIP","terms":["Spring"],"prereqs":[],"subject":"PHLT","credits":4}
,{"_id": "PHYS 081","subid":[],"name":"MECHANICS LAB - MONDAY 450-730PM - WEEK A","terms":["Fall","Summer","Spring"],"prereqs":[],"subject":"PHYS","credits":0}
,{"_id": "PHYS 082","subid":[],"name":"E&AMP;M LAB - MONDAY 200-440PM - WEEK A","terms":["Fall","Summer"],"prereqs":[],"subject":"PHYS","credits":0}
,{"_id": "PHYS 084","subid":[],"name":"GENERAL PHYSICS II LAB - FRIDAY 200-440PM - WEEK A","terms":["Fall","Summer","Spring"],"prereqs":[],"subject":"PHYS","credits":0}
,{"_id": "PHYS 099","subid":[],"name":"INTRO MATH METHODS IN SCIENCE &AMP; ENGINEERING","terms":["Fall"],"prereqs":["THE 121"],"subject":"PHYS","credits":0}
,{"_id": "PHYS 109","subid":[],"name":"QUANTUM WORLD","terms":["Fall"],"prereqs":[],"subject":"PHYS","credits":4}
,{"_id": "PHYS 113","subid":[],"name":"GENERAL PHYSICS I","terms":["Fall","Summer","Spring"],"prereqs":["SPAN 141","SPAN 161","PHYS 081"],"subject":"PHYS","credits":4}
,{"_id": "PHYS 114","subid":[],"name":"GENERAL PHYSICS II","terms":["Fall","Summer","Spring"],"prereqs":["PHYS 113","MTH 143","MTH 162","PHYS 084"],"subject":"PHYS","credits":4}
,{"_id": "PHYS 122","subid":[],"name":"ELECTRICITY &AMP; MAGNETISM","terms":["Fall","Summer"],"prereqs":["SPAN 143","SPAN 162","EAS 101","EAS 102","EAS 103","EAS 104","EAS 105","EAS 108","PHYS 082"],"subject":"PHYS","credits":4}
,{"_id": "PHYS 122P","subid":[],"name":"ELECTRICITY &AMP; MAGNETISM SELF PACED","terms":["Fall"],"prereqs":["SPAN 143","SPAN 162","EAS 101","EAS 102","EAS 103","EAS 104","EAS 105","EAS 108","PHYS 082","THE 202","THE 109"],"subject":"PHYS","credits":4}
,{"_id": "PHYS 141","subid":[],"name":"MECHANICS (HONORS)","terms":["Fall"],"prereqs":[],"subject":"PHYS","credits":4}
,{"_id": "PHYS 142","subid":[],"name":"ELECTRICITY &AMP; MAGNETISM (HONORS)","terms":["Fall"],"prereqs":["THE 121","THE 162","THE 172","THE 143","THE 142","THE 122","PHYS 082"],"subject":"PHYS","credits":4}
,{"_id": "PHYS 181","subid":[],"name":"MECHANICS LABORATORY","terms":["Fall","Spring"],"prereqs":[],"subject":"PHYS","credits":1}
,{"_id": "PHYS 182","subid":[],"name":"ELEC &AMP; MAGNETISM LAB","terms":["Fall","Spring"],"prereqs":[],"subject":"PHYS","credits":1}
,{"_id": "PHYS 184","subid":[],"name":"E/M AND MODERN PHYSICS LAB","terms":["Fall","Spring"],"prereqs":[],"subject":"PHYS","credits":1}
,{"_id": "PHYS 217","subid":[],"name":"ADVANCED ELECTRICITY &AMP; MAGNETISM I","terms":["Fall"],"prereqs":[],"subject":"PHYS","credits":4}
,{"_id": "PHYS 235W","subid":[],"name":"CLASSICAL MECHANICS I","terms":["Fall"],"prereqs":[],"subject":"PHYS","credits":4}
,{"_id": "PHYS 243W","subid":[],"name":"ADVANCED EXPERIMENTAL TECHNIQUES I","terms":["Fall"],"prereqs":[],"subject":"PHYS","credits":4}
,{"_id": "PHYS 251","subid":[],"name":"INTRO TO CONDENSED MATTER PHYSICS","terms":["Fall"],"prereqs":[],"subject":"PHYS","credits":4}
,{"_id": "PHYS 254","subid":[],"name":"NUCLEAR &AMP; PARTICLE PHYSICS","terms":["Fall"],"prereqs":["THE 440"],"subject":"PHYS","credits":4}
,{"_id": "PHYS 255","subid":["ME 225"],"name":"INTRO FLUID DYNAMICS","terms":["Fall"],"prereqs":[],"subject":"PHYS","credits":4}
,{"_id": "PHYS 257","subid":["BME 253","BME 453","ECE 251","ECE 453","PHYS 467","TEB 453"],"name":"ULTRASOUND IMAGING","terms":["Fall"],"prereqs":[],"subject":"PHYS","credits":4}
,{"_id": "PHYS 262","subid":["OPT 262"],"name":"ELECTROMAGNETIC THEORY","terms":["Fall"],"prereqs":[],"subject":"PHYS","credits":4}
,{"_id": "PHYS 373","subid":["PHYS 573"],"name":"PHYSICS AND FINANCE","terms":["Fall"],"prereqs":[],"subject":"PHYS","credits":4}
,{"_id": "PHYS 390A","subid":[],"name":"SUPERVISED TEACHING-PAS DEPARTMENT","terms":["Fall","Spring"],"prereqs":[],"subject":"PHYS","credits":2}
,{"_id": "PHYS 401","subid":["CHE 414","OPT 411"],"name":"MATH METH OF OPTICS &AMP; PHY","terms":["Fall"],"prereqs":[],"subject":"PHYS","credits":4}
,{"_id": "PHYS 405","subid":[],"name":"GEOMETRICAL METHODS OF PHYS","terms":["Fall"],"prereqs":[],"subject":"PHYS","credits":4}
,{"_id": "PHYS 407","subid":[],"name":"QUANTUM MECHANICS I","terms":["Fall"],"prereqs":[],"subject":"PHYS","credits":4}
,{"_id": "PHYS 411","subid":[],"name":"ADVANCED MECHANICS","terms":["Fall"],"prereqs":[],"subject":"PHYS","credits":4}
,{"_id": "PHYS 415","subid":[],"name":"ELECTROMAGNETIC THEORY I","terms":["Fall"],"prereqs":[],"subject":"PHYS","credits":4}
,{"_id": "PHYS 434","subid":["OPT 453"],"name":"QUANTUM &AMP; NANO OPT LAB (ADVANCED)","terms":["Fall"],"prereqs":[],"subject":"PHYS","credits":4}
,{"_id": "PHYS 437","subid":["OPT 467","TEO 467"],"name":"NONLINEAR OPTICS","terms":["Fall"],"prereqs":[],"subject":"PHYS","credits":4}
,{"_id": "PHYS 440","subid":[],"name":"NUCLEAR &AMP; PARTICLE PHYSICS","terms":["Fall"],"prereqs":[],"subject":"PHYS","credits":4}
,{"_id": "PHYS 453","subid":["ME 537"],"name":"INTRODUCTION TO HIGH ENERGY DENSITY PHYSICS","terms":["Fall"],"prereqs":[],"subject":"PHYS","credits":4}
,{"_id": "PHYS 454","subid":["ME 434","TME 434"],"name":"INTRO TO PLASMA PHYSICS I","terms":["Fall"],"prereqs":[],"subject":"PHYS","credits":4}
,{"_id": "PHYS 498","subid":[],"name":"SUPERVISED TEACHING ASST I","terms":["Fall"],"prereqs":[],"subject":"PHYS","credits":0}
,{"_id": "PHYS 499","subid":[],"name":"SUPERVISED TEACHING ASST II","terms":["Fall","Spring"],"prereqs":[],"subject":"PHYS","credits":0}
,{"_id": "PHYS 521","subid":[],"name":"CONDENSED MATTER I","terms":["Fall"],"prereqs":[],"subject":"PHYS","credits":4}
,{"_id": "PHYS 525","subid":[],"name":"DATA SCIENCE II: COMPLEXITY","terms":["Fall"],"prereqs":[],"subject":"PHYS","credits":4}
,{"_id": "PHYS 581","subid":[],"name":"PARTICLE PHYSICS I","terms":["Fall"],"prereqs":[],"subject":"PHYS","credits":4}
,{"_id": "PHYS 594","subid":[],"name":"INTERNSHIP","terms":["Fall","Summer","Spring"],"prereqs":[],"subject":"PHYS","credits":1}
,{"_id": "PHYS 595","subid":[],"name":"PHD RESEARCH IN PHYSICS","terms":["Fall","Summer","Spring"],"prereqs":[],"subject":"PHYS","credits":12}
,{"_id": "PHYS 597","subid":[],"name":"RESEARCH SEMINAR","terms":["Fall","Spring"],"prereqs":[],"subject":"PHYS","credits":0}
,{"_id": "PHYS 598","subid":[],"name":"TEACH WRKSHP LDR PEDAGOGY","terms":["Fall"],"prereqs":[],"subject":"PHYS","credits":0}
,{"_id": "PHYS 599","subid":[],"name":"PEDAGOGY&AMP;GROUP LEADERSHIP","terms":["Fall","Spring"],"prereqs":[],"subject":"PHYS","credits":0}
,{"_id": "PHYS 895","subid":[],"name":"CONT OF MASTER'S ENROLLMENT","terms":["Fall","Spring"],"prereqs":[],"subject":"PHYS","credits":0}
,{"_id": "PHYS 995","subid":[],"name":"CONT OF DOCTORAL ENROLLMENT","terms":["Fall","Spring"],"prereqs":[],"subject":"PHYS","credits":0}
,{"_id": "PHYS 997","subid":[],"name":"DOCTORAL DISSERTATION","terms":["Fall","Summer","Spring"],"prereqs":[],"subject":"PHYS","credits":0}
,{"_id": "PHYS 999","subid":[],"name":"DOCTORAL DISSERTATION","terms":["Fall","Spring"],"prereqs":[],"subject":"PHYS","credits":0}
,{"_id": "PHYS 047","subid":[],"name":"CULTURE OF RESEARCH IN SCIENCE","terms":["Summer"],"prereqs":[],"subject":"PHYS","credits":0}
,{"_id": "PHYS 121","subid":["PHYS 121S"],"name":"MECHANICS","terms":["Summer","Spring"],"prereqs":["PHYS 081","SPAN 099","SPAN 161","SPAN 162","EAS 101","EAS 102","EAS 103","EAS 104","EAS 105","EAS 108"],"subject":"PHYS","credits":4}
,{"_id": "PHYS 497","subid":[],"name":"CERTIFICATE IN COLL TEACHING","terms":["Summer"],"prereqs":[],"subject":"PHYS","credits":0}
,{"_id": "PHYS 897","subid":[],"name":"MASTERS DISSERTATION","terms":["Summer"],"prereqs":[],"subject":"PHYS","credits":0}
,{"_id": "PHYS 986V","subid":[],"name":"FULL TIME VISITING STUDENT","terms":["Summer"],"prereqs":[],"subject":"PHYS","credits":0}
,{"_id": "PHYS 113P","subid":[],"name":"GEN PHYSICS I (SELF-PACED)","terms":["Spring"],"prereqs":["PHYS 081","MTH 141","MTH 161"],"subject":"PHYS","credits":4}
,{"_id": "PHYS 121P","subid":[],"name":"MECHANICS (SELF-PACED)","terms":["Spring"],"prereqs":["PHYS 081","SPAN 099","SPAN 161","SPAN 162","EAS 101","EAS 102","EAS 103","EAS 104","EAS 105","EAS 108","THE 121","THE 122"],"subject":"PHYS","credits":4}
,{"_id": "PHYS 123","subid":[],"name":"WAVES AND MODERN PHYSICS","terms":["Spring"],"prereqs":["PHYS 083","SPAN 122","SPAN 163","SPAN 165"],"subject":"PHYS","credits":4}
,{"_id": "PHYS 143","subid":[],"name":"20TH CENTURY PHYSICS","terms":["Spring"],"prereqs":["THE 123","SPAN 141","THE 162"],"subject":"PHYS","credits":4}
,{"_id": "PHYS 183","subid":[],"name":"WAVES &AMP; MODERN PHYSICS LAB","terms":["Spring"],"prereqs":[],"subject":"PHYS","credits":1}
,{"_id": "PHYS 218","subid":[],"name":"E &AMP; M II","terms":["Spring"],"prereqs":["SPAN 217"],"subject":"PHYS","credits":4}
,{"_id": "PHYS 227","subid":[],"name":"THERMO &AMP; STAT MECHANICS","terms":["Spring"],"prereqs":["SPAN 237","SPAN 281"],"subject":"PHYS","credits":4}
,{"_id": "PHYS 233","subid":["AME 233","ECE 233","ECE 433","TEE 433"],"name":"MUSICAL ACOUSTICS","terms":["Spring"],"prereqs":[],"subject":"PHYS","credits":4}
,{"_id": "PHYS 237","subid":[],"name":"QUANTUM MECHANICS OF PHYSICAL SYSTEMS","terms":["Spring"],"prereqs":["SPAN 122","SPAN 142","SPAN 123","SPAN 143","SPAN 165","SPAN 174","SPAN 164"],"subject":"PHYS","credits":4}
,{"_id": "PHYS 245W","subid":["CHEM 244W","CHEM 444","PHYS 445"],"name":"ADVANCED NUCLEAR SCIENCE EDUCATION LAB","terms":["Spring"],"prereqs":["SPAN 123","SPAN 143"],"subject":"PHYS","credits":4}
,{"_id": "PHYS 246","subid":[],"name":"QUANTUM THEORY","terms":["Spring"],"prereqs":["SPAN 281"],"subject":"PHYS","credits":4}
,{"_id": "PHYS 256","subid":[],"name":"COMPUTATIONAL PHYSICS","terms":["Spring"],"prereqs":["SPAN 141","SPAN 143","SPAN 121","SPAN 123"],"subject":"PHYS","credits":4}
,{"_id": "PHYS 265","subid":[],"name":"INTRODUCTION TO QUANTUM COMPUTING AND QUANTUM INFORMATION","terms":["Spring"],"prereqs":["MTH 161","MTH 165","MTH 171","MTH 174"],"subject":"PHYS","credits":4}
,{"_id": "PHYS 371","subid":["OPT 254"],"name":"NANOMETROLOGY LABORATORY","terms":["Spring"],"prereqs":[],"subject":"PHYS","credits":4}
,{"_id": "PHYS 403","subid":[],"name":"MODERN STATISTICS &AMP; EXPLORATION","terms":["Spring"],"prereqs":[],"subject":"PHYS","credits":4}
,{"_id": "PHYS 408","subid":[],"name":"QUANTUM MECHANICS II","terms":["Spring"],"prereqs":[],"subject":"PHYS","credits":4}
,{"_id": "PHYS 435","subid":["ME 465","MSC 465","OPT 465","TEO 465"],"name":"PRINCIPLES OF LASERS","terms":["Spring"],"prereqs":[],"subject":"PHYS","credits":4}
,{"_id": "PHYS 455","subid":["ME 435","TME 435"],"name":"PLASMA PHYSICS II","terms":["Spring"],"prereqs":[],"subject":"PHYS","credits":4}
,{"_id": "PHYS 532","subid":["OPT 552"],"name":"QUANTUM OPTICS OF THE ELECTROMAGNETIC FIELD","terms":["Spring"],"prereqs":["PHYS 531"],"subject":"PHYS","credits":4}
,{"_id": "PHYS 552","subid":["ME 532"],"name":"MAGNETOHYDRODYNAMICS","terms":["Spring"],"prereqs":[],"subject":"PHYS","credits":4}
,{"_id": "PHYS 553","subid":["ME 535"],"name":"LASER PLASMA INTERACTIONS","terms":["Spring"],"prereqs":[],"subject":"PHYS","credits":4}
,{"_id": "PHYS 591","subid":[],"name":"PHD READINGS: MECHANICS &AMP; CHAOTIC DYNAMICS","terms":["Spring"],"prereqs":[],"subject":"PHYS","credits":5}
,{"_id": "PHYS 595A","subid":[],"name":"PHD RESEARCH IN ABSENTIA","terms":["Spring"],"prereqs":[],"subject":"PHYS","credits":12}
,{"_id": "PHYS 595B","subid":[],"name":"RESEARCH IN ABSENTIA ABROAD","terms":["Spring"],"prereqs":[],"subject":"PHYS","credits":12}
,{"_id": "PHYS 997A","subid":[],"name":"DOCT DISSERTATN IN ABSENTIA","terms":["Spring"],"prereqs":[],"subject":"PHYS","credits":0}
,{"_id": "PHYS 999A","subid":[],"name":"DOCT DISSERTATN IN ABSENTIA","terms":["Spring"],"prereqs":[],"subject":"PHYS","credits":0}
,{"_id": "PHYS 999B","subid":[],"name":"PHD IN-ABSENTIA ABROAD","terms":["Spring"],"prereqs":[],"subject":"PHYS","credits":0}









,{"_id": "POLS 101","subid":[],"name":"ELEMENTARY POLISH I","terms":["Fall"],"prereqs":[],"subject":"POLS","credits":4}
,{"_id": "POLS 151","subid":[],"name":"INTERMEDIATE POLISH","terms":["Fall"],"prereqs":[],"subject":"POLS","credits":4}
,{"_id": "POLS 157","subid":[],"name":"POLISH IN POLAND","terms":["Summer"],"prereqs":[],"subject":"POLS","credits":3}
,{"_id": "POLS 102","subid":[],"name":"ELEMENTARY POLISH II","terms":["Spring"],"prereqs":[],"subject":"POLS","credits":4}
,{"_id": "POLS 201","subid":[],"name":"POLISH REVIEW","terms":["Spring"],"prereqs":[],"subject":"POLS","credits":4}
,{"_id": "POLS 391","subid":[],"name":"INDEPENDENT STUDY","terms":["Spring"],"prereqs":[],"subject":"POLS","credits":4}
,{"_id": "PORT 101","subid":[],"name":"ELEMENTARY PORTUGUESE","terms":["Fall"],"prereqs":[],"subject":"PORT","credits":4}
,{"_id": "PORT 151","subid":[],"name":"INTERMEDIATE PORTUGUESE I","terms":["Fall"],"prereqs":["PORT 151","PORT 102"],"subject":"PORT","credits":4}
,{"_id": "PORT 102","subid":[],"name":"ELEMENTARY PORTUGUESE II","terms":["Spring"],"prereqs":[],"subject":"PORT","credits":4}
,{"_id": "PORT 152","subid":[],"name":"INTERMEDIATE PORTUGUESE II","terms":["Spring"],"prereqs":[],"subject":"PORT","credits":4}
,{"_id": "PREC 001","subid":[],"name":"DREAMING NEW REALITIES: INTERACTIVE STORYTELLING WITH EXTENDED REALITY (XR) (FULL RATE COMMUTER)","terms":["Summer"],"prereqs":[],"subject":"PREC","credits":0}
,{"_id": "PREC 002","subid":[],"name":"WHAT'S UP DOC? EXPLORING THE PRE-MED EXPERIENCE","terms":["Summer","Summer","Summer","Summer","Summer","Summer","Summer","Summer","Summer","Summer","Summer","Summer","Summer","Summer","Summer","Summer"],"prereqs":[],"subject":"PREC","credits":0}
,{"_id": "PREC 003","subid":[],"name":"MINI MEDICAL SCHOOL","terms":["Summer"],"prereqs":[],"subject":"PREC","credits":0}
,{"_id": "PREC 004","subid":[],"name":"EXPLORATIONS IN PATHOLOGY","terms":["Summer"],"prereqs":[],"subject":"PREC","credits":0}
,{"_id": "PREC 005","subid":[],"name":"BUSINESS BOOTCAMP: INNOVATION MANAGEMENT","terms":["Summer"],"prereqs":[],"subject":"PREC","credits":0}
,{"_id": "PREC 006","subid":[],"name":"EXPLORATIONS IN ENGINEERING","terms":["Summer"],"prereqs":[],"subject":"PREC","credits":0}
,{"_id": "PREC 007","subid":[],"name":"INTRODUCTION IN ENGINEERING","terms":["Summer"],"prereqs":[],"subject":"PREC","credits":0}
,{"_id": "PREC 008","subid":[],"name":"QUEER NY: EXPLORING THE HISTORY OF THE LGBTQ+ COMMUNITY IN NEW YORK STATE","terms":["Summer"],"prereqs":[],"subject":"PREC","credits":0}
,{"_id": "PREC 009","subid":[],"name":"ETHICS IN THE MODERN WORLD","terms":["Summer"],"prereqs":[],"subject":"PREC","credits":0}
,{"_id": "PREC 010","subid":[],"name":"INTRODUCTION TO VISUAL AND MEDIA STUDIES","terms":["Summer"],"prereqs":[],"subject":"PREC","credits":0}
,{"_id": "PREC 011","subid":[],"name":"�DARK PLACES�: AN INTRODUCTION TO THE HAUNTED HOUSE FILM","terms":["Summer"],"prereqs":[],"subject":"PREC","credits":0}
,{"_id": "PREC 012","subid":[],"name":"BIOMEDICAL TECHNOLOGY-ENGINEER, DOCTOR, OR BOTH?","terms":["Summer","Summer","Summer","Summer","Summer","Summer","Summer","Summer","Summer","Summer","Summer","Summer","Summer","Summer","Summer","Summer"],"prereqs":[],"subject":"PREC","credits":0}
,{"_id": "PREC 013","subid":[],"name":"CAREERS IN NURSING","terms":["Summer"],"prereqs":[],"subject":"PREC","credits":0}
,{"_id": "PREC 014","subid":[],"name":"MYSTERIES OF THE BRAIN AND HUMAN BEHAVIOR: PSYCHOLOGY'S UNDERSTANDING OF DEVIANCE","terms":["Summer"],"prereqs":[],"subject":"PREC","credits":0}
,{"_id": "PREC 015","subid":[],"name":"ETHICAL DILEMMAS IN HEALTHCARE","terms":["Summer"],"prereqs":[],"subject":"PREC","credits":0}
,{"_id": "PREC 016","subid":[],"name":"THE BASICS OF INVESTMENTS AND CAREERS IN FINANCE","terms":["Summer"],"prereqs":[],"subject":"PREC","credits":0}
,{"_id": "PREC 017","subid":[],"name":"TOPICS IN BUSINESS","terms":["Summer"],"prereqs":[],"subject":"PREC","credits":0}
,{"_id": "PREC 019","subid":[],"name":"HARD KNOCK LIFE: ORPHANS IN THE NINETEENTH-CENTURY UNITED STATES","terms":["Summer"],"prereqs":[],"subject":"PREC","credits":0}
,{"_id": "PREC 020","subid":[],"name":"CAREERS IN ORAL HEALTH","terms":["Summer"],"prereqs":[],"subject":"PREC","credits":0}
,{"_id": "PREC 021","subid":[],"name":"LANGUAGE AND ADVERTISING","terms":["Summer"],"prereqs":[],"subject":"PREC","credits":0}
,{"_id": "PREC 022","subid":[],"name":"GEMSGETMATH@UR","terms":["Summer"],"prereqs":[],"subject":"PREC","credits":0}
,{"_id": "PSCI 101","subid":["INTR 101"],"name":"INTRO TO COMPARATIVE POLITICS","terms":["Fall"],"prereqs":[],"subject":"PSCI","credits":4}
,{"_id": "PSCI 104","subid":[],"name":"INTRO TO POLITICAL PHILOSOPHY","terms":["Fall"],"prereqs":[],"subject":"PSCI","credits":4}
,{"_id": "PSCI 106","subid":["INTR 106"],"name":"INTRO/INTERNATIONAL RELATNS","terms":["Fall","Spring"],"prereqs":[],"subject":"PSCI","credits":4}
,{"_id": "PSCI 107","subid":[],"name":"INTRO TO POSITIVE POLITICAL THEORY","terms":["Fall"],"prereqs":[],"subject":"PSCI","credits":4}
,{"_id": "PSCI 116","subid":["PHLT 116"],"name":"INTRODUCTION TO THE U.S. HEALTH SYSTEM","terms":["Fall"],"prereqs":[],"subject":"PSCI","credits":4}
,{"_id": "PSCI 121","subid":[],"name":"DEMOCRACY IN AMERICA","terms":["Fall","Spring"],"prereqs":[],"subject":"PSCI","credits":4}
,{"_id": "PSCI 200","subid":[],"name":"DATA ANALYSIS I","terms":["Fall","Spring"],"prereqs":[],"subject":"PSCI","credits":4}
,{"_id": "PSCI 202W","subid":[],"name":"ARGUMENT IN POLITICAL SCIENCE","terms":["Fall"],"prereqs":[],"subject":"PSCI","credits":4}
,{"_id": "PSCI 209","subid":["PSCI 209W"],"name":"THE POLITICS OF PUNISHMENT","terms":["Fall"],"prereqs":[],"subject":"PSCI","credits":4}
,{"_id": "PSCI 210","subid":["PSCI 210W"],"name":"PANDEMIC POLITICS","terms":["Fall"],"prereqs":[],"subject":"PSCI","credits":4}
,{"_id": "PSCI 213","subid":["AAAS 296"],"name":"BLACK POLITICS","terms":["Fall"],"prereqs":[],"subject":"PSCI","credits":4}
,{"_id": "PSCI 235","subid":["PSCI 235W"],"name":"THE POLITICAL ECONOMY OF U.S. FOOD POLICY","terms":["Fall"],"prereqs":[],"subject":"PSCI","credits":4}
,{"_id": "PSCI 243","subid":["PSCI 243W"],"name":"ENVIRONMENTAL POLITICS","terms":["Fall"],"prereqs":[],"subject":"PSCI","credits":4}
,{"_id": "PSCI 248","subid":["PSCI 248W"],"name":"DISCRIMINATION","terms":["Fall"],"prereqs":[],"subject":"PSCI","credits":4}
,{"_id": "PSCI 264","subid":["INTR 264","INTR 264W","PSCI 264W"],"name":"COMPARATIVE POLITICAL INSTITUTIONS","terms":["Fall"],"prereqs":[],"subject":"PSCI","credits":4}
,{"_id": "PSCI 265","subid":["INTR 265"],"name":"CIVIL WAR AND THE INTERNATIONAL SYSTEM","terms":["Fall"],"prereqs":[],"subject":"PSCI","credits":4}
,{"_id": "PSCI 288","subid":["ECON 288","ECON 288W"],"name":"GAME THEORY","terms":["Fall","Spring"],"prereqs":[],"subject":"PSCI","credits":4}
,{"_id": "PSCI 299","subid":["INTR 299","WRTG 276"],"name":"COMMUNICATING YOUR PROFESSIONAL IDENTITY - LAW, POLICY, AND SOCIAL GOOD","terms":["Fall"],"prereqs":[],"subject":"PSCI","credits":2}
,{"_id": "PSCI 389W","subid":["INTR 389W"],"name":"SENIOR HONORS SEM","terms":["Fall"],"prereqs":[],"subject":"PSCI","credits":4}
,{"_id": "PSCI 390","subid":[],"name":"SUPERVISED TEACHING: PSCI 202","terms":["Fall"],"prereqs":[],"subject":"PSCI","credits":4}
,{"_id": "PSCI 394","subid":[],"name":"INTERNSHIP","terms":["Fall","Spring"],"prereqs":[],"subject":"PSCI","credits":4}
,{"_id": "PSCI 394A","subid":[],"name":"EUROPEAN POLITICAL INTERNSHIP","terms":["Fall"],"prereqs":[],"subject":"PSCI","credits":8}
,{"_id": "PSCI 394B","subid":[],"name":"EUROPEAN POLITICAL INTERNSHIP-BELGIUM","terms":["Fall","Spring"],"prereqs":[],"subject":"PSCI","credits":8}
,{"_id": "PSCI 394C","subid":[],"name":"WASHINGTON SEMESTER INTERNSHIP","terms":["Fall","Spring"],"prereqs":[],"subject":"PSCI","credits":12}
,{"_id": "PSCI 394F","subid":["PHLT 394F"],"name":"HEALTH POLICY INTERNSHIP","terms":["Fall","Spring"],"prereqs":[],"subject":"PSCI","credits":4}
,{"_id": "PSCI 394W","subid":[],"name":"INTERNSHIP","terms":["Fall"],"prereqs":[],"subject":"PSCI","credits":4}
,{"_id": "PSCI 399","subid":[],"name":"WASHINGTON SEMESTER","terms":["Fall","Spring"],"prereqs":[],"subject":"PSCI","credits":4}
,{"_id": "PSCI 401","subid":[],"name":"MATH FUNDAMENTALS FOR POLITICAL SCIENCE","terms":["Fall"],"prereqs":[],"subject":"PSCI","credits":2}
,{"_id": "PSCI 404","subid":[],"name":"PROBABILITY &AMP; INFERENCE","terms":["Fall"],"prereqs":["PSC 405","PSC 505","PSC 506"],"subject":"PSCI","credits":4}
,{"_id": "PSCI 407","subid":[],"name":"MATHEMATICAL MODELING","terms":["Fall"],"prereqs":["PSC 407","PSC 408"],"subject":"PSCI","credits":4}
,{"_id": "PSCI 505","subid":[],"name":"LIKELIHOOD + TOPICS","terms":["Fall"],"prereqs":[],"subject":"PSCI","credits":4}
,{"_id": "PSCI 541","subid":[],"name":"U.S. POLITICAL BEHAVIOR","terms":["Fall"],"prereqs":[],"subject":"PSCI","credits":4}
,{"_id": "PSCI 551","subid":[],"name":"STATE BUILDING AND CONFLICT","terms":["Fall"],"prereqs":[],"subject":"PSCI","credits":4}
,{"_id": "PSCI 566","subid":[],"name":"IR FIELD SEMINAR I","terms":["Fall"],"prereqs":[],"subject":"PSCI","credits":4}
,{"_id": "PSCI 576","subid":[],"name":"GRADUATE RESEARCH SEMINAR","terms":["Fall"],"prereqs":[],"subject":"PSCI","credits":0}
,{"_id": "PSCI 584","subid":[],"name":"GAME THEORY","terms":["Fall"],"prereqs":["PSC 407","PSC 408"],"subject":"PSCI","credits":4}
,{"_id": "PSCI 587","subid":[],"name":"STRUCTURAL MODELING AND ESTIMATION","terms":["Fall"],"prereqs":[],"subject":"PSCI","credits":4}
,{"_id": "PSCI 595","subid":[],"name":"PHD RESEARCH IN POL SCI","terms":["Fall","Spring"],"prereqs":[],"subject":"PSCI","credits":18}
,{"_id": "PSCI 895","subid":[],"name":"CONT OF MASTER'S ENROLLMENT","terms":["Fall","Spring"],"prereqs":[],"subject":"PSCI","credits":0}
,{"_id": "PSCI 899","subid":[],"name":"MASTER'S DISSERTATION","terms":["Fall","Spring"],"prereqs":[],"subject":"PSCI","credits":0}
,{"_id": "PSCI 995","subid":[],"name":"CONT OF DOCTORAL ENROLLMENT","terms":["Fall","Spring"],"prereqs":[],"subject":"PSCI","credits":0}
,{"_id": "PSCI 997","subid":[],"name":"DOCTORAL DISSERTATION","terms":["Fall","Summer","Spring"],"prereqs":[],"subject":"PSCI","credits":0}
,{"_id": "PSCI 999","subid":[],"name":"DOCTORAL DISSERTATION","terms":["Fall","Spring"],"prereqs":[],"subject":"PSCI","credits":0}
,{"_id": "PSCI 594","subid":[],"name":"RESEARCH INTERNSHIP","terms":["Summer","Spring"],"prereqs":[],"subject":"PSCI","credits":1}
,{"_id": "PSCI 105","subid":[],"name":"INTRO TO U.S. POLITICS","terms":["Spring"],"prereqs":[],"subject":"PSCI","credits":4}
,{"_id": "PSCI 205","subid":[],"name":"DATA ANALYSIS II","terms":["Spring"],"prereqs":["PSCI 200","ECON 230","STAT 212","STAT 213","STAT 214"],"subject":"PSCI","credits":4}
,{"_id": "PSCI 214","subid":["AAAS 212"],"name":"RACE AND THE LAW","terms":["Spring"],"prereqs":[],"subject":"PSCI","credits":4}
,{"_id": "PSCI 216","subid":["PHLT 238"],"name":"ENVIRONMENTAL HEALTH AND JUSTICE IN THE ROCHESTER COMMUNITY","terms":["Spring"],"prereqs":[],"subject":"PSCI","credits":4}
,{"_id": "PSCI 217","subid":[],"name":"PUBLIC POLICY AND BLACK COMMUNITIES:  EDUCATION, POVERTY, AFFIRMATIVE ACTION, AND CRIME","terms":["Spring"],"prereqs":[],"subject":"PSCI","credits":4}
,{"_id": "PSCI 224","subid":["AAAS 183","HIST 112","RELC 183"],"name":"INCARCERATION NATION","terms":["Spring"],"prereqs":[],"subject":"PSCI","credits":4}
,{"_id": "PSCI 225","subid":["AAAS 200","ANTH 233","GSWS 233","RELC 230"],"name":"CULTURAL POLITICS OF PRISON TOWNS","terms":["Spring"],"prereqs":[],"subject":"PSCI","credits":4}
,{"_id": "PSCI 226W","subid":[],"name":"ACT LOCALLY?:  LOCAL GOVERNMENT AND PUBLIC POLICY IN THE U.S.","terms":["Spring"],"prereqs":[],"subject":"PSCI","credits":4}
,{"_id": "PSCI 230","subid":["PHLT 230"],"name":"PUBLIC HEALTH LAW &AMP; POLICY","terms":["Spring"],"prereqs":[],"subject":"PSCI","credits":4}
,{"_id": "PSCI 231W","subid":["PHLT 234W"],"name":"MATERNAL CHILD HEALTH POLICY","terms":["Spring"],"prereqs":[],"subject":"PSCI","credits":4}
,{"_id": "PSCI 240","subid":[],"name":"CRIMINAL PROCEDURE &AMP; CONSTITUTIONAL PRINCIPLES","terms":["Spring"],"prereqs":[],"subject":"PSCI","credits":4}
,{"_id": "PSCI 244K","subid":[],"name":"POLITICS &AMP; MARKETS:  INNOVATION AND THE GLOBAL BUSINESS ENVIRONMENT","terms":["Spring"],"prereqs":[],"subject":"PSCI","credits":4}
,{"_id": "PSCI 253","subid":["INTR 253","INTR 253W","PSCI 253W"],"name":"COMPARATIVE POLITICAL PARTIES","terms":["Spring"],"prereqs":[],"subject":"PSCI","credits":4}
,{"_id": "PSCI 254","subid":["INTR 254","INTR 254W","PSCI 254W"],"name":"FASCISM:  POLITICS, HISTORY, AND CULTURE","terms":["Spring"],"prereqs":[],"subject":"PSCI","credits":4}
,{"_id": "PSCI 260","subid":["INTR 260","INTR 260W","PSCI 260W"],"name":"DEMOCRATIC EROSION","terms":["Spring"],"prereqs":[],"subject":"PSCI","credits":4}
,{"_id": "PSCI 268","subid":["INTR 268","INTR 268W","PSCI 268W"],"name":"INTERNATIONAL ORGANIZATION","terms":["Spring"],"prereqs":[],"subject":"PSCI","credits":4}
,{"_id": "PSCI 282W","subid":["PSCI 282","PSCI 482"],"name":"MAKING PUBLIC POLICY","terms":["Spring"],"prereqs":[],"subject":"PSCI","credits":4}
,{"_id": "PSCI 316W","subid":["HIST 374W","HIST 474","PHLT 374"],"name":"PANDEMICS, POLITICS AND POLICIES IN THE US, 1918-2020","terms":["Spring"],"prereqs":[],"subject":"PSCI","credits":4}
,{"_id": "PSCI 356","subid":["PSCI 556"],"name":"POLITICAL INSTITUTIONS &AMP; BEHAVIOR","terms":["Spring"],"prereqs":[],"subject":"PSCI","credits":4}
,{"_id": "PSCI 373","subid":["INTR 373","INTR 373W","PSCI 373W","PSCI 573"],"name":"TERRITORY AND GROUP CONFLICT","terms":["Spring"],"prereqs":[],"subject":"PSCI","credits":4}
,{"_id": "PSCI 393W","subid":["INTR 393W"],"name":"SENIOR HONORS PROJECT","terms":["Spring"],"prereqs":[],"subject":"PSCI","credits":4}
,{"_id": "PSCI 405","subid":[],"name":"CAUSAL INFERENCE","terms":["Spring"],"prereqs":[],"subject":"PSCI","credits":4}
,{"_id": "PSCI 408","subid":[],"name":"POSTIVE POLITICAL THEORY II","terms":["Spring"],"prereqs":[],"subject":"PSCI","credits":4}
,{"_id": "PSCI 491","subid":[],"name":"MASTER'S READINGS IN POL SCI","terms":["Spring"],"prereqs":[],"subject":"PSCI","credits":5}
,{"_id": "PSCI 493","subid":[],"name":"MASTER'S ESSAY","terms":["Spring"],"prereqs":[],"subject":"PSCI","credits":18}
,{"_id": "PSCI 496","subid":["AAAS 282","PSCI 296"],"name":"FREEDOM AND DOMINATION IN BLACK POLITICS","terms":["Spring"],"prereqs":[],"subject":"PSCI","credits":4}
,{"_id": "PSCI 507","subid":[],"name":"EXPERIMENTS IN PS RESEARCH","terms":["Spring"],"prereqs":[],"subject":"PSCI","credits":4}
,{"_id": "PSCI 540","subid":[],"name":"AMERICAN POLITICAL INSTITUTIONS","terms":["Spring"],"prereqs":[],"subject":"PSCI","credits":4}
,{"_id": "PSCI 559","subid":[],"name":"HISTORICAL POLITICAL ECONOMY","terms":["Spring"],"prereqs":[],"subject":"PSCI","credits":4}
,{"_id": "PSCI 586","subid":[],"name":"VOTING AND ELECTIONS","terms":["Spring"],"prereqs":[],"subject":"PSCI","credits":4}
,{"_id": "PSCI 589","subid":[],"name":"SOCIAL CHOICE, BARGAINING, AND ELECTIONS","terms":["Spring"],"prereqs":[],"subject":"PSCI","credits":4}
,{"_id": "PSCI 591","subid":[],"name":"PHD READINGS IN AMERICAN POLITICAL DEVELOPMENT","terms":["Spring"],"prereqs":[],"subject":"PSCI","credits":5}
,{"_id": "PSCI 595A","subid":[],"name":"PHD RESEARCH IN ABSENTIA","terms":["Spring"],"prereqs":[],"subject":"PSCI","credits":15}
,{"_id": "PSCI 997A","subid":[],"name":"DOCTORAL DISSERTATION IN ABSENTIA","terms":["Spring"],"prereqs":[],"subject":"PSCI","credits":0}
,{"_id": "PSCI 999A","subid":[],"name":"DOCTORAL DISSERTATION IN ABSENTIA","terms":["Spring"],"prereqs":[],"subject":"PSCI","credits":0}
,{"_id": "PSCI 999B","subid":[],"name":"PHD IN-ABSENTIA ABROAD","terms":["Spring"],"prereqs":[],"subject":"PSCI","credits":0}
,{"_id": "PSYC 101","subid":[],"name":"INTRO TO PSYCHOLOGY","terms":["Fall","Summer","Spring"],"prereqs":[],"subject":"PSYC","credits":4}
,{"_id": "PSYC 110","subid":["BCSC 110","CVSC 110"],"name":"NEURAL FOUNDATIONS OF BEHAVIOR","terms":["Fall","Summer","Spring"],"prereqs":[],"subject":"PSYC","credits":4}
,{"_id": "PSYC 111","subid":["BCSC 111"],"name":"FOUNDATIONS OF COGNITIVE SCIENCE","terms":["Fall","Summer","Spring"],"prereqs":[],"subject":"PSYC","credits":4}
,{"_id": "PSYC 151","subid":["BCSC 151","CVSC 151"],"name":"PERCEPTION &AMP; ACTION","terms":["Fall"],"prereqs":["BCSC 110","BCSC 111"],"subject":"PSYC","credits":4}
,{"_id": "PSYC 152","subid":["ASLA 260","BCSC 152","LING 217"],"name":"LANGUAGE &AMP; PSYCHOLINGUISTICS","terms":["Fall"],"prereqs":["BCSC 110","BCSC 111"],"subject":"PSYC","credits":4}
,{"_id": "PSYC 170","subid":["BCSC 170"],"name":"CHILD DEVELOPMENT","terms":["Fall"],"prereqs":[],"subject":"PSYC","credits":4}
,{"_id": "PSYC 181","subid":[],"name":"THY OF PERSONALITY &AMP; PSYCHOTHERAPY","terms":["Fall","Summer"],"prereqs":[],"subject":"PSYC","credits":4}
,{"_id": "PSYC 181W","subid":[],"name":"THY OF PERSONALITY&AMP;PSYCHOTHE","terms":["Fall"],"prereqs":[],"subject":"PSYC","credits":0}
,{"_id": "PSYC 183","subid":["BCSC 183"],"name":"ANIMAL MINDS","terms":["Fall"],"prereqs":[],"subject":"PSYC","credits":4}
,{"_id": "PSYC 205","subid":["BCSC 205"],"name":"LAB IN DEVELOPMENT &AMP; LEARNING","terms":["Fall"],"prereqs":["STAT 212","BCSC 172","BCSC 151","BCSC 152","BCSC 153"],"subject":"PSYC","credits":4}
,{"_id": "PSYC 219","subid":[],"name":"RESEARCH METHODS IN PSYCHOLOGY","terms":["Fall","Spring"],"prereqs":["PSYC 101","STAT 211","STAT 212"],"subject":"PSYC","credits":4}
,{"_id": "PSYC 219W","subid":[],"name":"RESEARCH METHODS OF PSYCHOLOGY","terms":["Fall","Spring"],"prereqs":[],"subject":"PSYC","credits":0}
,{"_id": "PSYC 259","subid":["ASLA 208","BCSC 259","LING 208"],"name":"LANGUAGE DEVELOPMENT","terms":["Fall"],"prereqs":["BCSC 152","LING 110"],"subject":"PSYC","credits":4}
,{"_id": "PSYC 263","subid":[],"name":"RELATIONSHIPS PROCESS&AMP;EMOTN","terms":["Fall"],"prereqs":[],"subject":"PSYC","credits":4}
,{"_id": "PSYC 267","subid":["GSWS 266"],"name":"PSYCHOLOGY OF GENDER","terms":["Fall"],"prereqs":["PSYC 101"],"subject":"PSYC","credits":4}
,{"_id": "PSYC 267W","subid":[],"name":"PSYCHOLOGY OF GENDER","terms":["Fall"],"prereqs":[],"subject":"PSYC","credits":0}
,{"_id": "PSYC 274W","subid":["WRTG 274"],"name":"COMMUNICATING YOUR PROFESSIONAL IDENTITY - PSYCHOLOGY","terms":["Fall","Spring"],"prereqs":[],"subject":"PSYC","credits":2}
,{"_id": "PSYC 280","subid":[],"name":"CLINICAL PSYCHOLOGY","terms":["Fall"],"prereqs":[],"subject":"PSYC","credits":4}
,{"_id": "PSYC 280W","subid":[],"name":"CLINICAL PSYCHOLOGY","terms":["Fall"],"prereqs":[],"subject":"PSYC","credits":0}
,{"_id": "PSYC 289","subid":[],"name":"DEVLP CHILD PSYCHOPATHOLOGY","terms":["Fall"],"prereqs":[],"subject":"PSYC","credits":4}
,{"_id": "PSYC 289W","subid":[],"name":"DEVLP CHILD PSYCHOPATHOLOGY","terms":["Fall"],"prereqs":[],"subject":"PSYC","credits":0}
,{"_id": "PSYC 301W","subid":[],"name":"TEACHING PSYCHOLOGY","terms":["Fall"],"prereqs":[],"subject":"PSYC","credits":6}
,{"_id": "PSYC 302","subid":[],"name":"TEACHING PSY OF PERSONALITY","terms":["Fall"],"prereqs":[],"subject":"PSYC","credits":6}
,{"_id": "PSYC 351","subid":[],"name":"RESEARCH IN DEVELOPMENTAL NEUROPSYCHOLOGY","terms":["Fall","Spring"],"prereqs":[],"subject":"PSYC","credits":4}
,{"_id": "PSYC 372","subid":[],"name":"SOCIAL STRESS RESEARCH","terms":["Fall","Spring"],"prereqs":[],"subject":"PSYC","credits":2}
,{"_id": "PSYC 373","subid":[],"name":"EXPLORING RESEARCH IN SOCIAL PSYCHOLOGY I","terms":["Fall"],"prereqs":[],"subject":"PSYC","credits":4}
,{"_id": "PSYC 375","subid":[],"name":"GUIDED RESEARCH IN DEVELOPMENTAL PSYCHOPATHOLOGY I","terms":["Fall"],"prereqs":[],"subject":"PSYC","credits":4}
,{"_id": "PSYC 383","subid":["PSYC 583"],"name":"MORAL DEVELOPMENT","terms":["Fall"],"prereqs":[],"subject":"PSYC","credits":4}
,{"_id": "PSYC 383W","subid":[],"name":"MORAL DEVELOPMENT","terms":["Fall"],"prereqs":[],"subject":"PSYC","credits":0}
,{"_id": "PSYC 386V","subid":[],"name":"FULL TIME VISITING STUDENT","terms":["Fall"],"prereqs":[],"subject":"PSYC","credits":0}
,{"_id": "PSYC 389","subid":[],"name":"HONORS RESEARCH","terms":["Fall"],"prereqs":[],"subject":"PSYC","credits":4}
,{"_id": "PSYC 390","subid":[],"name":"SUPERVISED TEACHING","terms":["Fall"],"prereqs":[],"subject":"PSYC","credits":4}
,{"_id": "PSYC 390W","subid":[],"name":"SUPERVISED TEACHING - PSYC 101: INTRODUCTION TO PSYCHOLOGY","terms":["Fall"],"prereqs":[],"subject":"PSYC","credits":4}
,{"_id": "PSYC 394","subid":[],"name":"INTERNSHIP","terms":["Fall"],"prereqs":[],"subject":"PSYC","credits":4}
,{"_id": "PSYC 504","subid":[],"name":"DATA ANALYSIS I","terms":["Fall"],"prereqs":[],"subject":"PSYC","credits":3}
,{"_id": "PSYC 515","subid":[],"name":"HIERARCHICAL LINEAR MODELING","terms":["Fall"],"prereqs":[],"subject":"PSYC","credits":3}
,{"_id": "PSYC 551","subid":[],"name":"SOCIAL COGNITION","terms":["Fall"],"prereqs":[],"subject":"PSYC","credits":3}
,{"_id": "PSYC 570","subid":[],"name":"CLINICAL ASSESSMENT I","terms":["Fall"],"prereqs":[],"subject":"PSYC","credits":3}
,{"_id": "PSYC 572","subid":[],"name":"INTRO TO CLINICAL RESEARCH METHODS","terms":["Fall"],"prereqs":[],"subject":"PSYC","credits":3}
,{"_id": "PSYC 575","subid":[],"name":"PSYCHOPATHOLOGY I","terms":["Fall"],"prereqs":[],"subject":"PSYC","credits":3}
,{"_id": "PSYC 584","subid":[],"name":"PSYCHOTHERAPY PRACTICUM I","terms":["Fall"],"prereqs":[],"subject":"PSYC","credits":3}
,{"_id": "PSYC 595","subid":[],"name":"PHD RESEARCH","terms":["Fall","Spring"],"prereqs":[],"subject":"PSYC","credits":12}
,{"_id": "PSYC 991","subid":[],"name":"CLINICAL INTERNSHIP","terms":["Fall","Spring"],"prereqs":[],"subject":"PSYC","credits":0}
,{"_id": "PSYC 995","subid":[],"name":"CONT OF DOCTORAL ENROLLMENT","terms":["Fall"],"prereqs":[],"subject":"PSYC","credits":0}
,{"_id": "PSYC 997","subid":[],"name":"DOCTORAL DISSERTATION","terms":["Fall","Summer","Spring"],"prereqs":[],"subject":"PSYC","credits":0}
,{"_id": "PSYC 999","subid":[],"name":"DOCTORAL DISSERTATION","terms":["Fall","Spring"],"prereqs":[],"subject":"PSYC","credits":0}
,{"_id": "PSYC 171","subid":[],"name":"SOCIAL &AMP; EMOTIONAL DEVELOPMENT","terms":["Summer"],"prereqs":[],"subject":"PSYC","credits":4}
,{"_id": "PSYC 171W","subid":[],"name":"SOCIAL &AMP; EMOTIONAL DEVELOPMENT","terms":["Summer"],"prereqs":[],"subject":"PSYC","credits":0}
,{"_id": "PSYC 172","subid":["BCSC 172"],"name":"DEVELOPMENT OF MIND &AMP; BRAIN","terms":["Summer","Spring"],"prereqs":[],"subject":"PSYC","credits":4}
,{"_id": "PSYC 277","subid":[],"name":"CULTURAL BASES OF HUMAN DEVELOPMENT","terms":["Summer"],"prereqs":[],"subject":"PSYC","credits":4}
,{"_id": "PSYC 278","subid":[],"name":"ADOLESCENT DEVELOPMENT","terms":["Summer","Spring"],"prereqs":[],"subject":"PSYC","credits":4}
,{"_id": "PSYC 278W","subid":[],"name":"ADOLESCENT DEVELOPMENT","terms":["Summer","Spring"],"prereqs":[],"subject":"PSYC","credits":0}
,{"_id": "PSYC 282","subid":[],"name":"PSYCHOPATHOLOGY","terms":["Summer","Spring"],"prereqs":[],"subject":"PSYC","credits":4}
,{"_id": "PSYC 282W","subid":[],"name":"PSYCHOPATHOLOGY","terms":["Summer","Spring"],"prereqs":[],"subject":"PSYC","credits":0}
,{"_id": "PSYC 594","subid":[],"name":"INTERNSHIP","terms":["Summer"],"prereqs":[],"subject":"PSYC","credits":1}
,{"_id": "PSYC 897","subid":[],"name":"MASTER'S DISSERTATION","terms":["Summer"],"prereqs":[],"subject":"PSYC","credits":0}
,{"_id": "PSYC 986V","subid":[],"name":"FULL TIME VISITING STUDENT","terms":["Summer","Spring"],"prereqs":[],"subject":"PSYC","credits":0}
,{"_id": "PSYC 153","subid":["BCSC 153"],"name":"COGNITION","terms":["Spring"],"prereqs":["SPAN 111","SPAN 110"],"subject":"PSYC","credits":4}
,{"_id": "PSYC 161","subid":[],"name":"SOCIAL PSYCHOLOGY &AMP; INDIVIDUAL DIFFERENCES","terms":["Spring"],"prereqs":[],"subject":"PSYC","credits":4}
,{"_id": "PSYC 161W","subid":[],"name":"SOCIAL PSYCHOLOGY &AMP; INDIVIDUAL DIFFERENCES","terms":["Spring"],"prereqs":[],"subject":"PSYC","credits":0}
,{"_id": "PSYC 208","subid":["BCSC 208","CVSC 208"],"name":"LAB IN PERCEPTION &AMP; COGNITION","terms":["Spring"],"prereqs":["STAT 212","BCSC 151","BCSC 153"],"subject":"PSYC","credits":4}
,{"_id": "PSYC 209","subid":["GSWS 209"],"name":"PSYCHOLOGY OF HUMAN SEXUALITY","terms":["Spring"],"prereqs":["PSYC 101"],"subject":"PSYC","credits":4}
,{"_id": "PSYC 209W","subid":[],"name":"PSYCHOLOGY OF HUMAN SEXUALITY","terms":["Spring"],"prereqs":[],"subject":"PSYC","credits":0}
,{"_id": "PSYC 210","subid":["BCSC 185"],"name":"SOCIAL COGNITION","terms":["Spring"],"prereqs":["PSYC 101"],"subject":"PSYC","credits":4}
,{"_id": "PSYC 210W","subid":[],"name":"SOCIAL COGNITION","terms":["Spring"],"prereqs":[],"subject":"PSYC","credits":0}
,{"_id": "PSYC 221","subid":["BCSC 221","BCSC 521"],"name":"AUDITORY PERCEPTION","terms":["Spring"],"prereqs":["BCSC 110","BCSC 111"],"subject":"PSYC","credits":4}
,{"_id": "PSYC 232","subid":[],"name":"PSYCHOLOGY OF CONSUMERISM","terms":["Spring"],"prereqs":[],"subject":"PSYC","credits":4}
,{"_id": "PSYC 232W","subid":[],"name":"PSYCHOLOGY OF CONSUMERISM","terms":["Spring"],"prereqs":[],"subject":"PSYC","credits":0}
,{"_id": "PSYC 246","subid":["BCSC 246","BCSC 546","NSCI 246"],"name":"BIOLOGY OF MENTAL DISORDERS","terms":["Spring"],"prereqs":["NSCI 201","BCSC 240"],"subject":"PSYC","credits":4}
,{"_id": "PSYC 248","subid":[],"name":"SOCIAL NEUROSCIENCE","terms":["Spring"],"prereqs":["PSYC 101","BCSC 110"],"subject":"PSYC","credits":4}
,{"_id": "PSYC 248W","subid":[],"name":"SOCIAL NEUROSCIENCE","terms":["Spring"],"prereqs":[],"subject":"PSYC","credits":0}
,{"_id": "PSYC 262","subid":[],"name":"AN APPROACH TO HUMAN MOTIVATION","terms":["Spring"],"prereqs":["PSYC 161","PSYC 181"],"subject":"PSYC","credits":4}
,{"_id": "PSYC 262W","subid":[],"name":"AN APPROACH TO HUMAN MOTIVATION","terms":["Spring"],"prereqs":[],"subject":"PSYC","credits":0}
,{"_id": "PSYC 264","subid":[],"name":"INDUSTRIAL &AMP; ORGANIZATIONAL PSYCHOLOGY","terms":["Spring"],"prereqs":[],"subject":"PSYC","credits":4}
,{"_id": "PSYC 264W","subid":[],"name":"INDUSTRIAL &AMP; ORGANIZATIONAL PSYCHOLOGY","terms":["Spring"],"prereqs":[],"subject":"PSYC","credits":0}
,{"_id": "PSYC 283","subid":[],"name":"BEHAVIORAL MEDICINE","terms":["Spring"],"prereqs":["PSYC 101"],"subject":"PSYC","credits":4}
,{"_id": "PSYC 283W","subid":[],"name":"BEHAVIORAL MEDICINE","terms":["Spring"],"prereqs":[],"subject":"PSYC","credits":0}
,{"_id": "PSYC 303","subid":[],"name":"TEACHING PSYCHOLOGY OF MOTIVATION","terms":["Spring"],"prereqs":[],"subject":"PSYC","credits":6}
,{"_id": "PSYC 321","subid":[],"name":"PSYCHOLOGY OF RELIGION","terms":["Spring"],"prereqs":[],"subject":"PSYC","credits":4}
,{"_id": "PSYC 340","subid":[],"name":"DEPRESSION AND ANXIETY SEMINAR","terms":["Spring"],"prereqs":["PSYC 101","PSYC 280","PSYC 282","PSYC 289"],"subject":"PSYC","credits":4}
,{"_id": "PSYC 376","subid":[],"name":"GUIDED RESEARCH IN DEVELOPMENTAL PSYCHOPATHOLOGY II","terms":["Spring"],"prereqs":[],"subject":"PSYC","credits":4}
,{"_id": "PSYC 376W","subid":[],"name":"GUIDED RESEARCH IN DEVELOPMENTAL PSYCHOPATHOLOGY II","terms":["Spring"],"prereqs":[],"subject":"PSYC","credits":0}
,{"_id": "PSYC 381","subid":[],"name":"SEMINAR IN NEURODEVELOPMENTAL DISABILITIES","terms":["Spring"],"prereqs":["PSYC 282","PSYC 289"],"subject":"PSYC","credits":4}
,{"_id": "PSYC 381W","subid":[],"name":"SEMINAR IN NEURODEVELOPMENTAL DISABILITIES","terms":["Spring"],"prereqs":[],"subject":"PSYC","credits":0}
,{"_id": "PSYC 393W","subid":[],"name":"HONORS RESEARCH","terms":["Spring"],"prereqs":[],"subject":"PSYC","credits":4}
,{"_id": "PSYC 513","subid":[],"name":"META-ANALYSIS","terms":["Spring"],"prereqs":[],"subject":"PSYC","credits":3}
,{"_id": "PSYC 517","subid":[],"name":"STRUCTURAL EQUATION MODELING II","terms":["Spring"],"prereqs":[],"subject":"PSYC","credits":3}
,{"_id": "PSYC 518","subid":[],"name":"STATISTICAL COMPUTING WITH R","terms":["Spring"],"prereqs":[],"subject":"PSYC","credits":3}
,{"_id": "PSYC 519","subid":[],"name":"DATA ANALYSIS II-GENERAL LINEAR APPROACHES","terms":["Spring"],"prereqs":[],"subject":"PSYC","credits":3}
,{"_id": "PSYC 555","subid":[],"name":"CLOSE RELATIONSHIPS","terms":["Spring"],"prereqs":[],"subject":"PSYC","credits":3}
,{"_id": "PSYC 562","subid":[],"name":"DEVELOPMENTAL RESEARCH METHODS","terms":["Spring"],"prereqs":[],"subject":"PSYC","credits":3}
,{"_id": "PSYC 566","subid":[],"name":"NEUROBIOLOGICAL FOUNDATIONS","terms":["Spring"],"prereqs":[],"subject":"PSYC","credits":3}
,{"_id": "PSYC 571","subid":[],"name":"CLINICAL ASSESSMENT II","terms":["Spring"],"prereqs":[],"subject":"PSYC","credits":3}
,{"_id": "PSYC 576","subid":[],"name":"PSYCHOPATHOLOGY II","terms":["Spring"],"prereqs":[],"subject":"PSYC","credits":3}
,{"_id": "PSYC 585","subid":[],"name":"PSYCHOTHERAPY PRACTICUM II","terms":["Spring"],"prereqs":[],"subject":"PSYC","credits":3}
,{"_id": "PSYC 586","subid":[],"name":"EVIDENCE-BASED CHILD PSYCHOTHERAPY","terms":["Spring"],"prereqs":[],"subject":"PSYC","credits":3}
,{"_id": "PSYC 591","subid":[],"name":"PHD READINGS","terms":["Spring"],"prereqs":[],"subject":"PSYC","credits":3}
,{"_id": "RELC 101","subid":["JWST 106"],"name":"INTRODUCTION TO THE HEBREW BIBLE","terms":["Fall"],"prereqs":[],"subject":"RELC","credits":4}
,{"_id": "RELC 105","subid":[],"name":"ASIAN SEARCH FOR SELF","terms":["Fall"],"prereqs":[],"subject":"RELC","credits":4}
,{"_id": "RELC 109","subid":["JWST 100"],"name":"INTRODUCTION TO JEWISH STUDIES","terms":["Fall"],"prereqs":[],"subject":"RELC","credits":4}
,{"_id": "RELC 132","subid":["AHST 212","CLTR 208A","HIST 146","JPNS 210"],"name":"VENGEANCE, LONGING, AND SALVATION: TOPICS IN �TRADITIONAL� JAPANESE CULTURE","terms":["Fall"],"prereqs":[],"subject":"RELC","credits":4}
,{"_id": "RELC 136","subid":["JWST 136"],"name":"ANGELS, SACRED LETTERS, AND HOLLYWOOD: INTRODUCTION TO JEWISH MYSTICISM","terms":["Fall"],"prereqs":[],"subject":"RELC","credits":4}
,{"_id": "RELC 140","subid":["CLST 140","ENGL 112"],"name":"CLASSICAL AND SCRIPTURAL BACKGROUNDS","terms":["Fall"],"prereqs":[],"subject":"RELC","credits":4}
,{"_id": "RELC 147","subid":["GSWS 161","JWST 161"],"name":"WOMEN IN JUDAISM: RITUAL, EXPERIENCE, AND LEADERSHIP","terms":["Fall"],"prereqs":[],"subject":"RELC","credits":4}
,{"_id": "RELC 149","subid":["ARBC 149"],"name":"THE MIDDLE EAST: REVOLUTION, WAR AND DISSENT","terms":["Fall"],"prereqs":[],"subject":"RELC","credits":4}
,{"_id": "RELC 159","subid":[],"name":"INTRODUCTION TO INTERRELIGIOUS STUDIES","terms":["Fall"],"prereqs":[],"subject":"RELC","credits":4}
,{"_id": "RELC 161","subid":[],"name":"NOT CULTS: CONTROVERSIAL RELIGIOUS MOVEMENTS EAST AND WEST","terms":["Fall"],"prereqs":[],"subject":"RELC","credits":4}
,{"_id": "RELC 173","subid":["AHST 148","ATHS 163"],"name":"INTRODUCTION TO ART AND ARCHITECTURE OF SOUTH ASIA","terms":["Fall"],"prereqs":[],"subject":"RELC","credits":4}
,{"_id": "RELC 175","subid":["CHIN 275","HIST 148"],"name":"RELIGION &AMP; CHINESE SOCIETY","terms":["Fall"],"prereqs":[],"subject":"RELC","credits":4}
,{"_id": "RELC 177","subid":["JWST 177"],"name":"KITCHEN JUDAISM: JEWISH FOOD BEYOND THE BAGEL AND THE BIBLE","terms":["Fall"],"prereqs":[],"subject":"RELC","credits":4}
,{"_id": "RELC 189","subid":["GSWS 189"],"name":"SEXUALITY IN WORLD RELIGIONS","terms":["Fall"],"prereqs":[],"subject":"RELC","credits":4}
,{"_id": "RELC 216","subid":[],"name":"WOMEN AND ISLAM","terms":["Fall"],"prereqs":[],"subject":"RELC","credits":4}
,{"_id": "RELC 225","subid":["AHST 216","AHST 416","CLTR 208H","CLTR 408H","JPNS 216"],"name":"CULTURES OF ENLIGHTENMENT: MEDITATION, MATERIALITY, AND THE LITERARY CULTURES OF JAPANESE BUDDHISM","terms":["Fall"],"prereqs":[],"subject":"RELC","credits":4}
,{"_id": "RELC 229","subid":[],"name":"RELIGION AND VIOLENCE","terms":["Fall"],"prereqs":[],"subject":"RELC","credits":4}
,{"_id": "RELC 252","subid":[],"name":"HEROINES AND HEROES IN INDIA'S MYTHOLOGIES","terms":["Fall"],"prereqs":[],"subject":"RELC","credits":4}
,{"_id": "RELC 259W","subid":["ATHS 259W"],"name":"PUBLIC AND COMMUNITY-ENGAGED ARCHAEOLOGY","terms":["Fall"],"prereqs":[],"subject":"RELC","credits":4}
,{"_id": "RELC 265","subid":["INTR 249","INTR 249W","JWST 265","RELC 265W"],"name":"ISRAEL/PALESTINE","terms":["Fall"],"prereqs":[],"subject":"RELC","credits":4}
,{"_id": "RELC 284","subid":["AAAS 285","EHUM 284","GSWS 285"],"name":"CIVIL DISOBEDIENCE","terms":["Fall"],"prereqs":[],"subject":"RELC","credits":4}
,{"_id": "RELC 285","subid":["AHST 195","CLTR 116","CLTR 253C","ENGL 205","ENGL 405","HIST 135","ITAL 195","ITAL 220","RELC 197"],"name":"DANTE'S DIVINE COMEDY I","terms":["Fall"],"prereqs":[],"subject":"RELC","credits":4}
,{"_id": "RELC 289","subid":["HIST 289","HIST 289W"],"name":"VISIONARIES, MYSTICS, SAINTS-MEDIEVAL &AMP; RENAISSANCE EUR","terms":["Fall"],"prereqs":[],"subject":"RELC","credits":4}
,{"_id": "RELC 292","subid":[],"name":"PARANOIA-- FROM DESCARTES TO TRUMP, A TOUR","terms":["Fall"],"prereqs":[],"subject":"RELC","credits":4}
,{"_id": "RELC 293W","subid":[],"name":"THEORIES OF RELIGION","terms":["Fall"],"prereqs":[],"subject":"RELC","credits":6}
,{"_id": "RELC 160","subid":[],"name":"PARLIAMENT OF WORLDS RELIGIONS: GLOBAL CITIZENSHIP PRACTICUM","terms":["Summer"],"prereqs":[],"subject":"RELC","credits":2}
,{"_id": "RELC 102","subid":[],"name":"INTRODUCTION TO THE NEW TESTAMENT","terms":["Spring"],"prereqs":[],"subject":"RELC","credits":4}
,{"_id": "RELC 106","subid":[],"name":"FROM CONFUCIUS TO ZEN","terms":["Spring"],"prereqs":[],"subject":"RELC","credits":4}
,{"_id": "RELC 108","subid":[],"name":"INTRODUCTION TO THE QURAN","terms":["Spring"],"prereqs":[],"subject":"RELC","credits":4}
,{"_id": "RELC 118","subid":[],"name":"WHAT�S SO FUNNY?: STAND-UP COMEDY AND RELIGION","terms":["Spring"],"prereqs":[],"subject":"RELC","credits":4}
,{"_id": "RELC 121","subid":["CASC 152"],"name":"BRIDGING THE GAP: DIALOGUE ACROSS DIFFERENCE","terms":["Spring"],"prereqs":[],"subject":"RELC","credits":4}
,{"_id": "RELC 130","subid":[],"name":"BUDDHISM: BELIEF AND PRACTICE","terms":["Spring"],"prereqs":[],"subject":"RELC","credits":4}
,{"_id": "RELC 135","subid":["CLST 110"],"name":"CLASSICAL MYTHOLOGY","terms":["Spring"],"prereqs":[],"subject":"RELC","credits":4}
,{"_id": "RELC 168","subid":["AAAS 140","MUSC 139"],"name":"RELIGION AND BLACK POP MUSIC","terms":["Spring"],"prereqs":[],"subject":"RELC","credits":4}
,{"_id": "RELC 169","subid":[],"name":"SPORTS, RACE AND RELIGION","terms":["Spring"],"prereqs":[],"subject":"RELC","credits":4}
,{"_id": "RELC 180","subid":["PHLT 180"],"name":"RELIGION AND PUBLIC HEALTH: COLLABORATION ON THE FRONT LINES","terms":["Spring"],"prereqs":[],"subject":"RELC","credits":4}
,{"_id": "RELC 183","subid":["AAAS 183","HIST 112","PSCI 224"],"name":"INCARCERATION NATION","terms":["Spring"],"prereqs":[],"subject":"RELC","credits":4}
,{"_id": "RELC 186","subid":["ATHS 102"],"name":"RITUAL AND RELIGION IN ARCHAEOLOGICAL PERSPECTIVE","terms":["Spring"],"prereqs":[],"subject":"RELC","credits":4}
,{"_id": "RELC 230","subid":["AAAS 200","ANTH 233","GSWS 233","PSCI 225"],"name":"CULTURAL POLITICS OF PRISON TOWNS","terms":["Spring"],"prereqs":[],"subject":"RELC","credits":4}
,{"_id": "RELC 247","subid":["ANTH 251"],"name":"ISLAMIC MODERNITIES IN AFRICA","terms":["Spring"],"prereqs":[],"subject":"RELC","credits":4}
,{"_id": "RELC 270","subid":[],"name":"THE MEANING OF LIFE: HAPPINESS AND LIBERATION IN THEORY AND PRACTICE","terms":["Spring"],"prereqs":[],"subject":"RELC","credits":4}
,{"_id": "RELC 275","subid":["JWST 275"],"name":"PSYCHOLOGY, RELIGION, ETHICS, LOVE","terms":["Spring"],"prereqs":[],"subject":"RELC","credits":4}
,{"_id": "RELC 287","subid":["GRMN 217","MUSC 207"],"name":"HILDEGARD OF BINGEN AND HER WORLD","terms":["Spring"],"prereqs":["THE 109","THE 117","THE 800"],"subject":"RELC","credits":4}
,{"_id": "RELC 294","subid":["CLST 294"],"name":"ANCIENT ROME IN CONTEXT","terms":["Spring"],"prereqs":[],"subject":"RELC","credits":2}
,{"_id": "RELC 325","subid":["JWST 325"],"name":"RESPONDING TO THE HOLOCAUST","terms":["Spring"],"prereqs":[],"subject":"RELC","credits":4}
,{"_id": "RELC 389W","subid":[],"name":"SENIOR SEMINAR","terms":["Spring"],"prereqs":[],"subject":"RELC","credits":4}
,{"_id": "RELC 390","subid":[],"name":"SUPERVISED TEACHING FOR RELC 183","terms":["Spring"],"prereqs":[],"subject":"RELC","credits":4}
,{"_id": "RELC 392","subid":[],"name":"PRACTICUM","terms":["Spring"],"prereqs":[],"subject":"RELC","credits":4}
,{"_id": "RELC 393","subid":[],"name":"SENIOR PROJECT","terms":["Spring"],"prereqs":[],"subject":"RELC","credits":4}
,{"_id": "RELC 393W","subid":[],"name":"SENIOR PROJECT","terms":["Spring"],"prereqs":[],"subject":"RELC","credits":4}
,{"_id": "RSST 126","subid":["HIST 134","RSST 127","RUSS 126","RUSS 127"],"name":"RUSSIA NOW","terms":["Fall","Spring"],"prereqs":[],"subject":"RSST","credits":4}
,{"_id": "RSST 128","subid":["CLTR 209A","HIST 130","RUSS 128"],"name":"RUSSIAN CIVILIZATION: MYTH, CULTURE, HISTORY","terms":["Fall"],"prereqs":[],"subject":"RSST","credits":4}
,{"_id": "RSST 240","subid":["CLTR 250","CLTR 450","ENGL 243M","RUSS 240"],"name":"NABOKOV- UNUSUAL �MIGR�","terms":["Fall"],"prereqs":[],"subject":"RSST","credits":4}
,{"_id": "RSST 214","subid":["CLTR 214R","RUSS 214"],"name":"RUSSIAN FOLKLORE","terms":["Spring"],"prereqs":[],"subject":"RSST","credits":4}
,{"_id": "RSST 289","subid":["CLTR 289","RUSS 289"],"name":"DANGEROUS TEXTS","terms":["Spring"],"prereqs":[],"subject":"RSST","credits":4}
,{"_id": "RUSS 101","subid":[],"name":"ELEMENTARY RUSSIAN I","terms":["Fall"],"prereqs":[],"subject":"RUSS","credits":4}
,{"_id": "RUSS 126","subid":["HIST 134","RSST 126","RSST 127","RUSS 127"],"name":"RUSSIA NOW","terms":["Fall","Spring"],"prereqs":[],"subject":"RUSS","credits":4}
,{"_id": "RUSS 128","subid":["CLTR 209A","HIST 130","RSST 128"],"name":"RUSSIAN CIVILIZATION: MYTH, CULTURE, HISTORY","terms":["Fall"],"prereqs":[],"subject":"RUSS","credits":4}
,{"_id": "RUSS 151","subid":[],"name":"INTERMEDIATE RUSSIAN I","terms":["Fall"],"prereqs":[],"subject":"RUSS","credits":4}
,{"_id": "RUSS 202","subid":[],"name":"ADVANCED READINGS IN RUSSIAN","terms":["Fall"],"prereqs":[],"subject":"RUSS","credits":4}
,{"_id": "RUSS 240","subid":["CLTR 250","CLTR 450","ENGL 243M","RSST 240"],"name":"NABOKOV- UNUSUAL �MIGR�","terms":["Fall"],"prereqs":[],"subject":"RUSS","credits":4}
,{"_id": "RUSS 390","subid":[],"name":"SUPERVISED TEACHING RUSS 101","terms":["Fall"],"prereqs":[],"subject":"RUSS","credits":4}
,{"_id": "RUSS 390B","subid":[],"name":"SUPERVISED TEACHING","terms":["Fall"],"prereqs":[],"subject":"RUSS","credits":1}
,{"_id": "RUSS 107","subid":[],"name":"RUSSIAN IN ESTONIA","terms":["Summer"],"prereqs":[],"subject":"RUSS","credits":4}
,{"_id": "RUSS 157","subid":[],"name":"RUSSIAN IN ESTONIA","terms":["Summer"],"prereqs":[],"subject":"RUSS","credits":4}
,{"_id": "RUSS 207","subid":[],"name":"RUSSIA IN ESTONIA","terms":["Summer"],"prereqs":[],"subject":"RUSS","credits":4}
,{"_id": "RUSS 102","subid":[],"name":"ELEMENTARY RUSSIAN II","terms":["Spring"],"prereqs":[],"subject":"RUSS","credits":4}
,{"_id": "RUSS 152","subid":[],"name":"INTERMEDIATE RUSSIAN II","terms":["Spring"],"prereqs":[],"subject":"RUSS","credits":4}
,{"_id": "RUSS 209","subid":[],"name":"ADVANCED RUSSIAN THROUGH FILM","terms":["Spring"],"prereqs":[],"subject":"RUSS","credits":4}
,{"_id": "RUSS 214","subid":["CLTR 214R","RSST 214"],"name":"RUSSIAN FOLKLORE","terms":["Spring"],"prereqs":[],"subject":"RUSS","credits":4}
,{"_id": "RUSS 215","subid":[],"name":"ADVANCED RUSSIAN LITERATURE IN ORIGINAL II","terms":["Spring"],"prereqs":[],"subject":"RUSS","credits":4}
,{"_id": "RUSS 289","subid":["CLTR 289","RSST 289"],"name":"DANGEROUS TEXTS","terms":["Spring"],"prereqs":[],"subject":"RUSS","credits":4}
,{"_id": "RUSS 392","subid":[],"name":"PRACTICUM","terms":["Spring"],"prereqs":[],"subject":"RUSS","credits":4}
,{"_id": "SABR 302","subid":[],"name":"STUDY ABROAD NON-UR PROGRAM","terms":["Fall"],"prereqs":[],"subject":"SABR","credits":0}
,{"_id": "SABR 306C","subid":[],"name":"BIOLOGY IN GALAPAGOS ISLANDS","terms":["Fall"],"prereqs":[],"subject":"SABR","credits":0}
,{"_id": "SABR 303","subid":[],"name":"ROCHESTER ABROAD","terms":["Summer"],"prereqs":[],"subject":"SABR","credits":0}
,{"_id": "SABR 304","subid":[],"name":"ROCHESTER ABROAD","terms":["Summer"],"prereqs":[],"subject":"SABR","credits":0}
,{"_id": "SABR 293","subid":[],"name":"ROCHESTER IN AREZZO ITALY SEM","terms":["Spring"],"prereqs":[],"subject":"SABR","credits":0}
,{"_id": "SART 111","subid":[],"name":"INTRODUCTION TO DRAWING","terms":["Fall","Spring"],"prereqs":[],"subject":"SART","credits":4}
,{"_id": "SART 121","subid":[],"name":"INTRODUCTION TO PAINTING","terms":["Fall","Spring"],"prereqs":[],"subject":"SART","credits":4}
,{"_id": "SART 131","subid":[],"name":"INTRODUCTION TO SCULPTURE","terms":["Fall","Spring"],"prereqs":[],"subject":"SART","credits":4}
,{"_id": "SART 141","subid":["DMST 112"],"name":"INTRODUCTION TO PHOTOGRAPHY","terms":["Fall","Summer"],"prereqs":[],"subject":"SART","credits":4}
,{"_id": "SART 151","subid":["DMST 111","FMST 205"],"name":"NEW MEDIA AND EMERGING PRACTICE","terms":["Fall","Spring"],"prereqs":[],"subject":"SART","credits":4}
,{"_id": "SART 153","subid":["AAAS 154","DMST 153","EHUM 153","FMST 153","MUSC 173"],"name":"INTRODUCTION TO SOUND ART","terms":["Fall"],"prereqs":[],"subject":"SART","credits":4}
,{"_id": "SART 161","subid":["ENGL 161","FMST 161"],"name":"INTRODUCTION TO VIDEO ART","terms":["Fall"],"prereqs":[],"subject":"SART","credits":4}
,{"_id": "SART 182","subid":[],"name":"INTRODUCTION TO PRINTMAKING","terms":["Fall"],"prereqs":[],"subject":"SART","credits":4}
,{"_id": "SART 190","subid":[],"name":"INTRODUCTION TO STUDIO PRACTICE","terms":["Fall"],"prereqs":[],"subject":"SART","credits":4}
,{"_id": "SART 209","subid":["AHST 209"],"name":"WRITING ON ART","terms":["Fall"],"prereqs":[],"subject":"SART","credits":4}
,{"_id": "SART 222A","subid":["SART 222B","SART 222C"],"name":"ADVANCED PAINTING","terms":["Fall","Spring"],"prereqs":[],"subject":"SART","credits":4}
,{"_id": "SART 232A","subid":["SART 232B","SART 232C"],"name":"ADVANCED SCULPTURE","terms":["Fall"],"prereqs":[],"subject":"SART","credits":4}
,{"_id": "SART 244A","subid":["SART 244B","SART 244C"],"name":"EXPANDED PHOTOGRAPHY: BOOKS AND BOXES","terms":["Fall"],"prereqs":["THE 141","THE 151"],"subject":"SART","credits":4}
,{"_id": "SART 252A","subid":["EHUM 258","FMST 252","SART 252B","SART 252C","SUST 252"],"name":"NEW MEDIA AND EMERGING PRACTICES: ART ENVIRONMENT ACTION","terms":["Fall"],"prereqs":[],"subject":"SART","credits":4}
,{"_id": "SART 272A","subid":["SART 272B","SART 272C"],"name":"ADVANCED DRAWING &AMP; COLLAGE","terms":["Fall"],"prereqs":["SART 111","SART 181","SART 182","SART 190"],"subject":"SART","credits":4}
,{"_id": "SART 279","subid":["AHST 231"],"name":"GALLERY PRACTICUM","terms":["Fall","Spring"],"prereqs":[],"subject":"SART","credits":4}
,{"_id": "SART 281A","subid":["SART 281B","SART 281C"],"name":"PERFORMANCE ART &AMP; SOCIAL ENGAGEMENT","terms":["Fall"],"prereqs":["THE 196"],"subject":"SART","credits":4}
,{"_id": "SART 282A","subid":["SART 282B","SART 282C"],"name":"ADVANCED PRINTMAKING","terms":["Fall"],"prereqs":[],"subject":"SART","credits":4}
,{"_id": "SART 390","subid":[],"name":"SUPERVISED TEACHING - SART 182","terms":["Fall"],"prereqs":[],"subject":"SART","credits":4}
,{"_id": "SART 393","subid":[],"name":"SENIOR PROJECT","terms":["Fall"],"prereqs":[],"subject":"SART","credits":4}
,{"_id": "SART 394","subid":[],"name":"INTERNSHIP","terms":["Fall"],"prereqs":[],"subject":"SART","credits":4}
,{"_id": "SART 396","subid":[],"name":"SENIOR STUDIO AND SEMINAR","terms":["Fall"],"prereqs":[],"subject":"SART","credits":4}
,{"_id": "SART 114","subid":["AHST 114"],"name":"CREATING ARCHITECTURE","terms":["Spring"],"prereqs":[],"subject":"SART","credits":4}
,{"_id": "SART 181","subid":[],"name":"INTRO TO PRINTMAKING: RELIEF &AMP; INTAGLIO","terms":["Spring"],"prereqs":[],"subject":"SART","credits":4}
,{"_id": "SART 242A","subid":["SART 242B","SART 242C"],"name":"EXPANDED PHOTOGRAPHY: REMIXES &AMP; COLLAGES","terms":["Spring"],"prereqs":[],"subject":"SART","credits":4}
,{"_id": "SART 292A","subid":["SART 292B","SART 292C"],"name":"MARKINGS, METHODS &AMP; MATERIALS","terms":["Spring"],"prereqs":[],"subject":"SART","credits":4}
,{"_id": "SART 300","subid":[],"name":"ART NEW YORK NEW FIELD STUDIO","terms":["Spring"],"prereqs":[],"subject":"SART","credits":4}
,{"_id": "SART 305K","subid":[],"name":"ART NEW YORK COLLOQUIM","terms":["Spring"],"prereqs":[],"subject":"SART","credits":4}
,{"_id": "SART 391W","subid":[],"name":"INDEPENDENT STUDY - MIXED MEDIA SCREENWRITING","terms":["Spring"],"prereqs":[],"subject":"SART","credits":0}
,{"_id": "SART 392","subid":[],"name":"PRACTICUM","terms":["Spring"],"prereqs":[],"subject":"SART","credits":4}
,{"_id": "SART 392A","subid":[],"name":"PRACTICUM - ART NY","terms":["Spring"],"prereqs":[],"subject":"SART","credits":8}
,{"_id": "SART 397","subid":[],"name":"SENIOR STUDIO &AMP; SEMINAR","terms":["Spring"],"prereqs":[],"subject":"SART","credits":4}
,{"_id": "SART 399","subid":[],"name":"SENIOR THESIS EXHIBITION","terms":["Spring"],"prereqs":[],"subject":"SART","credits":1}
,{"_id": "SOCI 210","subid":[],"name":"SILICON VALLEY AND ITS NETWORKS","terms":["Spring"],"prereqs":[],"subject":"SOCI","credits":4}
,{"_id": "SOCI 212","subid":[],"name":"SILICON VALLEY SANDBOX","terms":["Spring"],"prereqs":[],"subject":"SOCI","credits":2}
,{"_id": "SPAN 101","subid":[],"name":"ELEMENTARY SPANISH I","terms":["Fall","Spring"],"prereqs":[],"subject":"SPAN","credits":4}
,{"_id": "SPAN 102","subid":[],"name":"ELEMENTARY SPANISH II","terms":["Fall","Spring"],"prereqs":[],"subject":"SPAN","credits":4}
,{"_id": "SPAN 151","subid":[],"name":"INTERMEDIATE SPANISH I","terms":["Fall","Spring"],"prereqs":[],"subject":"SPAN","credits":4}
,{"_id": "SPAN 152","subid":[],"name":"INTERMEDIATE SPANISH II","terms":["Fall","Spring"],"prereqs":[],"subject":"SPAN","credits":4}
,{"_id": "SPAN 159","subid":[],"name":"SPANISH FOR HERITAGE SPEAKER","terms":["Fall"],"prereqs":[],"subject":"SPAN","credits":4}
,{"_id": "SPAN 161","subid":[],"name":"ADVANCED SPANISH GRAMMAR","terms":["Fall","Spring"],"prereqs":["SPAN 152","SPAN 200","SPAN 202"],"subject":"SPAN","credits":2}
,{"_id": "SPAN 162","subid":[],"name":"ADVANCED CONVERSATIONAL SPANISH","terms":["Fall","Spring"],"prereqs":[],"subject":"SPAN","credits":2}
,{"_id": "SPAN 200","subid":[],"name":"ADVANCED SPANISH COMPOSITION","terms":["Fall","Spring"],"prereqs":[],"subject":"SPAN","credits":4}
,{"_id": "SPAN 215","subid":["CLTR 256B","ENGL 243A"],"name":"DON QUIJOTE: THE BOOK, THE MYTH, THE IMAGE","terms":["Fall"],"prereqs":[],"subject":"SPAN","credits":4}
,{"_id": "SPAN 248","subid":[],"name":"OTRAS VANGUARDIAS: REVOLUTIONARY ARTISTIC MOVEMENTS IN THE AMERICAS","terms":["Fall"],"prereqs":[],"subject":"SPAN","credits":4}
,{"_id": "SPAN 259","subid":[],"name":"EXITOS DE TAQUILLA: BLOCKBUSTER FILMS FROM SPAIN AND SPANISH AMERICA","terms":["Fall"],"prereqs":[],"subject":"SPAN","credits":4}
,{"_id": "SPAN 392","subid":[],"name":"PRACTICUM","terms":["Fall","Spring"],"prereqs":[],"subject":"SPAN","credits":4}
,{"_id": "SPAN 394","subid":[],"name":"INTERNSHIP","terms":["Fall"],"prereqs":[],"subject":"SPAN","credits":4}
,{"_id": "SPAN 157","subid":[],"name":"SPANISH IN SPAIN","terms":["Summer"],"prereqs":[],"subject":"SPAN","credits":4}
,{"_id": "SPAN 207","subid":[],"name":"SPANISH IN SPAIN","terms":["Summer"],"prereqs":[],"subject":"SPAN","credits":4}
,{"_id": "SPAN 203","subid":[],"name":"REPRESENTING IDENTITIES IN THE EARLY MODERN HISPANIC WORLD","terms":["Spring"],"prereqs":[],"subject":"SPAN","credits":4}
,{"_id": "SPAN 249D","subid":["SPAN 449D"],"name":"BUNUEL, DALI, LORCA","terms":["Spring"],"prereqs":[],"subject":"SPAN","credits":4}
,{"_id": "SPAN 275","subid":[],"name":"MARX AND FREUD IN LATIN AMERICA","terms":["Spring"],"prereqs":["SPAN 200"],"subject":"SPAN","credits":4}
,{"_id": "SPAN 282","subid":["AAAS 208","GSWS 282","SPAN 482"],"name":"SI EL NORTE FUERA EL SUR: LATINX LITERATURE AND THOUGHT","terms":["Spring"],"prereqs":["SPAN 200"],"subject":"SPAN","credits":4}
,{"_id": "SPAN 393","subid":[],"name":"SENIOR PROJECT","terms":["Spring"],"prereqs":[],"subject":"SPAN","credits":4}
,{"_id": "STAT 201","subid":["MATH 201"],"name":"INTRO TO PROBABILITY","terms":["Fall","Spring"],"prereqs":["MTH 162","MTH 201"],"subject":"STAT","credits":4}
,{"_id": "STAT 203","subid":["MATH 203"],"name":"INTRO TO MATH STATISTICS","terms":["Fall","Spring"],"prereqs":["SPAN 203","SPAN 201"],"subject":"STAT","credits":4}
,{"_id": "STAT 212","subid":[],"name":"APPLIED STATISTICS I","terms":["Fall","Summer","Spring"],"prereqs":[],"subject":"STAT","credits":4}
,{"_id": "STAT 213","subid":[],"name":"ELEMENTS PROB &AMP; MATH STAT","terms":["Fall","Spring"],"prereqs":["MTH 141","STAT 211","STAT 212","STAT 213","STAT 214"],"subject":"STAT","credits":4}
,{"_id": "STAT 216","subid":["STAT 416"],"name":"APPLIED STATISTICAL METHODS I","terms":["Fall","Summer","Spring"],"prereqs":["STAT 211","STAT 212","STAT 213","STAT 416","STAT 216"],"subject":"STAT","credits":4}
,{"_id": "STAT 218","subid":["STAT 418"],"name":"CATEGORICAL DATA ANALYSIS","terms":["Fall"],"prereqs":[],"subject":"STAT","credits":4}
,{"_id": "STAT 221W","subid":["BST 421"],"name":"SAMPLING TECHNIQUES","terms":["Fall"],"prereqs":["BST 421","STAT 221","STAT 211","STAT 212","STAT 213","STAT 203"],"subject":"STAT","credits":4}
,{"_id": "STAT 262","subid":["CSC 262","DSCC 262"],"name":"COMPUTATIONAL INTRODUCTION TO STATISTICS","terms":["Fall","Summer"],"prereqs":["THE 150","THE 142","THE 161","THE 171"],"subject":"STAT","credits":4}
,{"_id": "STAT 277","subid":["STAT 477"],"name":"INTRO STATISTICAL SOFTWARE I","terms":["Fall"],"prereqs":["STAT 277","STAT 477","STAT 211","STAT 212","STAT 213","STAT 216","STAT 226"],"subject":"STAT","credits":4}
,{"_id": "STAT 390","subid":[],"name":"SUPERVISED TEACHING-STT DEPT","terms":["Fall"],"prereqs":[],"subject":"STAT","credits":4}
,{"_id": "STAT 390A","subid":[],"name":"SUPERVISED TEACHING-STT DEPT","terms":["Fall"],"prereqs":[],"subject":"STAT","credits":2}
,{"_id": "STAT 392","subid":[],"name":"PRACTICUM","terms":["Fall","Spring"],"prereqs":[],"subject":"STAT","credits":0}
,{"_id": "STAT 394","subid":[],"name":"INTERNSHIP IN STATISTICS","terms":["Fall"],"prereqs":[],"subject":"STAT","credits":4}
,{"_id": "STAT 226W","subid":[],"name":"INTRO TO LINEAR MODELS","terms":["Summer","Spring"],"prereqs":[],"subject":"STAT","credits":4}
,{"_id": "STAT 215","subid":["STAT 415"],"name":"DESIGN AND ANALYSIS OF EXPERIMENTS","terms":["Spring"],"prereqs":[],"subject":"STAT","credits":4}
,{"_id": "STAT 217","subid":[],"name":"APPLIED STATISTICAL METHODS II","terms":["Spring"],"prereqs":["STAT 417","STAT 217","STAT 216"],"subject":"STAT","credits":4}
,{"_id": "STAT 223","subid":["STAT 423"],"name":"INTRO TO BAYESIAN INFERENCE","terms":["Spring"],"prereqs":["STAT 223","STAT 423","STAT 203","STAT 164"],"subject":"STAT","credits":4}
,{"_id": "STAT 276","subid":["STAT 276W","STAT 476"],"name":"STATISTICAL COMPUTING IN R","terms":["Spring"],"prereqs":["STAT 476","STAT 276","STAT 211","STAT 212","STAT 213"],"subject":"STAT","credits":4}
,{"_id": "STR 221","subid":[],"name":"BUSINESS STRATEGY","terms":["Spring"],"prereqs":["SPAN 207"],"subject":"STR","credits":4}
,{"_id": "SUST 101","subid":["EESC 101"],"name":"INTRODUCTION TO EARTH SCIENCES","terms":["Fall"],"prereqs":[],"subject":"SUST","credits":4}
,{"_id": "SUST 112","subid":["PHLT 101"],"name":"INTRO TO PUBLIC HEALTH","terms":["Fall","Spring"],"prereqs":[],"subject":"SUST","credits":4}
,{"_id": "SUST 113","subid":[],"name":"CONCEPTS OF EPIDEMIOLOGY","terms":["Fall"],"prereqs":[],"subject":"SUST","credits":4}
,{"_id": "SUST 114","subid":["EHUM 103","PHIL 103"],"name":"MORAL PROBLEMS","terms":["Fall","Spring"],"prereqs":[],"subject":"SUST","credits":4}
,{"_id": "SUST 205","subid":["INTR 205"],"name":"GLOBAL SUSTAINABLE DEVELOPMENT","terms":["Fall"],"prereqs":[],"subject":"SUST","credits":4}
,{"_id": "SUST 223","subid":["PHIL 223","PHIL 223W"],"name":"SOCIAL &AMP;POLITICAL PHILOSOPHY","terms":["Fall"],"prereqs":[],"subject":"SUST","credits":4}
,{"_id": "SUST 228","subid":["PHIL 228","PHIL 228W","PHIL 428"],"name":"PUBLIC HEALTH ETHICS","terms":["Fall"],"prereqs":[],"subject":"SUST","credits":4}
,{"_id": "SUST 238","subid":["ECON 238","ECON 238W"],"name":"ENVIRONMENTAL ECONOMICS","terms":["Fall"],"prereqs":[],"subject":"SUST","credits":4}
,{"_id": "SUST 241","subid":["EHUM 268","ENGL 310","FMST 275"],"name":"DECOLONIZING FOOD (FORMERLY FOOD MEDIA LITERATURE)","terms":["Fall"],"prereqs":[],"subject":"SUST","credits":4}
,{"_id": "SUST 245","subid":["AAAS 245","EHUM 245","ENGL 212","FMST 274"],"name":"RACE, COLONIALISM, AND NATURE (FORMERLY ENVIRONMENTAL LITERATURE)","terms":["Fall"],"prereqs":[],"subject":"SUST","credits":4}
,{"_id": "SUST 252","subid":["EHUM 258","FMST 252","SART 252A","SART 252B","SART 252C"],"name":"NEW MEDIA AND EMERGING PRACTICES: ART ENVIRONMENT ACTION","terms":["Fall"],"prereqs":[],"subject":"SUST","credits":4}
,{"_id": "SUST 304","subid":[],"name":"ECOREPS LEADERS","terms":["Fall","Spring"],"prereqs":[],"subject":"SUST","credits":1}
,{"_id": "SUST 103","subid":["EESC 103"],"name":"INTRO TO ENVIRONMNTL SCIENCE","terms":["Spring"],"prereqs":[],"subject":"SUST","credits":4}
,{"_id": "SUST 201","subid":["EESC 201"],"name":"EVOLUTION OF THE EARTH","terms":["Spring"],"prereqs":[],"subject":"SUST","credits":4}
,{"_id": "SUST 210","subid":["PHLT 201W"],"name":"ENVIRONMENTAL HEALTH","terms":["Spring"],"prereqs":[],"subject":"SUST","credits":4}
,{"_id": "SUST 220","subid":["DANC 233","DMST 230","EHUM 233"],"name":"CLIMATE INTERVENTIONS: PERFORMING ARTS + NEW MEDIA","terms":["Spring"],"prereqs":[],"subject":"SUST","credits":4}
,{"_id": "SUST 224","subid":["ANTH 224"],"name":"ANTHROPOLOGY OF DEVELOPMENT","terms":["Spring"],"prereqs":[],"subject":"SUST","credits":4}
,{"_id": "SUST 233A","subid":["AHST 286A","ATHS 233A"],"name":"CLIMATE CHANGE AND THE AFRICAN CULTURAL HERITAGE","terms":["Spring"],"prereqs":[],"subject":"SUST","credits":4}
,{"_id": "SUST 310","subid":["EESC 310","EESC 310W"],"name":"SCIENCE &AMP; SUSTAINABILITY","terms":["Spring"],"prereqs":[],"subject":"SUST","credits":4}
,{"_id": "TCS 442","subid":["CSC 442"],"name":"ARTIFICIAL INTELLIGENCE","terms":["Fall"],"prereqs":[],"subject":"TCS","credits":4}
,{"_id": "TCS 444","subid":["CSC 244","CSC 444"],"name":"MACHINE REASONING","terms":["Fall"],"prereqs":[],"subject":"TCS","credits":4}
,{"_id": "TCS 446","subid":["CSC 446","ECE 409"],"name":"MACHINE LEARNING","terms":["Fall","Spring"],"prereqs":["MTH 165","MTH 164","CSC 242","CSC 446","CSC 246"],"subject":"TCS","credits":4}
,{"_id": "TCS 447","subid":["BCSC 235","BCSC 435","CSC 247","CSC 447","LING 247","LING 447"],"name":"NATURAL LANGUAGE PROCESSING","terms":["Fall","Spring"],"prereqs":["CSC 447","CSC 242"],"subject":"TCS","credits":4}
,{"_id": "TCS 452","subid":["CSC 252","CSC 452"],"name":"COMPUTER ORGANIZATION","terms":["Fall","Spring"],"prereqs":["MTH 150","CSC 172"],"subject":"TCS","credits":4}
,{"_id": "TCS 453","subid":["CSC 253","CSC 453"],"name":"COLLABORATIVE PROGRAMMING &AMP; SOFTWARE DESIGN","terms":["Fall"],"prereqs":["CSC 453","CSC 172","CSC 253","CSC 252"],"subject":"TCS","credits":4}
,{"_id": "TCS 454","subid":["CSC 254","CSC 454"],"name":"PROG LANGUAGE DESIGN &AMP; IMP.","terms":["Fall"],"prereqs":["CSC 173","CSC 252"],"subject":"TCS","credits":4}
,{"_id": "TCS 457","subid":["CSC 257","CSC 457"],"name":"COMPUTER NETWORKS","terms":["Fall"],"prereqs":[],"subject":"TCS","credits":4}
,{"_id": "TCS 461","subid":["CSC 261","CSC 461","DSCC 261","DSCC 461"],"name":"DATABASE SYSTEMS","terms":["Fall","Summer","Spring"],"prereqs":[],"subject":"TCS","credits":4}
,{"_id": "TCS 480","subid":["CSC 280","CSC 480"],"name":"COMPUTER MODELS &AMP; LIMITATIONS","terms":["Fall","Spring"],"prereqs":["CSC 173","MTH 150"],"subject":"TCS","credits":4}
,{"_id": "TCS 481","subid":["CSC 281","CSC 481"],"name":"INTRO TO CRYPTOGRAPHY","terms":["Fall"],"prereqs":[],"subject":"TCS","credits":4}
,{"_id": "TCS 482","subid":["CSC 282","CSC 482"],"name":"DESIGN &AMP; ANALYSIS OF EFFICIENT ALGORITHMS","terms":["Fall","Spring"],"prereqs":["CSC 172","MTH 150"],"subject":"TCS","credits":4}
,{"_id": "TCS 484","subid":["CSC 284","CSC 484"],"name":"ADVANCED ALGORITHMS","terms":["Fall"],"prereqs":[],"subject":"TCS","credits":4}
,{"_id": "TCS 487","subid":["CSC 287","CSC 487"],"name":"SAMPLING ALGORITHMS","terms":["Fall"],"prereqs":[],"subject":"TCS","credits":4}
,{"_id": "TCS 440","subid":["CSC 240","CSC 440","DSCC 240","DSCC 440"],"name":"DATA MINING","terms":["Spring"],"prereqs":[],"subject":"TCS","credits":4}
,{"_id": "TCS 449","subid":["BCSC 236","BCSC 536","CSC 249","CSC 449","ECE 449"],"name":"MACHINE VISION","terms":["Spring"],"prereqs":["CSC 449","MTH 161","CSC 242","MTH 165"],"subject":"TCS","credits":4}
,{"_id": "TCS 455","subid":["CSC 255","CSC 455","ECE 455"],"name":"SOFTWARE ANALYSIS &AMP; IMPROV","terms":["Spring"],"prereqs":["CSC 252","CSC 254"],"subject":"TCS","credits":4}
,{"_id": "TCS 458","subid":["CSC 258","CSC 458"],"name":"PARALLEL &AMP; DIST. SYSTEMS","terms":["Spring"],"prereqs":[],"subject":"TCS","credits":4}
,{"_id": "TCS 478","subid":["CSC 278","CSC 478"],"name":"COMPUTER SECURITY FOUNDATIONS","terms":["Spring"],"prereqs":["CSC 252","CSC 452","ECE 200"],"subject":"TCS","credits":4}
,{"_id": "TCS 486","subid":["CSC 286","CSC 486"],"name":"COMPUTATIONAL COMPLEXITY","terms":["Spring"],"prereqs":["CSC 280"],"subject":"TCS","credits":4}
,{"_id": "TEB 211","subid":["BME 211","BME 411","TEB 411"],"name":"CELLULAR&AMP;MOLECULAR BIO FOUND","terms":["Fall"],"prereqs":["BIOL 110"],"subject":"TEB","credits":4}
,{"_id": "TEB 260","subid":["BME 260","BME 460","TEB 460"],"name":"QUANTITATIVE PHYSIOLOGY","terms":["Fall"],"prereqs":["ECE 113","BME 210"],"subject":"TEB","credits":4}
,{"_id": "TEB 428","subid":["BME 228","BME 428"],"name":"PHYSIOLOGICAL CONTROL SYSTMS","terms":["Fall"],"prereqs":[],"subject":"TEB","credits":4}
,{"_id": "TEB 453","subid":["BME 253","BME 453","ECE 251","ECE 453","PHYS 257","PHYS 467"],"name":"ULTRASOUND IMAGING","terms":["Fall"],"prereqs":[],"subject":"TEB","credits":4}
,{"_id": "TEC 441","subid":["CHE 441"],"name":"ADV TRANSPORT PHENOMENON","terms":["Fall"],"prereqs":[],"subject":"TEC","credits":4}
,{"_id": "TEC 454","subid":["CHE 454","MSC 454"],"name":"INTERFACIAL ENGINEERING","terms":["Fall"],"prereqs":[],"subject":"TEC","credits":4}
,{"_id": "TEC 458","subid":["CHE 258","CHE 458","MSC 458"],"name":"ELECTROCHEM BATT &AMP; FUEL CELL","terms":["Fall"],"prereqs":[],"subject":"TEC","credits":4}
,{"_id": "TEC 487","subid":["CHE 287","CHE 487","CHEM 487"],"name":"SURFACE ANALYSIS","terms":["Fall"],"prereqs":[],"subject":"TEC","credits":4}
,{"_id": "TEC 465","subid":["CHE 465"],"name":"GREEN CHEMICAL ENGINEERING","terms":["Spring"],"prereqs":[],"subject":"TEC","credits":4}
,{"_id": "TEE 423","subid":["ECE 223","ECE 423","MSC 423"],"name":"SEMICONDUCTOR DEVICES","terms":["Fall"],"prereqs":[],"subject":"TEE","credits":4}
,{"_id": "TEE 436","subid":["ECE 436","MSC 437","OPT 464"],"name":"NANOPHOTONIC DEVICES","terms":["Fall","Spring"],"prereqs":[],"subject":"TEE","credits":4}
,{"_id": "TEE 440","subid":["DSCC 420","ECE 271","ECE 440","OPT 413"],"name":"INTRO TO RANDOM PROCESSES","terms":["Fall"],"prereqs":["ECE 242"],"subject":"TEE","credits":4}
,{"_id": "TEE 446","subid":["ECE 246","ECE 446"],"name":"DIGITAL SIGNAL PROCESSING","terms":["Fall"],"prereqs":[],"subject":"TEE","credits":4}
,{"_id": "TEE 447","subid":["CSC 227","CSC 427","ECE 247","ECE 447"],"name":"INTRO TO DIP USING PYTHON","terms":["Fall"],"prereqs":[],"subject":"TEE","credits":4}
,{"_id": "TEE 476","subid":["AME 264","ECE 476"],"name":"AUDIO SOFTWARE DES II","terms":["Fall"],"prereqs":["AME 262","ECE 475"],"subject":"TEE","credits":4}
,{"_id": "TEE 477","subid":["AME 277","CSC 264","CSC 464","ECE 277","ECE 477"],"name":"COMPUTER AUDITION","terms":["Fall"],"prereqs":["ECE 246","ECE 446","ECE 272","ECE 472"],"subject":"TEE","credits":4}
,{"_id": "TEE 404","subid":["CSC 404","ECE 204","ECE 404"],"name":"MULTIPROCESSOR ARCH","terms":["Spring"],"prereqs":[],"subject":"TEE","credits":4}
,{"_id": "TEE 408","subid":["ECE 208","ECE 408"],"name":"THE ART OF MACHINE LEARNING","terms":["Spring"],"prereqs":["ECE 114","MTH 165","ECE 270"],"subject":"TEE","credits":4}
,{"_id": "TEE 433","subid":["AME 233","ECE 233","ECE 433","PHYS 233"],"name":"MUSICAL ACOUSTICS","terms":["Spring"],"prereqs":[],"subject":"TEE","credits":4}
,{"_id": "TEE 472","subid":["AME 272","ECE 272","ECE 472"],"name":"AUDIO SIG PROC","terms":["Spring"],"prereqs":[],"subject":"TEE","credits":4}
,{"_id": "TEE 475","subid":["AME 262","ECE 475"],"name":"AUDIO SOFTWARE DESIGN","terms":["Spring"],"prereqs":["ECE 114"],"subject":"TEE","credits":4}
,{"_id": "TEM 401","subid":[],"name":"ECONOMICS, MARKETING &AMP; STRATEGY","terms":["Fall"],"prereqs":[],"subject":"TEM","credits":4}
,{"_id": "TEM 402","subid":[],"name":"ACCOUNTING &AMP; FINANCE PRIMER FOR ENTREPRENEURS","terms":["Fall"],"prereqs":[],"subject":"TEM","credits":4}
,{"_id": "TEM 440","subid":[],"name":"SCREENING TECHNICAL OPPORTUNITIES","terms":["Fall"],"prereqs":[],"subject":"TEM","credits":1}
,{"_id": "TEM 494","subid":[],"name":"INTERNSHIP","terms":["Fall"],"prereqs":[],"subject":"TEM","credits":1}
,{"_id": "TEM 895","subid":[],"name":"CONT OF MASTER'S ENROLLMENT","terms":["Fall","Spring"],"prereqs":[],"subject":"TEM","credits":0}
,{"_id": "TEM 897","subid":[],"name":"MASTER'S DISSERTATION","terms":["Fall","Spring"],"prereqs":[],"subject":"TEM","credits":0}
,{"_id": "TEM 899","subid":[],"name":"MASTER'S DISSERTATION","terms":["Fall","Spring"],"prereqs":[],"subject":"TEM","credits":0}
,{"_id": "TEM 411","subid":["OPT 481"],"name":"GEN MANAGEMNT OF NEW VENTURE","terms":["Spring"],"prereqs":[],"subject":"TEM","credits":4}
,{"_id": "TEM 441","subid":["OPT 482"],"name":"PRODUCT DEV &AMP; TECH MGMT","terms":["Spring"],"prereqs":[],"subject":"TEM","credits":4}
,{"_id": "TEM 491","subid":[],"name":"MASTER'S READING","terms":["Spring"],"prereqs":[],"subject":"TEM","credits":5}
,{"_id": "TEO 425","subid":["OPT 425"],"name":"RADIATION &AMP; DETECTORS","terms":["Fall"],"prereqs":[],"subject":"TEO","credits":4}
,{"_id": "TEO 441","subid":["OPT 441"],"name":"GEOMETRICAL OPTICS","terms":["Fall"],"prereqs":[],"subject":"TEO","credits":4}
,{"_id": "TEO 463","subid":["OPT 463"],"name":"WAVE OPTICS &AMP; IMAGING","terms":["Fall"],"prereqs":[],"subject":"TEO","credits":4}
,{"_id": "TEO 467","subid":["OPT 467","PHYS 437"],"name":"NONLINEAR OPTICS","terms":["Fall"],"prereqs":[],"subject":"TEO","credits":4}
,{"_id": "TEO 468","subid":["ECE 426","OPT 468"],"name":"INTEGRATED PHOTONICS","terms":["Fall"],"prereqs":[],"subject":"TEO","credits":4}
,{"_id": "TEO 412","subid":["OPT 412"],"name":"QUANTUM MECHANICS FOR OPTICS","terms":["Spring"],"prereqs":[],"subject":"TEO","credits":4}
,{"_id": "TEO 421","subid":["ECE 421","MSC 470","OPT 421"],"name":"OPT PROPERTIES OF MATERIALS","terms":["Spring"],"prereqs":[],"subject":"TEO","credits":4}
,{"_id": "TEO 423","subid":["OPT 423"],"name":"DETECTION OF OPTCL RADIATION","terms":["Spring"],"prereqs":[],"subject":"TEO","credits":4}
,{"_id": "TEO 442","subid":["OPT 442"],"name":"INSTRUMENTAL OPT","terms":["Spring"],"prereqs":[],"subject":"TEO","credits":4}
,{"_id": "TEO 447","subid":["OPT 247","OPT 447"],"name":"ADVANCED OPTICAL COATINGS","terms":["Spring"],"prereqs":[],"subject":"TEO","credits":4}
,{"_id": "TEO 448","subid":["BCSC 223","OPT 248","OPT 448"],"name":"VISION AND THE EYE","terms":["Spring"],"prereqs":[],"subject":"TEO","credits":4}
,{"_id": "TEO 462","subid":["OPT 462"],"name":"ELECTROMAG WAVES","terms":["Spring"],"prereqs":[],"subject":"TEO","credits":4}
,{"_id": "TEO 465","subid":["ME 465","MSC 465","OPT 465","PHYS 435"],"name":"PRINCIPLES OF LASERS","terms":["Spring"],"prereqs":[],"subject":"TEO","credits":4}
,{"_id": "TME 434","subid":["ME 434","PHYS 454"],"name":"INTRO TO PLASMA PHYSICS I","terms":["Fall"],"prereqs":[],"subject":"TME","credits":4}
,{"_id": "TME 441","subid":["BME 486","ME 254","ME 441"],"name":"FINITE ELEMENTS METHODS","terms":["Fall"],"prereqs":[],"subject":"TME","credits":4}
,{"_id": "TME 445","subid":["ME 245","ME 445","OPT 245","OPT 445"],"name":"PRECISION INSTRUMENT DESIGN","terms":["Fall"],"prereqs":[],"subject":"TME","credits":4}
,{"_id": "TME 449","subid":["ME 449"],"name":"ELASTICITY","terms":["Fall"],"prereqs":[],"subject":"TME","credits":4}
,{"_id": "TME 424","subid":["ME 222","ME 424","MSC 424"],"name":"ROBUST DESIGN/QUALITY","terms":["Spring"],"prereqs":[],"subject":"TME","credits":4}
,{"_id": "TME 432","subid":["ME 232","ME 432","MSC 432","OPT 232","OPT 432"],"name":"OPTO-MECHANICAL","terms":["Spring"],"prereqs":[],"subject":"TME","credits":4}
,{"_id": "TME 435","subid":["ME 435","PHYS 455"],"name":"INTRO TO PLASMA PHYSICS II","terms":["Spring"],"prereqs":[],"subject":"TME","credits":4}
,{"_id": "TME 436","subid":["ME 436"],"name":"COMPRESSIBLE FLOW","terms":["Spring"],"prereqs":[],"subject":"TME","credits":4}
,{"_id": "TME 444","subid":["ME 444"],"name":"CONTINUUM MECHANICS","terms":["Spring"],"prereqs":[],"subject":"TME","credits":4}
,{"_id": "WRTG 101","subid":[],"name":"EAPP COMMUNICATION ACROSS CONTEXTS I","terms":["Fall"],"prereqs":["WRTG 101","WRTG 102"],"subject":"WRTG","credits":2}
,{"_id": "WRTG 103","subid":[],"name":"EAPP CRITICAL READING, REASONING &AMP; WRITING","terms":["Fall"],"prereqs":["SPAN 103","WRTG 104"],"subject":"WRTG","credits":6}
,{"_id": "WRTG 105","subid":[],"name":"FRIENDSHIP, IDENTITY, AND SOCIETY","terms":["Fall","Summer","Spring"],"prereqs":[],"subject":"WRTG","credits":4}
,{"_id": "WRTG 105A","subid":[],"name":"CONTEMPLATING MINDFULNESS IN WRITING AND BEYOND","terms":["Fall","Spring"],"prereqs":[],"subject":"WRTG","credits":2}
,{"_id": "WRTG 105B","subid":[],"name":"REASONING &AMP; WRITING IN THE COLLEGE: SECOND PART OF THE WRTG 105A-WRTG 105B SEQUENCE","terms":["Fall"],"prereqs":[],"subject":"WRTG","credits":2}
,{"_id": "WRTG 105E","subid":[],"name":"DISEASE &AMP; SOCIETY","terms":["Fall","Spring"],"prereqs":[],"subject":"WRTG","credits":4}
,{"_id": "WRTG 108","subid":[],"name":"WORKSHOP IN WRITING","terms":["Fall","Spring"],"prereqs":[],"subject":"WRTG","credits":2}
,{"_id": "WRTG 245","subid":["ENGL 285"],"name":"ADVANCED WRITING &AMP; PEER TUTORING","terms":["Fall"],"prereqs":[],"subject":"WRTG","credits":4}
,{"_id": "WRTG 253","subid":["BCSC 163"],"name":"COGNITION &AMP; WRITING","terms":["Fall"],"prereqs":[],"subject":"WRTG","credits":4}
,{"_id": "WRTG 260","subid":["DMST 260"],"name":"WRITING ACROSS TECHNOLOGIES","terms":["Fall"],"prereqs":[],"subject":"WRTG","credits":4}
,{"_id": "WRTG 266","subid":["GSWS 276"],"name":"WORDS HAVE POWER: WRITING FOR SOCIAL CHANGE","terms":["Fall"],"prereqs":[],"subject":"WRTG","credits":4}
,{"_id": "WRTG 269","subid":["CLTR 287","CLTR 487","ENGL 287","ENGL 487","LTST 200","LTST 400"],"name":"STUDIES IN TRANSLATION","terms":["Fall"],"prereqs":[],"subject":"WRTG","credits":4}
,{"_id": "WRTG 272","subid":["BIOL 272W"],"name":"COMMUNICATING YOUR PROFESSIONAL IDENTITY - BIOLOGY AND PUBLIC HEALTH","terms":["Fall","Spring"],"prereqs":[],"subject":"WRTG","credits":2}
,{"_id": "WRTG 273","subid":[],"name":"COMMUNICATING YOUR PROFESSIONAL IDENTITY - ENGINEERING","terms":["Fall","Summer"],"prereqs":[],"subject":"WRTG","credits":2}
,{"_id": "WRTG 274","subid":["PSYC 274W"],"name":"COMMUNICATING YOUR PROFESSIONAL IDENTITY - PSYCHOLOGY","terms":["Fall","Spring"],"prereqs":[],"subject":"WRTG","credits":2}
,{"_id": "WRTG 275","subid":[],"name":"COMMUNICATING YOUR PROFESSIONAL IDENTITY - MATHEMATICS","terms":["Fall"],"prereqs":[],"subject":"WRTG","credits":2}
,{"_id": "WRTG 276","subid":["INTR 299","PSCI 299"],"name":"COMMUNICATING YOUR PROFESSIONAL IDENTITY - LAW, POLICY, AND SOCIAL GOOD","terms":["Fall"],"prereqs":[],"subject":"WRTG","credits":2}
,{"_id": "WRTG 571","subid":[],"name":"WRITING PEDAGOGY","terms":["Fall"],"prereqs":[],"subject":"WRTG","credits":5}
,{"_id": "WRTG 098","subid":[],"name":"SPEAKING AND LISTENING II","terms":["Spring"],"prereqs":["WRTG 098"],"subject":"WRTG","credits":0}
,{"_id": "WRTG 099","subid":[],"name":"RHETORIC, READING &AMP; WRITING","terms":["Spring"],"prereqs":["WRTG 099","WRTG 098"],"subject":"WRTG","credits":0}
,{"_id": "WRTG 102","subid":[],"name":"EAPP COMMUNICATION ACROSS CONTEXTS II","terms":["Spring"],"prereqs":["WRTG 101","WRTG 102","WRTG 104"],"subject":"WRTG","credits":2}
,{"_id": "WRTG 104","subid":[],"name":"EAPP RESEARCH, READING, AND WRITING","terms":["Spring"],"prereqs":["WRTG 104","WRTG 103"],"subject":"WRTG","credits":6}
,{"_id": "WRTG 247","subid":[],"name":"SPOKEN COMMUNICATION &AMP; PEER TUTORING","terms":["Spring"],"prereqs":[],"subject":"WRTG","credits":4}
,{"_id": "WRTG 252","subid":["ENGL 136"],"name":"PRINCIPLES &AMP; PRACTICES OF COPYEDITING","terms":["Spring"],"prereqs":[],"subject":"WRTG","credits":4}
,{"_id": "WRTG 261","subid":["DMST 250","ENGL 288"],"name":"WRITING IN A DIGITAL WORLD","terms":["Spring"],"prereqs":[],"subject":"WRTG","credits":4}
,{"_id": "WRTG 263","subid":["ENGL 289","LTST 263"],"name":"TRANSLATION: INTERPRETING &AMP; ADAPTING","terms":["Spring"],"prereqs":[],"subject":"WRTG","credits":4}
,{"_id": "WRTG 277","subid":[],"name":"COMMUNICATING YOUR PROFESSIONAL IDENTITY - CROSS-DISCIPLINARY","terms":["Spring"],"prereqs":[],"subject":"WRTG","credits":2}
,{"_id": "WRTG 572","subid":["ENGL 572"],"name":"PRACTICUM IN TEACHING OF WRITING","terms":["Spring"],"prereqs":[],"subject":"WRTG","credits":2}]
'''

driver = Driver()

json_import = json.loads(x)
print("JSON imported")

driver.addCourses(json_import)