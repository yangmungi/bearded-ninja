document.write("<!-- -->");

var terminalBuilder = function(pre, rows, cols) {
    obj = {
            pre: pre,
            rows: rows,
            cols: cols,
            buffer: [],
        };

    var buffer = obj.buffer;
    for (var r = 0; r < rows; r++) {
        buffer[r] = [];
        for (var c = 0; c < cols; c++) {
            buffer[r][c] = '';
        }
    }

    obj.writeHorizontal = function(msg, row, col) {

    };

    // operates like a normal console, starting from most bottom-right block
    obj.write = function(msg) {
        var print;
        if (Array.isArray(msg)) {
            // render clean
            var maxLength = 0;
            print = "";

            for (var i in msg) {
                var c =  msg[i];
                var cLength = c.toString().length;
                if (cLength > maxLength) {
                    maxLength = cLength;
                }
            }

            maxLength += 1;

            // pad()
            var padString = ' ';
            for (var i = 0; i < maxLength; i++) {
                padString += ' ';
            }

            for (var i in msg) {
                print += (padString + msg[i]).slice(-1 * maxLength);
            }
        } else {
            print = msg.toString();
        }

        obj.pre.innerHTML += (print + "\n");
    };

    return obj;
};

// bootstrap ``console''
var consoleDom = document.getElementById("console");
var terminal = terminalBuilder(consoleDom, 30, 20);

//
// build cards out
//

var suits = ['C', 'D', 'H', 'S'];

var ranks = ['A'];
for (var i = 2; i < 10; i++) {
    ranks.push(String(i));
}
ranks = ranks.concat(['T', 'J', 'Q', 'K']);

function Card(suit, rank) {
    this.suit = suit;
    this.rank = rank;

    this.getRank = function() {
        return this.rank;
    };

    this.getSuit = function() {
        return this.suit;
    };

    this.compareTo = function(otherCard) {
        var otherRank = ranks.indexOf(otherCard.getRank());
        var myRank = ranks.indexOf(this.getRank());
        // todo: checks

        if (myRank === otherRank) {
           var otherSuit = suits.indexOf(otherCard.getSuit());
           var mySuit = suits.indexOf(this.getSuit());

           // todo: checks

           return otherSuit - mySuit;
        } else {
            return otherRank - myRank;
        }
    };

    this.greaterThan = function(otherCard) {
        return this.compareTo(otherCard) > 0;
    };

    this.lessThan = function(otherCard) {
        return this.compareTo(otherCard) < 0;
    };

    this.equalTo = function(otherCard) {
        return this.compareTo(otherCard) === 0;
    };
};

//
//
//

var deck = [];
for (var suitI in suits) {
    var suit = suits[suitI];
    for (var rankI in ranks) {
        var rank = ranks[rankI];
        var card = new Card(suit, rank);

        deck.push(card);
    }
}

var printDeck = function(deck) {
    for (var cardI in deck) {
        var card = deck[cardI];

        terminal.write(card.getSuit() + card.getRank());
    }
};

var buildShuffler = function(list) {
    var t = {
            list: list,
        };

    t.shuffleHelper = function(offset) {
        var list = t.list;
        var listLength = list.length;

        // @todo compensate for odd lists
        var halfOffset = offset / 2;
        var halfListLength = listLength / 2 + halfOffset;
        if (listLength - offset <= 2) {
            return;
        }

        // assume list[i] is where it is supposed to be
        // replace next one with half one
        var i = offset;
        var nextIterFrom;

        var from, to;
        var tmp;

        from = i + 1;
        to = halfListLength

        tmp = list[from];
        list[from] = list[to];
        list[to] = tmp;

        // doing a search?
        // @todo see if there's a mathematical way/iterative way instead of 
        // searching
        for (var j = offset; j <= halfListLength; j++) {
            if (list[j] == halfOffset + 2) {
                nextIterFrom = j;
                break;
            }
        }

        // debugging help
        var helper = [];
        for (var j = 0; j < listLength; j++) {
            if (j == offset) {
                helper[j] = '|';
            } else if (j == halfListLength) {
                helper[j] = '.';
            } else if (j == nextIterFrom) {
                helper[j] = '!';
            } else {
                helper[j] = '';
            }
        }

        // iteration step
        helper.push(halfOffset);
        // next iteration value offset
        helper.push(nextIterFrom);
        // distance from half
        helper.push(halfListLength - nextIterFrom);
        // absolute offset from iteration starter
        helper.push(nextIterFrom - offset);
        helper.push(listLength);

        terminal.write(helper);
        terminal.write(list);

        // next iteration is to assume list[i + 2] is where it is supposed to
        // be, so move that one back
        
        from = i + 2;
        to = nextIterFrom;

        tmp = list[from];
        list[from] = list[to];
        list[to] = tmp;

        terminal.write(list);
    };

    t.shuffle = function() {
        var list = t.list;
        var listLength = list.length;

        terminal.write(list);

        if (listLength == 2) {
            return;
        }

        for (var i = 0; i < listLength; i += 2) {
            t.shuffleHelper(i);
        }

        terminal.write(list);
    };

    return t;
};

//
//
//

var smaller = [];
for (var i = 1; i <= 200; i++) {
    smaller.push(i);
}

var shuffler = buildShuffler(smaller);
shuffler.shuffle();
