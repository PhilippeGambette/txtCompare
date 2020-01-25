/*
    sankeyCompare, a script of txtCompare to compare the order of texts
    inside two books
    Copyright (C) 2020, Philippe Gambette

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
*/
    
$(document).ready(function(){   

    var couleurTitresIdentiques = "#CCCCCC99";
    var couleurTitresDifferents = "#99999999";
    
    $(document).on("click",".lien",function(){
       // Changement de couleur du lien au clic
       if($(this).attr("fill")==couleurTitresDifferents){
           $(this).attr("fill",couleurTitresIdentiques);
       } else {
           $(this).attr("fill",couleurTitresDifferents);
       }
       $(".svg").html($(".svg").html());
    })

function loadSankeyCompare(){
    var data = [
   { 
   titreLong : 'nouvelles de <i>L’Heptaméron</i> de Marguerite de Navarre, dans les éditions <a href="https://gallica.bnf.fr/ark:/12148/bpt6k1519008r">par Pierre Boaistuau en 1558</a> et <a href="https://gallica.bnf.fr/ark:/12148/btv1b86171930">par Pierre Gruget en 1559</a>',
   titreCourt : 'nouvelles de <i>L’Heptaméron</i>',
   ecart : 11,
   pixelsParPage : 3,
   sourceData : "https://docs.google.com/spreadsheets/d/11dMJLEs1Bo_C0Wfsgrz3a_Yw6H0Ow-4pRI2dxGiAXbM/edit?usp=sharing",
   texts : [
["identifiant","recueil","partie","texte","nb-pages","lien","url"],
["Boaistuau-01","Boaistuau (1558)","1","De l’incontinence d’une Duchesse de Bourgongne…","19","","https://gallica.bnf.fr/ark:/12148/bpt6k1519008r/f45"],
["Boaistuau-02","Boaistuau (1558)","1","D’une dame d’Alemaigne…","4","","https://gallica.bnf.fr/ark:/12148/bpt6k1519008r/f64"],
["Boaistuau-03","Boaistuau (1558)","1","D’un Roy de Naples…","6","","https://gallica.bnf.fr/ark:/12148/bpt6k1519008r/f68"],
["Boaistuau-04","Boaistuau (1558)","1","D’une princesse de Flandres…","6","","https://gallica.bnf.fr/ark:/12148/bpt6k1519008r/f74"],
["Boaistuau-05","Boaistuau (1558)","1","D’une bastelliere…","3","","https://gallica.bnf.fr/ark:/12148/bpt6k1519008r/f80"],
["Boaistuau-06","Boaistuau (1558)","1","Du seigneur de Bonnivet…","7","","https://gallica.bnf.fr/ark:/12148/bpt6k1519008r/f83"],
["Boaistuau-07","Boaistuau (1558)","1","D’un gentilhomme…","12","","https://gallica.bnf.fr/ark:/12148/bpt6k1519008r/f90"],
["Boaistuau-08","Boaistuau (1558)","1","D’une veuve Millannoise…","4","","https://gallica.bnf.fr/ark:/12148/bpt6k1519008r/f102"],
["Boaistuau-09","Boaistuau (1558)","1","De la façon dont usa le Roy François…","4","","https://gallica.bnf.fr/ark:/12148/bpt6k1519008r/f106"],
["Boaistuau-10","Boaistuau (1558)","1","De l’amour d’une dame et d’un escollier…","5","","https://gallica.bnf.fr/ark:/12148/bpt6k1519008r/f110"],
["Boaistuau-11","Boaistuau (1558)","1","De l’amour d’une damoiselle nommée Pauline…","10","","https://gallica.bnf.fr/ark:/12148/bpt6k1519008r/f115"],
["Boaistuau-12","Boaistuau (1558)","1","D’un gentilhomme François…","4","","https://gallica.bnf.fr/ark:/12148/bpt6k1519008r/f125"],
["Boaistuau-13","Boaistuau (1558)","1","De l’honneste amitié d’une dame…","17","","https://gallica.bnf.fr/ark:/12148/bpt6k1519008r/f129"],
["Boaistuau-14","Boaistuau (1558)","1","De l’hypocrisie d’un prieur…","10","","https://gallica.bnf.fr/ark:/12148/bpt6k1519008r/f146"],
["Boaistuau-15","Boaistuau (1558)","1","Du grand scandalle qui survint à la maison…","7","","https://gallica.bnf.fr/ark:/12148/bpt6k1519008r/f156"],
["Boaistuau-16","Boaistuau (1558)","1","De l’artifice dont usa un gentilhomme…","8","","https://gallica.bnf.fr/ark:/12148/bpt6k1519008r/f163"],
["Boaistuau-17","Boaistuau (1558)","1","De la piteuse mort d’un gentilhomme…","6","","https://gallica.bnf.fr/ark:/12148/bpt6k1519008r/f171"],
["Boaistuau-18","Boaistuau (1558)","1","Des amours de Florinde, & d’Amadour…","29","","https://gallica.bnf.fr/ark:/12148/bpt6k1519008r/f177"],
["Boaistuau-19","Boaistuau (1558)","1","Histoire dixneuvfiesme","2","","https://gallica.bnf.fr/ark:/12148/bpt6k1519008r/f206"],
["Boaistuau-20","Boaistuau (1558)","1","De l’habomination d’un prestre incestueux…","3","","https://gallica.bnf.fr/ark:/12148/bpt6k1519008r/f208"],
["Boaistuau-21","Boaistuau (1558)","1","De deux freres mineurs…","4","","https://gallica.bnf.fr/ark:/12148/bpt6k1519008r/f211"],
["Boaistuau-22","Boaistuau (1558)","1","De la loüable industrie d’un sage mary…","6","","https://gallica.bnf.fr/ark:/12148/bpt6k1519008r/f215"],
["Boaistuau-23","Boaistuau (1558)","1","D’un president de Grenoble…","4","","https://gallica.bnf.fr/ark:/12148/bpt6k1519008r/f221"],
["Boaistuau-24","Boaistuau (1558)","1","De l’extreme charité d’une bourgeoise de Tours…","2","","https://gallica.bnf.fr/ark:/12148/bpt6k1519008r/f225"],
["Boaistuau-25","Boaistuau (1558)","1","D’un grand seigneur de France…","2","","https://gallica.bnf.fr/ark:/12148/bpt6k1519008r/f227"],
["Boaistuau-26","Boaistuau (1558)","1","Malice extreme d’un predicateur…","4","","https://gallica.bnf.fr/ark:/12148/bpt6k1519008r/f229"],
["Boaistuau-27","Boaistuau (1558)","1","De la merveilleuse continence d’une damoiselle…","9","","https://gallica.bnf.fr/ark:/12148/bpt6k1519008r/f233"],
["Boaistuau-28","Boaistuau (1558)","1","De la ruse d’une dame courtisanne…","5","","https://gallica.bnf.fr/ark:/12148/bpt6k1519008r/f242"],
["Boaistuau-29","Boaistuau (1558)","1","Du tapissier qui donna les innocens…","4","","https://gallica.bnf.fr/ark:/12148/bpt6k1519008r/f247"],
["Boaistuau-30","Boaistuau (1558)","1","D’une Contesse estrangere…","5","","https://gallica.bnf.fr/ark:/12148/bpt6k1519008r/f251"],
["Boaistuau-31","Boaistuau (1558)","1","Finesse d’une Espagnolle…","3","","https://gallica.bnf.fr/ark:/12148/bpt6k1519008r/f256"],
["Boaistuau-32","Boaistuau (1558)","1","D’un cordelier d’Italie…","5","","https://gallica.bnf.fr/ark:/12148/bpt6k1519008r/f259"],
["Boaistuau-33","Boaistuau (1558)","1","D’un mylhort d’Angleterre…","3","","https://gallica.bnf.fr/ark:/12148/bpt6k1519008r/f264"],
["Boaistuau-34","Boaistuau (1558)","1","D’une femme d’Autun…","6","","https://gallica.bnf.fr/ark:/12148/bpt6k1519008r/f267"],
["Boaistuau-35","Boaistuau (1558)","1","De l’amour d’un Curé et d’une femme de village…","2","","https://gallica.bnf.fr/ark:/12148/bpt6k1519008r/f273"],
["Boaistuau-36","Boaistuau (1558)","1","De la grande simplicité d’une bonne vieille…","1","","https://gallica.bnf.fr/ark:/12148/bpt6k1519008r/f275"],
["Boaistuau-37","Boaistuau (1558)","1","De la femme d’un procureur nommé sainct Aignan…","7","","https://gallica.bnf.fr/ark:/12148/bpt6k1519008r/f276"],
["Boaistuau-38","Boaistuau (1558)","1","De la femme d’un muletier…","3","","https://gallica.bnf.fr/ark:/12148/bpt6k1519008r/f283"],
["Boaistuau-39","Boaistuau (1558)","1","Artifice merveilleux qu’une femme inventa…","2","","https://gallica.bnf.fr/ark:/12148/bpt6k1519008r/f286"],
["Boaistuau-40","Boaistuau (1558)","1","D’un marchant de Paris…","2","","https://gallica.bnf.fr/ark:/12148/bpt6k1519008r/f288"],
["Boaistuau-41","Boaistuau (1558)","1","D’un quidam…","6","","https://gallica.bnf.fr/ark:/12148/bpt6k1519008r/f290"],
["Boaistuau-42","Boaistuau (1558)","1","De l’incontinence d’un Duc…","7","","https://gallica.bnf.fr/ark:/12148/bpt6k1519008r/f296"],
["Boaistuau-43","Boaistuau (1558)","1","D’une dame qui ayant receu un anneau…","13","","https://gallica.bnf.fr/ark:/12148/bpt6k1519008r/f303"],
["Boaistuau-44","Boaistuau (1558)","1","De la temerité d’un sot secretaire…","2","","https://gallica.bnf.fr/ark:/12148/bpt6k1519008r/f316"],
["Boaistuau-45","Boaistuau (1558)","1","Encore d’un secretaire…","4","","https://gallica.bnf.fr/ark:/12148/bpt6k1519008r/f318"],
["Boaistuau-46","Boaistuau (1558)","1","De la cruauté d’un cordelier flamment…","3","","https://gallica.bnf.fr/ark:/12148/bpt6k1519008r/f322"],
["Boaistuau-47","Boaistuau (1558)","1","De la prudence d’une femme…","3","","https://gallica.bnf.fr/ark:/12148/bpt6k1519008r/f325"],
["Boaistuau-48","Boaistuau (1558)","1","D’un Conte qui tua un gentilhomme…","7","","https://gallica.bnf.fr/ark:/12148/bpt6k1519008r/f328"],
["Boaistuau-49","Boaistuau (1558)","1","De la merveilleuse amitié de deux gentilzhommes…","3","","https://gallica.bnf.fr/ark:/12148/bpt6k1519008r/f335"],
["Boaistuau-50","Boaistuau (1558)","1","De deux cordeliers de perigort…","3","","https://gallica.bnf.fr/ark:/12148/bpt6k1519008r/f338"],
["Boaistuau-51","Boaistuau (1558)","1","D’un aymant…","2","","https://gallica.bnf.fr/ark:/12148/bpt6k1519008r/f341"],
["Boaistuau-52","Boaistuau (1558)","1","De la subtilité d’une dame…","3","","https://gallica.bnf.fr/ark:/12148/bpt6k1519008r/f343"],
["Boaistuau-53","Boaistuau (1558)","1","De l’amour d’un chantre…","4","","https://gallica.bnf.fr/ark:/12148/bpt6k1519008r/f346"],
["Boaistuau-54","Boaistuau (1558)","1","D’une damoiselle…","2","","https://gallica.bnf.fr/ark:/12148/bpt6k1519008r/f350"],
["Boaistuau-55","Boaistuau (1558)","1","De certain gentilhomme de Valence…","5","","https://gallica.bnf.fr/ark:/12148/bpt6k1519008r/f352"],
["Boaistuau-56","Boaistuau (1558)","1","Merveilleuse austerité de la vie d’un homme…","3","","https://gallica.bnf.fr/ark:/12148/bpt6k1519008r/f357"],
["Boaistuau-57","Boaistuau (1558)","1","De la femme d’un apoticaire…","3","","https://gallica.bnf.fr/ark:/12148/bpt6k1519008r/f360"],
["Boaistuau-58","Boaistuau (1558)","1","De la prudence d’une femme à surprendre son mary…","2","","https://gallica.bnf.fr/ark:/12148/bpt6k1519008r/f363"],
["Boaistuau-59","Boaistuau (1558)","1","D’une femme presque morte…","2","","https://gallica.bnf.fr/ark:/12148/bpt6k1519008r/f365"],
["Boaistuau-60","Boaistuau (1558)","1","Comme une damoiselle donna assignation…","3","","https://gallica.bnf.fr/ark:/12148/bpt6k1519008r/f367"],
["Boaistuau-61","Boaistuau (1558)","1","Comme une damoiselle trompa son mary…","5","","https://gallica.bnf.fr/ark:/12148/bpt6k1519008r/f370"],
["Boaistuau-62","Boaistuau (1558)","1","De la cruauté d’un Italien…","6","","https://gallica.bnf.fr/ark:/12148/bpt6k1519008r/f375"],
["Boaistuau-63","Boaistuau (1558)","1","Comme un serviteur d’apoticaire…","1","","https://gallica.bnf.fr/ark:/12148/bpt6k1519008r/f381"],
["Boaistuau-64","Boaistuau (1558)","1","De l’astuce d’un prince…","6","","https://gallica.bnf.fr/ark:/12148/bpt6k1519008r/f382"],
["Boaistuau-65","Boaistuau (1558)","1","Du subtil moyen dont usoit un grand seigneur…","4","","https://gallica.bnf.fr/ark:/12148/bpt6k1519008r/f388"],
["Boaistuau-66","Boaistuau (1558)","1","Plaisant discours d’un autre grand seigneur…","13","","https://gallica.bnf.fr/ark:/12148/bpt6k1519008r/f392"],
["Boaistuau-67","Boaistuau (1558)","1","D’une femme que son filz engrossa…","6","","https://gallica.bnf.fr/ark:/12148/bpt6k1519008r/f405"],
["Gruget01","Gruget (1559)","1re journée","Une femme d’Alençon…","7","Boaistuau-37","https://gallica.bnf.fr/ark:/12148/btv1b86171930/f31"],
["Gruget02","Gruget (1559)","1re journée","Piteuse & chaste mort de la femme…","3","Boaistuau-38","https://gallica.bnf.fr/ark:/12148/btv1b86171930/f38"],
["Gruget03","Gruget (1559)","1re journée","Un roy de Naples…","6","Boaistuau-03","https://gallica.bnf.fr/ark:/12148/btv1b86171930/f41"],
["Gruget04","Gruget (1559)","1re journée","Temeraire entreprinse d’un gentil-homme…","6","Boaistuau-04","https://gallica.bnf.fr/ark:/12148/btv1b86171930/f47"],
["Gruget05","Gruget (1559)","1re journée","Une basteliere s’eschappa de deux cordeliers…","4","Boaistuau-05","https://gallica.bnf.fr/ark:/12148/btv1b86171930/f53"],
["Gruget06","Gruget (1559)","1re journée","Subtilité d’une femme…","2","Boaistuau-39","https://gallica.bnf.fr/ark:/12148/btv1b86171930/f57"],
["Gruget07","Gruget (1559)","1re journée","Un marchant de Paris trompe la mere de s’amie…","2","Boaistuau-40","https://gallica.bnf.fr/ark:/12148/btv1b86171930/f59"],
["Gruget08","Gruget (1559)","1re journée","Un quidam…","6","Boaistuau-41","https://gallica.bnf.fr/ark:/12148/btv1b86171930/f61"],
["Gruget09","Gruget (1559)","1re journée","Piteuse mort d’un gentil-homme amoureux…","5","Boaistuau-17","https://gallica.bnf.fr/ark:/12148/btv1b86171930/f67"],
["Gruget10","Gruget (1559)","1re journée","Amours d’Amadour & Florinde…","30","Boaistuau-18","https://gallica.bnf.fr/ark:/12148/btv1b86171930/f72"],
["Gruget11","Gruget (1559)","2e journée","Propos facetieux d’un cordelier…","3","","https://gallica.bnf.fr/ark:/12148/btv1b86171930/f103"],
["Gruget12","Gruget (1559)","2e journée","L’incontinence d’un Duc…","7","Boaistuau-42","https://gallica.bnf.fr/ark:/12148/btv1b86171930/f106"],
["Gruget13","Gruget (1559)","2e journée","Un capitaine de galeres…","13","Boaistuau-43","https://gallica.bnf.fr/ark:/12148/btv1b86171930/f113"],
["Gruget14","Gruget (1559)","2e journée","Subtilité d’un amoureux…","6","Boaistuau-06","https://gallica.bnf.fr/ark:/12148/btv1b86171930/f126"],
["Gruget15","Gruget (1559)","2e journée","Une dame de la court du Roy…","12","Boaistuau-07","https://gallica.bnf.fr/ark:/12148/btv1b86171930/f132"],
["Gruget16","Gruget (1559)","2e journée","Une dame Millannoise…","5","Boaistuau-08","https://gallica.bnf.fr/ark:/12148/btv1b86171930/f144"],
["Gruget17","Gruget (1559)","2e journée","Le Roy François monstra sa generosité…","4","Boaistuau-09","https://gallica.bnf.fr/ark:/12148/btv1b86171930/f149"],
["Gruget18","Gruget (1559)","2e journée","Une belle jeune dame experimente la foy d’un jeune…","5","Boaistuau-10","https://gallica.bnf.fr/ark:/12148/btv1b86171930/f153"],
["Gruget19","Gruget (1559)","2e journée","De deux amans…","11","Boaistuau-11","https://gallica.bnf.fr/ark:/12148/btv1b86171930/f158"],
["Gruget20","Gruget (1559)","2e journée","Un gentil-homme est inopinément guary du mal…","6","Boaistuau-12","https://gallica.bnf.fr/ark:/12148/btv1b86171930/f169"],
["Gruget21","Gruget (1559)","3e journée","L’Honneste & merveilleuse amitié d’une fille…","15","Boaistuau-13","https://gallica.bnf.fr/ark:/12148/btv1b86171930/f176"],
["Gruget22","Gruget (1559)","3e journée","Un prieur reformateur…","10","Boaistuau-14","https://gallica.bnf.fr/ark:/12148/btv1b86171930/f191"],
["Gruget23","Gruget (1559)","3e journée","Trois meurtres advenuz en une maison…","7","Boaistuau-15","https://gallica.bnf.fr/ark:/12148/btv1b86171930/f201"],
["Gruget24","Gruget (1559)","3e journée","Gentile invention d’un gentil-homme…","9","Boaistuau-16","https://gallica.bnf.fr/ark:/12148/btv1b86171930/f208"],
["Gruget25","Gruget (1559)","3e journée","Subtil moyen, dont usoit un grand prince…","5","Boaistuau-65","https://gallica.bnf.fr/ark:/12148/btv1b86171930/f217"],
["Gruget26","Gruget (1559)","3e journée","Plaisant discours d’un grand seigneur…","13","Boaistuau-66","https://gallica.bnf.fr/ark:/12148/btv1b86171930/f222"],
["Gruget27","Gruget (1559)","3e journée","Temerité d’un sot secrettaire…","2","Boaistuau-44","https://gallica.bnf.fr/ark:/12148/btv1b86171930/f235"],
["Gruget28","Gruget (1559)","3e journée","Un secrettaire pensait affiner quelqu’un qui l’affina…","2","Boaistuau-45","https://gallica.bnf.fr/ark:/12148/btv1b86171930/f237"],
["Gruget29","Gruget (1559)","3e journée","Un bon Jannin de village…","3","Boaistuau-35","https://gallica.bnf.fr/ark:/12148/btv1b86171930/f239"],
["Gruget30","Gruget (1559)","3e journée","Merveilleuse exemple de la fragilité humaine…","6","Boaistuau-67","https://gallica.bnf.fr/ark:/12148/btv1b86171930/f242"],
["Gruget31","Gruget (1559)","4e journée","Exécrable cruauté d’un cordelier…","5","Boaistuau-46","https://gallica.bnf.fr/ark:/12148/btv1b86171930/f249"],
["Gruget32","Gruget (1559)","4e journée","Punition plus rigoureuse que la mort…","5","Boaistuau-02","https://gallica.bnf.fr/ark:/12148/btv1b86171930/f254"],
["Gruget33","Gruget (1559)","4e journée","Abomination d’un prestre incestueux…","3","Boaistuau-20","https://gallica.bnf.fr/ark:/12148/btv1b86171930/f259"],
["Gruget34","Gruget (1559)","4e journée","Deux cordeliers trop curieux d’escouter…","4","Boaistuau-21","https://gallica.bnf.fr/ark:/12148/btv1b86171930/f262"],
["Gruget35","Gruget (1559)","4e journée","Industrie d’un sage mary…","6","Boaistuau-22","https://gallica.bnf.fr/ark:/12148/btv1b86171930/f266"],
["Gruget36","Gruget (1559)","4e journée","Un président de Grenoble…","5","Boaistuau-23","https://gallica.bnf.fr/ark:/12148/btv1b86171930/f272"],
["Gruget37","Gruget (1559)","4e journée","Prudence d’une femme…","3","Boaistuau-47","https://gallica.bnf.fr/ark:/12148/btv1b86171930/f277"],
["Gruget38","Gruget (1559)","4e journée","Memorable charité d’une femme de Tours…","3","Boaistuau-24","https://gallica.bnf.fr/ark:/12148/btv1b86171930/f280"],
["Gruget39","Gruget (1559)","4e journée","Bonne invention pour chasser le Lutin…","2","Boaistuau-25","https://gallica.bnf.fr/ark:/12148/btv1b86171930/f283"],
["Gruget40","Gruget (1559)","4e journée","Un seigneur fait mourir son beau-frere…","7","Boaistuau-48","https://gallica.bnf.fr/ark:/12148/btv1b86171930/f285"],
["Gruget41","Gruget (1559)","5e journée","Estrange & nouvelle penitence…","3","Boaistuau-26","https://gallica.bnf.fr/ark:/12148/btv1b86171930/f293"],
["Gruget42","Gruget (1559)","5e journée","Continence d’une jeune fille…","10","Boaistuau-27","https://gallica.bnf.fr/ark:/12148/btv1b86171930/f296"],
["Gruget43","Gruget (1559)","5e journée","L’hypocrisie d’une dame de court…","5","Boaistuau-28","https://gallica.bnf.fr/ark:/12148/btv1b86171930/f306"],
["Gruget44","Gruget (1559)","5e journée","De deux amans, qui ont subtilement jouy…","7","","https://gallica.bnf.fr/ark:/12148/btv1b86171930/f311"],
["Gruget45","Gruget (1559)","5e journée","Un mary baillant les innocens à sa chambriere…","4","Boaistuau-29","https://gallica.bnf.fr/ark:/12148/btv1b86171930/f318"],
["Gruget46","Gruget (1559)","5e journée","D’un cordelier…","3","","https://gallica.bnf.fr/ark:/12148/btv1b86171930/f322"],
["Gruget47","Gruget (1559)","5e journée","Un gentil-homme du Perche…","3","Boaistuau-49","https://gallica.bnf.fr/ark:/12148/btv1b86171930/f325"],
["Gruget48","Gruget (1559)","5e journée","Deux cordeliers une premiere nuict de nopces…","3","Boaistuau-50","https://gallica.bnf.fr/ark:/12148/btv1b86171930/f328"],
["Gruget49","Gruget (1559)","5e journée","Subtilité d’une Comtesse…","5","Boaistuau-30","https://gallica.bnf.fr/ark:/12148/btv1b86171930/f331"],
["Gruget50","Gruget (1559)","5e journée","Un amoureux, apres la saignée…","6","Boaistuau-51","https://gallica.bnf.fr/ark:/12148/btv1b86171930/f336"],
["Gruget51","Gruget (1559)","6e journée","Perfidie & cruauté d’un Duc italien…","2","Boaistuau-62","https://gallica.bnf.fr/ark:/12148/btv1b86171930/f343"],
["Gruget52","Gruget (1559)","6e journée","Du sale desjeuner preparé par un varlet d’apoticaire…","3","Boaistuau-63","https://gallica.bnf.fr/ark:/12148/btv1b86171930/f345"],
["Gruget53","Gruget (1559)","6e journée","Diligence personelle d’un prince…","6","Boaistuau-64","https://gallica.bnf.fr/ark:/12148/btv1b86171930/f348"],
["Gruget54","Gruget (1559)","6e journée","D’une damoiselle de si bonne nature…","3","Boaistuau-52","https://gallica.bnf.fr/ark:/12148/btv1b86171930/f354"],
["Gruget55","Gruget (1559)","6e journée","Finesse d’une Espaignole…","2","Boaistuau-31","https://gallica.bnf.fr/ark:/12148/btv1b86171930/f357"],
["Gruget56","Gruget (1559)","6e journée","Un cordelier marie frauduleusement un autre…","5","Boaistuau-32","https://gallica.bnf.fr/ark:/12148/btv1b86171930/f359"],
["Gruget57","Gruget (1559)","6e journée","Compte ridicule d’un Milhort d’Angleterre…","4","Boaistuau-33","https://gallica.bnf.fr/ark:/12148/btv1b86171930/f364"],
["Gruget58","Gruget (1559)","6e journée","Une dame de court se venge plaisamment…","3","Boaistuau-60","https://gallica.bnf.fr/ark:/12148/btv1b86171930/f368"],
["Gruget59","Gruget (1559)","6e journée","Un gentil-homme pensant acoler en secret…","5","Boaistuau-61","https://gallica.bnf.fr/ark:/12148/btv1b86171930/f371"],
["Gruget60","Gruget (1559)","6e journée","Une Parisienne abandonne son mary…","5","Boaistuau-53","https://gallica.bnf.fr/ark:/12148/btv1b86171930/f376"],
["Gruget61","Gruget (1559)","7e journée","Merveilleuse pertinacité d’amour effrontée…","6","Boaistuau-34","https://gallica.bnf.fr/ark:/12148/btv1b86171930/f382"],
["Gruget62","Gruget (1559)","7e journée","Une damoiselle, faisant un compte de l’amour…","3","Boaistuau-54","https://gallica.bnf.fr/ark:/12148/btv1b86171930/f388"],
["Gruget63","Gruget (1559)","7e journée","Notable chasteté d’un seigneur François…","3","","https://gallica.bnf.fr/ark:/12148/btv1b86171930/f391"],
["Gruget64","Gruget (1559)","7e journée","Un gentil-homme desdaigné pour mary…","5","Boaistuau-55","https://gallica.bnf.fr/ark:/12148/btv1b86171930/f394"],
["Gruget65","Gruget (1559)","7e journée","Simplicité d’une vieille…","2","Boaistuau-36","https://gallica.bnf.fr/ark:/12148/btv1b86171930/f399"],
["Gruget66","Gruget (1559)","7e journée","Compte risible advenu au Roy & Royne de Navarre…","2","","https://gallica.bnf.fr/ark:/12148/btv1b86171930/f401"],
["Gruget67","Gruget (1559)","7e journée","Extreme amour & austerité de femme…","3","Boaistuau-56","https://gallica.bnf.fr/ark:/12148/btv1b86171930/f403"],
["Gruget68","Gruget (1559)","7e journée","Une femme faict manger des cantarides à son mary…","3","Boaistuau-57","https://gallica.bnf.fr/ark:/12148/btv1b86171930/f406"],
["Gruget69","Gruget (1559)","7e journée","Un Italien se laisse affiner par sa chambriere…","2","Boaistuau-58","https://gallica.bnf.fr/ark:/12148/btv1b86171930/f409"],
["Gruget70","Gruget (1559)","7e journée","L’incontinence furieuse d’une Duchesse…","20","Boaistuau-01","https://gallica.bnf.fr/ark:/12148/btv1b86171930/f411"],
["Gruget71","Gruget (1559)","8e journée","Une femme estant aux aboiz de la mort…","2","Boaistuau-59","https://gallica.bnf.fr/ark:/12148/btv1b86171930/f432"],
["Gruget72","Gruget (1559)","8e journée","Continuelle repentance d’une religieuse…","5","","https://gallica.bnf.fr/ark:/12148/btv1b86171930/f434"],
    ]
   },
   { 
   titreLong : '<i>Conversations d’Émilie</i> de Louise d’Épinay, dans les éditions <a href="https://books.google.fr/books?id=olZ9vgAACAAJ&hl=fr&pg=PR1#v=onepage&q&f=false">de 1774</a> et <a href="https://fr.wikisource.org/wiki/Les_Conversations_d%E2%80%99%C3%89milie">de 1781</a>',
   titreCourt : '<i>Conversations d’Émilie</i>',
   ecart : 13,
   pixelsParPage : 0.5,
   sourceData : "https://docs.google.com/spreadsheets/d/1wqyxRS_6LTE5gAPa8qxydS2dHLSUxTUYJ43467Rn6pM/edit?usp=sharing",
   texts : [
["identifiant","recueil","partie","texte","nb-pages","lien","url"],
["1774-01","Les Conversations d'Émilie (1774)","2","Lettre de l’auteur à l’éditeur","4","","https://books.google.fr/books?id=olZ9vgAACAAJ&hl=fr&pg=PR3#v=onepage&q&f=false"],
["1774-02","Les Conversations d'Émilie (1774)","3","Première conversation","26","","https://books.google.fr/books?id=olZ9vgAACAAJ&hl=fr&pg=PA1#v=onepage&q&f=false"],
["1774-03","Les Conversations d'Émilie (1774)","3","Deuxième conversation","16","","https://books.google.fr/books?id=olZ9vgAACAAJ&hl=fr&pg=PA27#v=onepage&q&f=false"],
["1774-04","Les Conversations d'Émilie (1774)","3","Troisième conversation","24","","https://books.google.fr/books?id=olZ9vgAACAAJ&hl=fr&pg=PA43#v=onepage&q&f=false"],
["1774-05","Les Conversations d'Émilie (1774)","3","Quatrième conversation","30","","https://books.google.fr/books?id=olZ9vgAACAAJ&hl=fr&pg=PA67#v=onepage&q&f=false"],
["1774-06","Les Conversations d'Émilie (1774)","3","Cinquième conversation","42","","https://books.google.fr/books?id=olZ9vgAACAAJ&hl=fr&pg=PA97#v=onepage&q&f=false"],
["1774-07","Les Conversations d'Émilie (1774)","3","Sixième conversation","33","","https://books.google.fr/books?id=olZ9vgAACAAJ&hl=fr&pg=PA139#v=onepage&q&f=false"],
["1774-08","Les Conversations d'Émilie (1774)","3","Septième conversation","29","","https://books.google.fr/books?id=olZ9vgAACAAJ&hl=fr&pg=PA172#v=onepage&q&f=false"],
["1774-09","Les Conversations d'Émilie (1774)","3","Huitième conversation","41","","https://books.google.fr/books?id=olZ9vgAACAAJ&hl=fr&pg=PA201#v=onepage&q&f=false"],
["1774-10","Les Conversations d'Émilie (1774)","3","Neuvième conversation","50","","https://books.google.fr/books?id=olZ9vgAACAAJ&hl=fr&pg=PA242#v=onepage&q&f=false"],
["1774-11","Les Conversations d'Émilie (1774)","3","Dixième conversation","31","","https://books.google.fr/books?id=olZ9vgAACAAJ&hl=fr&pg=PA292#v=onepage&q&f=false"],
["1774-12","Les Conversations d'Émilie (1774)","3","Onzième conversation","86","","https://books.google.fr/books?id=olZ9vgAACAAJ&hl=fr&pg=PA323#v=onepage&q&f=false"],
["1774-13","Les Conversations d'Émilie (1774)","3","Douzième conversation","22","","https://books.google.fr/books?id=olZ9vgAACAAJ&hl=fr&pg=PA409#v=onepage&q&f=false"],
["1781-01","Les Conversations d'Émilie (1781)","1","Avertissement sur cette seconde édition","10","","https://fr.wikisource.org/wiki/Les_Conversations_d%E2%80%99%C3%89milie/Avertissement"],
["1781-02","Les Conversations d'Émilie (1781)","2","Lettre de l’auteur à l’éditeur","2","1774-01","https://fr.wikisource.org/wiki/Les_Conversations_d%E2%80%99%C3%89milie/Lettre_de_l%E2%80%99auteur_%C3%A0_l%E2%80%99%C3%A9diteur"],
["1781-03","Les Conversations d'Émilie (1781)","3","Première conversation","26","1774-02","https://fr.wikisource.org/wiki/Les_Conversations_d%E2%80%99%C3%89milie/01"],
["1781-04","Les Conversations d'Émilie (1781)","3","Deuxième conversation","15","1774-03","https://fr.wikisource.org/wiki/Les_Conversations_d%E2%80%99%C3%89milie/02"],
["1781-05","Les Conversations d'Émilie (1781)","3","Troisième conversation","23","1774-04","https://fr.wikisource.org/wiki/Les_Conversations_d%E2%80%99%C3%89milie/03"],
["1781-06","Les Conversations d'Émilie (1781)","3","Quatrième conversation","31","1774-05","https://fr.wikisource.org/wiki/Les_Conversations_d%E2%80%99%C3%89milie/04"],
["1781-07","Les Conversations d'Émilie (1781)","3","Cinquième conversation","34","","https://fr.wikisource.org/wiki/Les_Conversations_d%E2%80%99%C3%89milie/05"],
["1781-08","Les Conversations d'Émilie (1781)","3","Sixième conversation","47","1774-06","https://fr.wikisource.org/wiki/Les_Conversations_d%E2%80%99%C3%89milie/06"],
["1781-09","Les Conversations d'Émilie (1781)","3","Septième conversation","41","1774-07","https://fr.wikisource.org/wiki/Les_Conversations_d%E2%80%99%C3%89milie/07"],
["1781-10","Les Conversations d'Émilie (1781)","3","Huitième conversation","37","1774-08","https://fr.wikisource.org/wiki/Les_Conversations_d%E2%80%99%C3%89milie/08"],
["1781-11","Les Conversations d'Émilie (1781)","3","Neuvième conversation","49","1774-09","https://fr.wikisource.org/wiki/Les_Conversations_d%E2%80%99%C3%89milie/09"],
["1781-12","Les Conversations d'Émilie (1781)","3","Dixième conversation","64","1774-11","https://fr.wikisource.org/wiki/Les_Conversations_d%E2%80%99%C3%89milie/10"],
["1781-13","Les Conversations d'Émilie (1781)","3","Onzième conversation","33","1774-10","https://fr.wikisource.org/wiki/Les_Conversations_d%E2%80%99%C3%89milie/11"],
["1781-14","Les Conversations d'Émilie (1781)","3","Douzième conversation","73","","https://fr.wikisource.org/wiki/Les_Conversations_d%E2%80%99%C3%89milie/12"],
["1781-15","Les Conversations d'Émilie (1781)","3","Treizième conversation","48","1774-12","https://fr.wikisource.org/wiki/Les_Conversations_d%E2%80%99%C3%89milie/13"],
["1781-16","Les Conversations d'Émilie (1781)","3","Quatorzième conversation","109","","https://fr.wikisource.org/wiki/Les_Conversations_d%E2%80%99%C3%89milie/14"],
["1781-17","Les Conversations d'Émilie (1781)","3","Quinzième conversation","59","","https://fr.wikisource.org/wiki/Les_Conversations_d%E2%80%99%C3%89milie/15"],
["1781-18","Les Conversations d'Émilie (1781)","3","Seizième conversation","40","","https://fr.wikisource.org/wiki/Les_Conversations_d%E2%80%99%C3%89milie/16"],
["1781-19","Les Conversations d'Émilie (1781)","3","Dix-septième conversation","50","","https://fr.wikisource.org/wiki/Les_Conversations_d%E2%80%99%C3%89milie/17"],
["1781-20","Les Conversations d'Émilie (1781)","3","Dix-huitième conversation","45","","https://fr.wikisource.org/wiki/Les_Conversations_d%E2%80%99%C3%89milie/18"],
["1781-21","Les Conversations d'Émilie (1781)","3","Dix-neuvième conversation","68","","https://fr.wikisource.org/wiki/Les_Conversations_d%E2%80%99%C3%89milie/19"],
["1781-22","Les Conversations d'Émilie (1781)","3","Vingtième conversation","51","","https://fr.wikisource.org/wiki/Les_Conversations_d%E2%80%99%C3%89milie/20"],
["1781-23","Les Conversations d'Émilie (1781)","4","Privilège du roi","4","","https://fr.wikisource.org/wiki/Les_Conversations_d%E2%80%99%C3%89milie/21"],
    ]
    }
]

    // Choix du corpus 
    var corpusNumber = $("select").val();
    $("#titreCourt").html(data[corpusNumber].titreCourt);
    $("#titreLong").html(data[corpusNumber].titreLong);
    $("#sourceData").attr("href",data[corpusNumber].sourceData);
    var texts = data[corpusNumber].texts;
    var ecart = data[corpusNumber].ecart;
    
    // Initialisation
    var xLeft = 380;
    var xRight = 620;
    var i = 1;
    var hauteurParDefaut = 16;
    var pixelsParPage = data[corpusNumber].pixelsParPage;
    $("#label").css("font-size",hauteurParDefaut+"px");
    var hauteurRecueils = [];
    var ordonneeTextes = {};
    var hauteurTextes = {};
    var titreTextes = {}
    var recueils = [];
    var couleurs = ["#DDDDDD","#55CCCC","#CC5555","#55CC55","#5555CC","#CC55CC","#55CCCC"];
    var numPartie = 0;
    var partie = "";
    var y = hauteurParDefaut+10;
    
    // Ajout des paramètres de style dans l'image SVG
    $(".svg").html('  <svg xmlns="http://www.w3.org/2000/svg" width="1000" height="300" version="1.1" xmlns:xlink="http://www.w3.org/1999/xlink"><style>.titre { font: italic '+(hauteurParDefaut+2)+'px Calibri; fill: grey;}</style>	<title>sankeyCompare</title><g font-family="Calibri"></g></svg>')
    
    // Parcours des données
    while(i < texts.length){
       if(recueils.length == 0){
          // Début de l'ajout du premier texte
          recueils.push(texts[i][1]);
          // Ajout du titre du premier texte
          $("#label").css("font-size",(hauteurParDefaut+2)+"px");
          $("#label").html(recueils[0]);
          $(".svg g").append('<text class="titre" x="'+(xLeft-parseInt($("#label").css("width"))-20)+'" y="'+(y)+'" font-size="'+(hauteurParDefaut+2)+'">'+recueils[0]+'</text>');
          $("#label").css("font-size",hauteurParDefaut+"px");
          y += 5;

       } else {
          if(texts[i][1] != recueils[recueils.length-1]){
             // Début de l'ajout du deuxième texte
             recueils.push(texts[i][1]);
             y = hauteurParDefaut+10;
             // Ajout du titre du deuxième texte
             $("#label").css("font-size",(hauteurParDefaut+2)+"px");
             $("#label").html(recueils[1]);
             $(".svg g").append('<text class="titre" x="'+(xRight+20)+'" y="'+(y)+'" fill="grey" font-size="'+(hauteurParDefaut+2)+'">'+recueils[1]+'</text>');
             $("#label").css("font-size",hauteurParDefaut+"px");
             partie = "";
             numPartie = 0;
             y += 5;
          }
       }
       
       // Calcul de la hauteur du prochain texte ajouté :
       var hauteurTexte = parseInt(texts[i][4])*pixelsParPage;
       y = y+hauteurTexte+ecart;
       
       // Mise à jour du numéro de partie du texte
       if(texts[i][2] != partie){
          partie = texts[i][2];
          numPartie = texts[i][2][0];
       } 
       hauteurRecueils[recueils.length-1] = y;
       ordonneeTextes["i"+texts[i][0]] = y;
       hauteurTextes["i"+texts[i][0]] = hauteurTexte;
       titreTextes["i"+texts[i][0]] = texts[i][3];
       var url = texts[i][6];
       
       if(texts[i][1] == recueils[0]){
          // Affichage du titre de l'extrait sur la gauche
          $("#label").html(texts[i][3]+"…");
          $(".svg g").append('		<path fill="'+couleurs[numPartie]+'" d="M'+(xLeft-10)+' '+y+' H '+(xLeft)+' V '+(y-hauteurTexte)+' H '+(xLeft-10)+' L '+(xLeft-10)+' '+y+'">');          
          // Ajout d'un lien vers l'extrait
          $(".svg g").append('    <a xlink:show="new" xlink:href="'+url+'" xlink:title="Accéder au texte…"><text x="'+(xLeft-parseInt($("#label").css("width"))-20)+'" y="'+(y)+'" fill="'+couleurs[numPartie]+'" font-size="'+hauteurParDefaut+'">'+texts[i][3]+'</text></a>');
       } else {
          // Affichage du titre de l'extrait sur la droite
          $(".svg g").append('		<path fill="'+couleurs[numPartie]+'" d="M'+(xRight+10)+' '+y+' H '+(xRight)+' V '+(y-hauteurTexte)+' H '+(xRight+10)+' L '+(xRight+10)+' '+y+'">');
          // Ajout d'un lien vers l'extrait
          $(".svg g").append('    <a xlink:show="new" xlink:href="'+url+'" xlink:title="Accéder au texte…"><text x="'+(xRight+20)+'" y="'+(y)+'" fill="'+couleurs[numPartie]+'" font-size="'+hauteurParDefaut+'">'+texts[i][3]+'</text></a>');       

          if(texts[i][5]!=""){
             // Ajout du lien entre l'extrait de droite et un extrait de gauche
             var y2 = ordonneeTextes["i"+texts[i][5]];
             var h2 = hauteurTextes["i"+texts[i][5]];
             var couleurLien = couleurTitresIdentiques;
             if (texts[i][3].toLowerCase() != titreTextes["i"+texts[i][5]].toLowerCase() ){
                // Lien plus foncé entre des titres différents
                couleurLien = couleurTitresDifferents;
             }
             $(".svg g").append('		<path class="lien" fill="'+couleurLien+'" d="M'+(xLeft)+','+y2+' C'+((xRight+xLeft)/2)+','+y2+' '+((xRight+xLeft)/2)+','+y+' '+(xRight)+','+y+' V '+(y-hauteurTexte)+' C'+((xRight+xLeft)/2)+','+(y-hauteurTexte)+' '+((xRight+xLeft)/2)+','+(y2-h2)+' '+(xLeft)+','+(y2-h2)+'"/>')
          }
       }
       i ++;
    }
    
    // Mise à jour de la hauteur de l'image SVG
    var hauteurMax = hauteurRecueils[0];    
    if(hauteurMax < hauteurRecueils[1]){
       hauteurMax = hauteurRecueils[1];
    }
    $("svg").attr("height",hauteurMax + hauteurParDefaut*3+2)
    
    // Mise à jour de l'image SVG
    $(".svg").html($(".svg").html());
    
}

loadSankeyCompare();

$("select").on("change",loadSankeyCompare);

})