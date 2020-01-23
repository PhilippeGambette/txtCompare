var textWords;
var textPunctuation;
var intervalNb;
var intervalLength;
var wordDict;
var numberOfBlocks;
var noTraceYet = true;

// Split the text into a list of punctuation sequences and a list of words
function wordsAndPunctuation(text){
    var punctuation = {"[":1,".":1,",":1,"/":1,"…":1,"#":1,"!":1,"$":1,"%":1,"^":1,"&":1,"*":1,";":1,":":1,"{":1,"}":1,"=":1,"\\":1,"-":1,"`":1,"~":1,"(":1,")":1,"’":1,"'":1,"]":1,"«":1,"»":1,"\"":1,"¤":1," ":1};
    //var punctuation = {" ":1};
    var currentWord = "";
    var currentPunctuation = "";
    var punctuationList = [];
    var wordList = [];
    var i=0;
    searchPunct = true;
    while(i<text.length){
       if(text[i] in punctuation){
          if(searchPunct){
             currentPunctuation += text[i];
          } else {
             wordList.push(currentWord);
             searchPunct = true;
             currentWord = "";
             currentPunctuation += text[i];
          }
       } else {
          if(searchPunct){
             punctuationList.push(currentPunctuation);
             searchPunct = false;
             currentPunctuation = "";
             currentWord += text[i];
          } else {
             currentWord += text[i];
          }       
       }
       i++;
    }
    punctuationList.push(currentPunctuation);
    wordList.push(currentWord);
    return [punctuationList,wordList];
}

// From a list of words, with repeats, build a dictionary which associate
// to each word, its number of occurrences.
function frequencies(list){
   var i = 0;
   var freq = {};
   while(i<list.length){
      if(list[i] in freq){
         freq[list[i]]++;
      } else {
         freq[list[i]]=1;
      }
      i++;
   }
   return freq
}

// Display an extract of the text on the webpage
function loadBlock(){
    // Get the extract number
    var blockNb = parseInt($("#blockNumber").val())-1;
    var i = intervalLength * blockNb;
    var fragment = "";
    while (i < intervalLength * (blockNb+1)){
      var wordToSearch = textWords[i];
      if($("#minuscules").prop("checked")){
         if(wordToSearch!=undefined){
            wordToSearch = wordToSearch.toLowerCase();
         }
      }

      if(textPunctuation[i]!=undefined){
      if(wordDict[wordToSearch] != null){
        fragment += textPunctuation[i].replace(/¤/g,"<br/>")+"<strong>"+textWords[i]+"</strong>";
      } else {
        if(wordDict2[wordToSearch] != null){
          fragment += textPunctuation[i].replace(/¤/g,"<br/>")+"<strong class=\"topic\">"+textWords[i]+"</strong>";
        } else {
          fragment += textPunctuation[i].replace(/¤/g,"<br/>")+textWords[i];
        }
      }
      }
      i++;
    }
    $("#fragment").html(fragment);
  }

$(document).ready(function(){  

  // Hide the result block
  $(".block").eq(0).hide();
  
  // Load a different extract of the text if the keyboard is used to change the block number
  $("#blockNumber").on("change",loadBlock)

  $("#start").on("click",function(){
  
    // Get a list of all the words in the input word lists
    var theWords = $("#words1").val();
    if($("#minuscules").prop("checked")){
       theWords = theWords.toLowerCase();
    }
    var wordList = wordsAndPunctuation(theWords.replace(/(?:\r\n|\r|\n)/g, ' '))[1];

    theWords = $("#words2").val();
    if($("#minuscules").prop("checked")){
       theWords = theWords.toLowerCase();
    }
    var wordList2 = wordsAndPunctuation(theWords.replace(/(?:\r\n|\r|\n)/g, ' '))[1];

    var theText = $("#text").val();
    
    // Get a list of all punctuation sequences and words
    var wordPunctuationList = wordsAndPunctuation(theText.replace(/(?:\r\n|\r|\n)/g, '¤'))
    textPunctuation = wordPunctuationList[0];
    textWords = wordPunctuationList[1];
    
    // Get a dictionary which associates to each word of the word lists its number of occurrences
    wordDict = frequencies(wordList);
    wordDict2 = frequencies(wordList2);
    
    // Compute the block length depending on the text length and the chosen number of blocks
    intervalNb = parseInt($("#intervalNumber").val());
    intervalLength = Math.floor(textWords.length/intervalNb)+1;
    
    var data = [];
    var data2 = [];
    var i = 0;
    var block = 0;
    var wordNb = 0;
    var wordNb2 = 0;
    var intervalNumbers = [];
    
    while (i < textWords.length){
      
      //if(i%10 == 0){
      //  console.log(textWords[i]+" "+i+"/"+textWords.length)
      //}
      
      var wordToSearch = textWords[i];
      if($("#minuscules").prop("checked")){
         wordToSearch = wordToSearch.toLowerCase()
      }
      
      if(wordToSearch in wordDict){
         //console.log("found "+textWords[i]+"!");
         wordNb ++;
      }

      if(wordToSearch in wordDict2){
         //console.log("found "+textWords[i]+"!");
         wordNb2 ++;
      }

      i++;
      
      if(i%intervalLength == 0){
         // Add to the data the number of words found in the block
         data.push(wordNb);
         data2.push(wordNb2);
         intervalNumbers.push(block+1);
         wordNb = 0;
         wordNb2 = 0;
         block ++;
      }
    }
    
    data.push(wordNb);
    data2.push(wordNb2);
    intervalNumbers.push(block+1);
    console.log(data);
    console.log(intervalNumbers);
    $("#blockNumber").attr("min",1);
    $("#blockNumber").attr("max",data.length);

    
    // console.log("intervals: "+intervalNumbers);
    // console.log("values: "+data);
    
    
    var myPlot = document.getElementById('results');
    /*
    if(!noTraceYet){
       Plotly.deleteTraces(myPlot, 0);
    }
    noTraceYet = false;
    */

    var traces = [
  	{x: intervalNumbers, y: data, stackgroup: 'one', line:{color:"#ffffff00"}, fillcolor: '#ff4444', name: 'première liste'},
	  {x: intervalNumbers, y: data2, stackgroup: 'one', line:{color:"#ffffff00"}, fillcolor: '#FFCC66', name: 'deuxième liste'},
    ];

    Plotly.newPlot('results', traces,  {margin: {l:20, r:20, t: 20,b: 20}});
    loadBlock();
    
    myPlot.on('plotly_click', function(data){
       $("#blockNumber").val(data.points[0].x);
       loadBlock();
    });    
    $(".block").eq(0).show();
  })
  
})
