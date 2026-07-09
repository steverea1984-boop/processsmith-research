# Transcript: Google DeepMind's Logan Kilpatrick - Why the Model Eats the Harness

Source: YouTube captions for https://www.youtube.com/watch?v=cMAs8z2dehs

 
So we could edit this set so it looks
 
So we could edit this set so it looks
like we're on
 
like we're on
&gt;&gt; Yes. Yeah, yeah, we I want this where
 
&gt;&gt; Yes. Yeah, yeah, we I want this where
where we were talking off camera like we
 
where we were talking off camera like we
should do that for the intro because I
 
should do that for the intro because I
think it just like makes all this stuff
 
think it just like makes all this stuff
more capable. I've seen these examples
 
more capable. I've seen these examples
of like such subtle nuance that like
 
of like such subtle nuance that like
make me appreciate that it's like the
 
make me appreciate that it's like the
world understanding playing out. I was I
 
world understanding playing out. I was I
was giving a talk um
 
was giving a talk um
and was on stage with with my friend
 
and was on stage with with my friend
Tulsi who leads the model team. I had
 
Tulsi who leads the model team. I had
mentioned to someone in the crowd to
 
mentioned to someone in the crowd to
like edit the video and they had
 
like edit the video and they had
literally like took the picture, edited
 
literally like took the picture, edited
it with omni in real time and this like
 
it with omni in real time and this like
dog came on the stage in the edited
 
dog came on the stage in the edited
version. The other guests sort of like
 
version. The other guests sort of like
looked down and see the dog. They like
 
looked down and see the dog. They like
chuckle a little bit. This is while I'm
 
chuckle a little bit. This is while I'm
like opining about whatever AI nonsense.
 
like opining about whatever AI nonsense.
&gt;&gt; jokes.
 
&gt;&gt; jokes.
&gt;&gt; Yeah, that it was not my jokes. They
 
&gt;&gt; Yeah, that it was not my jokes. They
[laughter] they laugh at the dog coming
 
[laughter] they laugh at the dog coming
up. It jumps onto my lap. I sort of like
 
up. It jumps onto my lap. I sort of like
acknowledge the dog. I keep talking. I'm
 
acknowledge the dog. I keep talking. I'm
like petting it or whatever and just
 
like petting it or whatever and just
like there's like so much subtle
 
like there's like so much subtle
subtlety in getting that right and the
 
subtlety in getting that right and the
model crushed it and it's just it it
 
model crushed it and it's just it it
very interesting and like still trying
 
very interesting and like still trying
to like absorb and digest [music] like
 
to like absorb and digest [music] like
what that means for you know, the way we
 
what that means for you know, the way we
make content and all these other things.
 
make content and all these other things.
&gt;&gt; That's so interesting.
 
&gt;&gt; [music]
 
[music]
 
&gt;&gt; I'm delighted to have Logan on the show.
 
&gt;&gt; I'm delighted to have Logan on the show.
Logan runs Google AI studio and the
 
Logan runs Google AI studio and the
Gemini API. You spend a lot of your time
 
Gemini API. You spend a lot of your time
thinking and building for the next
 
thinking and building for the next
generation of builders.
 
generation of builders.
&gt;&gt; Yes.
 
&gt;&gt; Yes.
&gt;&gt; So I'm excited to talk to you about
 
&gt;&gt; So I'm excited to talk to you about
everything from my agentic AI to AI
 
everything from my agentic AI to AI
coding, world models and more today and
 
coding, world models and more today and
right off the heels of Google IO. So
 
right off the heels of Google IO. So
what better timing?
 
what better timing?
&gt;&gt; Yeah, I'm super excited. Thank you for
 
&gt;&gt; Yeah, I'm super excited. Thank you for
having me.
 
having me.
&gt;&gt; Wonderful. Um let's start with agentic
 
&gt;&gt; Wonderful. Um let's start with agentic
AI. So Sundar opened IO by calling this
 
AI. So Sundar opened IO by calling this
the agentic Gemini era. What does
 
the agentic Gemini era. What does
agentic AI mean for Google?
 
agentic AI mean for Google?
&gt;&gt; Yeah. It's a good question. I think and
 
&gt;&gt; Yeah. It's a good question. I think and
we were
 
we were
uh we sort of if you if you followed
 
uh we sort of if you if you followed
closely, we did sort of mention some of
 
closely, we did sort of mention some of
these things back with like Gemini 2.0,
 
these things back with like Gemini 2.0,
which I think was like a a little bit
 
which I think was like a a little bit
early. And so, I think this era, this
 
early. And so, I think this era, this
like Gemini 3.5 era, feels like it's
 
like Gemini 3.5 era, feels like it's
actually becoming true now and we're in
 
actually becoming true now and we're in
the era of agentic coding uh or agentic
 
the era of agentic coding uh or agentic
products and everything agents as far as
 
products and everything agents as far as
Gemini goes. I think for us
 
Gemini goes. I think for us
this agentic layer, and I think we we
 
this agentic layer, and I think we we
announced this actually at IO, um sort
 
announced this actually at IO, um sort
of being powered by the anti-gravity
 
of being powered by the anti-gravity
agent harness, is this like additional
 
agent harness, is this like additional
through line for Google that sort of
 
through line for Google that sort of
connects all of our products that
 
connects all of our products that
they're sort of like based on now. And
 
they're sort of like based on now. And
so, historically like prior to Gemini,
 
so, historically like prior to Gemini,
there actually like wasn't a through
 
there actually like wasn't a through
line for the, you know, probably
 
line for the, you know, probably
sub-100 number of Google products that
 
sub-100 number of Google products that
we have, the 50 Google products we have,
 
we have, the 50 Google products we have,
there wasn't a through line. We had
 
there wasn't a through line. We had
Gemini, it became this through line,
 
Gemini, it became this through line,
everything is now sort of using Gemini
 
everything is now sort of using Gemini
in some way. That's now becoming true
 
in some way. That's now becoming true
for anti-gravity as sort of all of the
 
for anti-gravity as sort of all of the
products rebase um to become sort of
 
products rebase um to become sort of
like agentic native products and like
 
like agentic native products and like
actually taking action on behalf of
 
actually taking action on behalf of
users and helping them get things done.
 
users and helping them get things done.
You see this like new through line
 
You see this like new through line
emerging, which I think is actually
 
emerging, which I think is actually
really, really interesting. Um
 
really, really interesting. Um
and so
 
and so
&gt;&gt; And sorry, help me with anti-gravity is
 
&gt;&gt; And sorry, help me with anti-gravity is
the
 
the
the IDE, right? Or the non-IDE?
 
the IDE, right? Or the non-IDE?
&gt;&gt; Yeah, anti-gravity is is a lot of
 
&gt;&gt; Yeah, anti-gravity is is a lot of
things, which I think is is sort of
 
things, which I think is is sort of
again uh is an is an opportunity for us.
 
again uh is an is an opportunity for us.
Um you have sort of a core IDE, you have
 
Um you have sort of a core IDE, you have
sort of like the agent first experience
 
sort of like the agent first experience
if you want it on the web, you have a
 
if you want it on the web, you have a
CLI, you have an SDK. So, I actually
 
CLI, you have an SDK. So, I actually
think and I don't know how much we
 
think and I don't know how much we
framed it this way, but like it really
 
framed it this way, but like it really
is an ecosystem of stuff that we built.
 
is an ecosystem of stuff that we built.
And it's designed to sort of like meet
 
And it's designed to sort of like meet
developers wherever they are. So, you
 
developers wherever they are. So, you
could use it through the Gemini API if
 
could use it through the Gemini API if
you want to and you want a managed agent
 
you want to and you want a managed agent
that you don't have to do any of the the
 
that you don't have to do any of the the
sort of infrastructure work for. Um
 
sort of infrastructure work for. Um
and then the most interesting bit is
 
and then the most interesting bit is
like it's not just the ecosystem of
 
like it's not just the ecosystem of
anti-gravity stuff, it's also powering
 
anti-gravity stuff, it's also powering
like literally it's the the same harness
 
like literally it's the the same harness
is actually powering all the other
 
is actually powering all the other
Google products. So, anti-gravity will
 
Google products. So, anti-gravity will
be powering a bunch of agent stuff in
 
be powering a bunch of agent stuff in
search, in the Gemini app, um across
 
search, in the Gemini app, um across
like cloud and and ASU deal, which is
 
like cloud and and ASU deal, which is
really exciting.
 
really exciting.
&gt;&gt; I see. So, it used to be the Gemini API,
 
&gt;&gt; I see. So, it used to be the Gemini API,
so like the language model was the
 
so like the language model was the
through line in terms of how AI gets
 
through line in terms of how AI gets
baked into every Google product.
 
baked into every Google product.
&gt;&gt; Yeah.
 
&gt;&gt; Yeah.
&gt;&gt; And now it's not only the API, it's the
 
&gt;&gt; And now it's not only the API, it's the
the coding harness.
 
the coding harness.
&gt;&gt; Exactly.
 
&gt;&gt; Exactly.
&gt;&gt; Um that's that's being used into these
 
&gt;&gt; Um that's that's being used into these
products and therefore it's a coding
 
products and therefore it's a coding
agent itself that's driving more agentic
 
agent itself that's driving more agentic
properties.
 
properties.
&gt;&gt; Yeah.
 
&gt;&gt; Yeah.
&gt;&gt; products.
 
&gt;&gt; products.
&gt;&gt; Yeah, and I think
 
&gt;&gt; Yeah, and I think
&gt;&gt; description?
 
&gt;&gt; description?
&gt;&gt; Fair fair description. I think more
 
&gt;&gt; Fair fair description. I think more
generically too, it's just like it is
 
generically too, it's just like it is
the agent harness. I think like coding
 
the agent harness. I think like coding
is sort of like a specialized use case
 
is sort of like a specialized use case
of the agent harness. I think is is
 
of the agent harness. I think is is
obviously powerful, but it is like
 
obviously powerful, but it is like
coding has proved to be the general
 
coding has proved to be the general
purpose agent harness in addition to
 
purpose agent harness in addition to
also working really well for coding.
 
also working really well for coding.
&gt;&gt; Are agent harness and coding harness
 
&gt;&gt; Are agent harness and coding harness
synonymous or not?
 
synonymous or not?
&gt;&gt; There's definitely nuance. I think
 
&gt;&gt; There's definitely nuance. I think
there's like optimization that you can
 
there's like optimization that you can
squeeze out of like specializing and
 
squeeze out of like specializing and
actually you see this where like the you
 
actually you see this where like the you
know, technically the agent harness that
 
know, technically the agent harness that
gets used for the way that AI Studio
 
gets used for the way that AI Studio
uses it is like a little bit specialized
 
uses it is like a little bit specialized
for you know, the vibe coding use case
 
for you know, the vibe coding use case
and the the way that the Gemini app is
 
and the the way that the Gemini app is
using the agent harness is a little bit
 
using the agent harness is a little bit
specialized for the sort of consumer
 
specialized for the sort of consumer
always on 24/7 agent.
 
always on 24/7 agent.
Um so, I think you have that base
 
Um so, I think you have that base
harness
 
harness
um that like probably has like 80% of
 
um that like probably has like 80% of
the same stuff and then you specialize
 
the same stuff and then you specialize
for for coding or for whatever the use
 
for for coding or for whatever the use
case is.
 
case is.
&gt;&gt; Interesting. How do you think about the
 
&gt;&gt; Interesting. How do you think about the
cannibalization of the existing
 
cannibalization of the existing
business, especially now that you are
 
business, especially now that you are
you know, going much more aggressively
 
you know, going much more aggressively
into agentic properties? Because I could
 
into agentic properties? Because I could
see, for example, if all you're doing is
 
see, for example, if all you're doing is
search or summarization, um there's you
 
search or summarization, um there's you
know, not as much of a cannibalization
 
know, not as much of a cannibalization
fear. Whereas if you're actually
 
fear. Whereas if you're actually
going through my emails, replying
 
going through my emails, replying
replying to them for me, like am I even
 
replying to them for me, like am I even
going through my email anymore? And so,
 
going through my email anymore? And so,
I could imagine that there's actually
 
I could imagine that there's actually
just fewer human eyeball hours um
 
just fewer human eyeball hours um
uh on your products as a result of
 
uh on your products as a result of
having more agentic capabilities. Is
 
having more agentic capabilities. Is
that fair or how do you think about the
 
that fair or how do you think about the
cannibalization?
 
cannibalization?
&gt;&gt; Yeah, it's interesting. I think
 
&gt;&gt; Yeah, it's interesting. I think
one sort of observation I have is that
 
one sort of observation I have is that
like at the beginning and I think
 
like at the beginning and I think
Sundar's done a great job of of sort of
 
Sundar's done a great job of of sort of
talking through this is at the beginning
 
talking through this is at the beginning
of the the sort of current AI era like
 
of the the sort of current AI era like
everyone assumed that
 
everyone assumed that
AI being able to answer questions for
 
AI being able to answer questions for
you was going to be like negative sum
 
you was going to be like negative sum
for for search. Um and actually what
 
for for search. Um and actually what
ended up happening is it's been
 
ended up happening is it's been
incredibly positive sum for search. Like
 
incredibly positive sum for search. Like
people are searching more, people are
 
people are searching more, people are
doing more. And so I think
 
doing more. And so I think
&gt;&gt; are searching, too.
 
&gt;&gt; are searching, too.
&gt;&gt; Yeah, and agent
 
&gt;&gt; Yeah, and agent
actually again, there's like this whole
 
actually again, there's like this whole
market that spawned at the same time
 
market that spawned at the same time
that agents are doing more, at the same
 
that agents are doing more, at the same
time that humans are also searching
 
time that humans are also searching
more. And so I think it will be
 
more. And so I think it will be
Obviously, there's a finite amount of
 
Obviously, there's a finite amount of
like human time in the world. Um
 
like human time in the world. Um
but from from like my early feelings of
 
but from from like my early feelings of
how a lot of this is playing out, it
 
how a lot of this is playing out, it
does feel like it's it's very positive
 
does feel like it's it's very positive
sum from like an ecosystem value
 
sum from like an ecosystem value
creation, like how the human behavior
 
creation, like how the human behavior
aspect of it turns out. I think it's
 
aspect of it turns out. I think it's
like somewhat clear in the next 1 to 2
 
like somewhat clear in the next 1 to 2
years, much less clear you know, 3 to 5
 
years, much less clear you know, 3 to 5
years from now when the technology has
 
years from now when the technology has
improved and the products probably look
 
improved and the products probably look
a little bit different than the way that
 
a little bit different than the way that
they do. But ultimately, like that is
 
they do. But ultimately, like that is
the success of product. I think like we
 
the success of product. I think like we
we have a bunch of conversations with
 
we have a bunch of conversations with
Demis all the time and it's like the
 
Demis all the time and it's like the
point of building the technology is so
 
point of building the technology is so
that it can go and do stuff for you.
 
that it can go and do stuff for you.
Like that point like success for Google
 
Like that point like success for Google
like probably doesn't look like you
 
like probably doesn't look like you
know, maximizing eyeball time in front
 
know, maximizing eyeball time in front
of our products. It's like maximizing
 
of our products. It's like maximizing
outcome for customers to like do the
 
outcome for customers to like do the
thing that they want to do so that they
 
thing that they want to do so that they
can go and live their life and do what
 
can go and live their life and do what
they want. And so I feel like
 
they want. And so I feel like
you'll you'll probably see us go down
 
you'll you'll probably see us go down
the route of like maximizing outcomes
 
the route of like maximizing outcomes
for customers and like not maximizing
 
for customers and like not maximizing
eyeballs.
 
eyeballs.
&gt;&gt; Yeah.
 
&gt;&gt; Yeah.
I have this term stuck in my head,
 
I have this term stuck in my head,
agent-led growth. Like it seems to me So
 
agent-led growth. Like it seems to me So
I'm using using coding agents a lot in
 
I'm using using coding agents a lot in
my personal time and, you know, I just
 
my personal time and, you know, I just
let the agent make all the
 
let the agent make all the
infrastructure choices for me. I'm like,
 
infrastructure choices for me. I'm like,
I don't care what database you tell me.
 
I don't care what database you tell me.
&gt;&gt; Yeah.
 
&gt;&gt; Yeah.
&gt;&gt; And and so and the reason I ask is you
 
&gt;&gt; And and so and the reason I ask is you
know, it's true in coding today. I would
 
know, it's true in coding today. I would
imagine it's maybe going to be
 
imagine it's maybe going to be
generally true for a a of things, let's
 
generally true for a a of things, let's
say shopping
 
say shopping
down the line. Um how do you think
 
down the line. Um how do you think
that's going to change how advertising
 
that's going to change how advertising
works, how value capture works for for
 
works, how value capture works for for
the aggregators?
 
the aggregators?
&gt;&gt; It feels like it's a very similar trend.
 
&gt;&gt; It feels like it's a very similar trend.
This isn't perfectly true, but a lot of
 
This isn't perfectly true, but a lot of
these things are just like proxies of
 
these things are just like proxies of
each other, like the way that SEO works,
 
each other, like the way that SEO works,
I think like is directly correlated with
 
I think like is directly correlated with
like the way that um like I forgot what
 
like the way that um like I forgot what
the term that was, it's like GEO is like
 
the term that was, it's like GEO is like
the generative engine optimization or
 
the generative engine optimization or
whatever it's called. Um
 
whatever it's called. Um
And so it does feel like there's a lot
 
And so it does feel like there's a lot
of correlation between the uh between
 
of correlation between the uh between
the things. My guess is it looks like
 
the things. My guess is it looks like
much less of a radical shift than than
 
much less of a radical shift than than
the than I think maybe what we assume
 
the than I think maybe what we assume
right now, just cuz these things
 
right now, just cuz these things
compound on top of each other.
 
compound on top of each other.
&gt;&gt; If you were to
 
&gt;&gt; If you were to
you know, grade the scale of agenticness
 
you know, grade the scale of agenticness
in terms of crawl, walk, run, where are
 
in terms of crawl, walk, run, where are
we in terms of how agentic the Google
 
we in terms of how agentic the Google
suite of products is?
 
suite of products is?
&gt;&gt; Yeah, that's a that's a great question.
 
&gt;&gt; Yeah, that's a that's a great question.
It's definitely like crawl right now. Um
 
It's definitely like crawl right now. Um
and I think some of this is like all of
 
and I think some of this is like all of
the inherent product tension for Google
 
the inherent product tension for Google
is like you have what, 13 billion plus
 
is like you have what, 13 billion plus
user products. And so like I actually
 
user products. And so like I actually
think we have some more like labs-like
 
think we have some more like labs-like
experiences where you're probably closer
 
experiences where you're probably closer
to running uh or walking. Um but I think
 
to running uh or walking. Um but I think
like most of the product experience
 
like most of the product experience
today is definitely closer to crawling.
 
today is definitely closer to crawling.
And I think that's just like the
 
And I think that's just like the
stewardship responsibility we have sort
 
stewardship responsibility we have sort
of building a product that's being used
 
of building a product that's being used
by lots of people. Like I don't think
 
by lots of people. Like I don't think
the long tail of customers are like
 
the long tail of customers are like
ready to have AI running and just doing
 
ready to have AI running and just doing
all the things. Like they probably they
 
all the things. Like they probably they
want to be in the driver's seat. They're
 
want to be in the driver's seat. They're
cautiously taking the first step. And I
 
cautiously taking the first step. And I
think the the Google team and like
 
think the the Google team and like
search is maybe like the most
 
search is maybe like the most
quintessential example of this. Like I
 
quintessential example of this. Like I
think they have a lot of responsibility
 
think they have a lot of responsibility
to actually do that in a way that it
 
to actually do that in a way that it
brings people along and doesn't just
 
brings people along and doesn't just
like change everything of how they
 
like change everything of how they
interact with the internet and the way
 
interact with the internet and the way
they associate with products and stuff
 
they associate with products and stuff
like that. So
 
like that. So
&gt;&gt; Yeah. Which products do you think are
 
&gt;&gt; Yeah. Which products do you think are
closest to the walk?
 
closest to the walk?
&gt;&gt; That's a good question. I think Gemini
 
&gt;&gt; That's a good question. I think Gemini
app is definitely closest to walk. And
 
app is definitely closest to walk. And
so for for Spark, I think having a 24/7
 
so for for Spark, I think having a 24/7
always on agent like literally going and
 
always on agent like literally going and
potentially doing a bunch of actions on
 
potentially doing a bunch of actions on
your behalf is definitely like one of
 
your behalf is definitely like one of
the frontier use cases. And I think
 
the frontier use cases. And I think
you'll see I think like anti-gravity is
 
you'll see I think like anti-gravity is
another one where it's like you can have
 
another one where it's like you can have
autonomous coding agents, you know,
 
autonomous coding agents, you know,
rebuilding operating systems and doing,
 
rebuilding operating systems and doing,
you know, billions of tokens and
 
you know, billions of tokens and
spending thousands of dollars on your
 
spending thousands of dollars on your
behalf. And I think those are
 
behalf. And I think those are
again like more and actually like
 
again like more and actually like
they're in GDM as well as another angle
 
they're in GDM as well as another angle
of this. So, I think like GDM is taking
 
of this. So, I think like GDM is taking
like very much like a a frontier look at
 
like very much like a a frontier look at
this where I think like the rest of
 
this where I think like the rest of
Google's products I think are like more
 
Google's products I think are like more
incrementally getting there which again
 
incrementally getting there which again
makes makes reasonable sense to me.
 
makes makes reasonable sense to me.
&gt;&gt; Yeah.
 
&gt;&gt; Yeah.
Do you think that Google ends up with
 
Do you think that Google ends up with
one, two, three product surfaces for for
 
one, two, three product surfaces for for
using AI or thousands?
 
using AI or thousands?
&gt;&gt; It's tough.
 
&gt;&gt; It's tough.
I think a lot of this is actually baked
 
I think a lot of this is actually baked
in just like how humans consume
 
in just like how humans consume
products. And my sense is that there's
 
products. And my sense is that there's
something nice about like having this
 
something nice about like having this
like compartmentalization and this like
 
like compartmentalization and this like
specialization of products where like it
 
specialization of products where like it
becomes if you end up with a product
 
becomes if you end up with a product
that is like doing everything for you,
 
that is like doing everything for you,
inherently there's more work involved in
 
inherently there's more work involved in
using that version of the product. I
 
using that version of the product. I
think I think would be like the default
 
think I think would be like the default
state. I think maybe somebody will spin
 
state. I think maybe somebody will spin
together like the truly magic experience
 
together like the truly magic experience
that doesn't make that true, but I think
 
that doesn't make that true, but I think
I think the long tail of folks end up
 
I think the long tail of folks end up
having to spend more mental energy and
 
having to spend more mental energy and
more time to actually like get the
 
more time to actually like get the
general purpose product to do the thing
 
general purpose product to do the thing
that they actually want to do versus
 
that they actually want to do versus
like there's something nice about I
 
like there's something nice about I
click my calendar app, it just shows me
 
click my calendar app, it just shows me
my calendar. Like I don't need to worry
 
my calendar. Like I don't need to worry
and deal with anything else.
 
and deal with anything else.
&gt;&gt; This is my hot take for why slide decks
 
&gt;&gt; This is my hot take for why slide decks
have existed for so long of just like
 
have existed for so long of just like
you know, the thing the piece of
 
you know, the thing the piece of
information you want to be exactly in
 
information you want to be exactly in
the same place. Um and I think like we
 
the same place. Um and I think like we
as humans are just actually very used
 
as humans are just actually very used
used to that as opposed to
 
used to that as opposed to
the idea of a generative interface
 
the idea of a generative interface
sounds so cool to me, but it's like are
 
sounds so cool to me, but it's like are
do our brains really isn't it just more
 
do our brains really isn't it just more
cognitive overhead for us?
 
cognitive overhead for us?
&gt;&gt; It definitely is in certain cases and I
 
&gt;&gt; It definitely is in certain cases and I
think somebody needs to again there's
 
think somebody needs to again there's
there's a lot of incredibly smart people
 
there's a lot of incredibly smart people
in the world and so maybe somebody will
 
in the world and so maybe somebody will
find the experience that like makes it
 
find the experience that like makes it
feel more natural, but to me right now
 
feel more natural, but to me right now
I'm I'm maybe not 10,000 is the extreme
 
I'm I'm maybe not 10,000 is the extreme
version. I'm guessing it looks more like
 
version. I'm guessing it looks more like
more products going after sort of like
 
more products going after sort of like
different
 
different
and maybe the other answer is like I
 
and maybe the other answer is like I
don't know what it looks like for Google
 
don't know what it looks like for Google
for the ecosystem. It looks like a lot
 
for the ecosystem. It looks like a lot
more products, I think. Like and that's
 
more products, I think. Like and that's
that's really exciting. I think like how
 
that's really exciting. I think like how
Google will end up strategically
 
Google will end up strategically
deciding like do our customers want to
 
deciding like do our customers want to
deal with us having 10,000 products or
 
deal with us having 10,000 products or
would it be better to only have three?
 
would it be better to only have three?
Um will come down to like a strategic
 
Um will come down to like a strategic
decision for us.
 
decision for us.
&gt;&gt; That's totally makes sense.
 
&gt;&gt; That's totally makes sense.
Um when I talk to companies in the
 
Um when I talk to companies in the
enterprise, they say, you know,
 
enterprise, they say, you know,
everyone's talking about agentic AI, but
 
everyone's talking about agentic AI, but
the only place they've seen agents
 
the only place they've seen agents
really working is coding agents. Do you
 
really working is coding agents. Do you
agree or disagree with that take?
 
agree or disagree with that take?
&gt;&gt; Yeah, I think it depends what your bar
 
&gt;&gt; Yeah, I think it depends what your bar
for working is, which I think is a lot
 
for working is, which I think is a lot
of the nuance of this. Like I think if
 
of the nuance of this. Like I think if
you're if you're truly trying to like
 
you're if you're truly trying to like
offload very complicated tasks for for
 
offload very complicated tasks for for
domains in which like it's the models
 
domains in which like it's the models
haven't actually crossed the threshold
 
haven't actually crossed the threshold
of quality, then like I think that's
 
of quality, then like I think that's
definitely true. Like the it's not going
 
definitely true. Like the it's not going
to solve the problem, but this is
 
to solve the problem, but this is
something that I want I wish we could
 
something that I want I wish we could
like measure. A good example is like
 
like measure. A good example is like
open router for example is like
 
open router for example is like
measuring, you know, the the total token
 
measuring, you know, the the total token
consumption that's happening. And so you
 
consumption that's happening. And so you
can sort of like see these trends play
 
can sort of like see these trends play
out over time of like how much more
 
out over time of like how much more
intelligence is in the world you know,
 
intelligence is in the world you know,
now versus a year ago. In parallel, the
 
now versus a year ago. In parallel, the
thing that I'm actually really
 
thing that I'm actually really
interested to measure is like how long
 
interested to measure is like how long
is the average like thing the average
 
is the average like thing the average
like agent run or the average task
 
like agent run or the average task
actually taking place. And it's I don't
 
actually taking place. And it's I don't
think it's something that they publish,
 
think it's something that they publish,
but I feel like they probably have
 
but I feel like they probably have
interesting data. I'm sure there's
 
interesting data. I'm sure there's
others. Cuz because I I do think you're
 
others. Cuz because I I do think you're
like seeing these like new model
 
like seeing these like new model
capability lands or new model drop and
 
capability lands or new model drop and
and it's like spiking up. And and maybe
 
and it's like spiking up. And and maybe
the the curve is still like very low
 
the the curve is still like very low
right now, but like you're seeing those
 
right now, but like you're seeing those
like early signs of it spiking up or to
 
like early signs of it spiking up or to
like long running tasks and all the
 
like long running tasks and all the
model labs are talking about like we
 
model labs are talking about like we
released this new model and it did, you
 
released this new model and it did, you
know, 3 days of autonomous work or
 
know, 3 days of autonomous work or
whatever it is."
 
whatever it is."
Um that that's the extreme, but I think
 
Um that that's the extreme, but I think
in practice you're seeing that like
 
in practice you're seeing that like
trickling up like pretty pretty quickly,
 
trickling up like pretty pretty quickly,
which is really interesting. So, even if
 
which is really interesting. So, even if
the enterprises haven't felt it outside
 
the enterprises haven't felt it outside
of coding, like they are going to like
 
of coding, like they are going to like
this year um as as sort of a bunch of
 
this year um as as sort of a bunch of
those other use cases get get much
 
those other use cases get get much
better as well.
 
better as well.
&gt;&gt; From like a, you know, from the DeepMind
 
&gt;&gt; From like a, you know, from the DeepMind
perspective, do you think long horizon
 
perspective, do you think long horizon
agents is like a KPI that matters? Is it
 
agents is like a KPI that matters? Is it
the Is it the KPI that matters?
 
the Is it the KPI that matters?
&gt;&gt; It definitely It definitely matters.
 
&gt;&gt; It definitely It definitely matters.
Um
 
Um
I think for DeepMind like we're doing
 
I think for DeepMind like we're doing
lots of things, which which we can talk
 
lots of things, which which we can talk
more about later. Like there's, you
 
more about later. Like there's, you
know, a a huge portfolio of of different
 
know, a a huge portfolio of of different
bets that are taking place. Long writing
 
bets that are taking place. Long writing
agents obviously matters a lot. And I
 
agents obviously matters a lot. And I
think also like specifically coding
 
think also like specifically coding
agents and that matters a lot. Like it
 
agents and that matters a lot. Like it
clearly is an accelerant of like every
 
clearly is an accelerant of like every
other part of your business if you have
 
other part of your business if you have
a great coding model.
 
a great coding model.
Um and so making sure we have that I
 
Um and so making sure we have that I
think is is super top of mind.
 
think is is super top of mind.
&gt;&gt; Got it. Um I'd love to shift gears a
 
&gt;&gt; Got it. Um I'd love to shift gears a
little bit and talk about coding.
 
little bit and talk about coding.
&gt;&gt; Yeah.
 
&gt;&gt; Yeah.
&gt;&gt; Um okay, I'm going to ask a hard
 
&gt;&gt; Um okay, I'm going to ask a hard
question.
 
question.
Uh
 
Uh
a lot of my developer friends were using
 
a lot of my developer friends were using
Claude for a long time.
 
Claude for a long time.
OpenAI saw that declared code red. Codex
 
OpenAI saw that declared code red. Codex
is now really good. I'd say my friends
 
is now really good. I'd say my friends
are maybe split 50/50 now in using
 
are maybe split 50/50 now in using
Claude and using Codex. I don't hear a
 
Claude and using Codex. I don't hear a
ton of them using Gemini, which is
 
ton of them using Gemini, which is
always kind of puzzled me.
 
always kind of puzzled me.
Um
 
Um
what's going on with that?
 
what's going on with that?
&gt;&gt; Yeah, it's a great question. I think
 
&gt;&gt; Yeah, it's a great question. I think
there's one there's one part of the
 
there's one there's one part of the
story that I'll add, which is which
 
story that I'll add, which is which
which is it makes it even more which is
 
which is it makes it even more which is
uh
 
uh
December the narrative was that Google
 
December the narrative was that Google
had won.
 
had won.
Um and when we landed Gemini 3, I think
 
Um and when we landed Gemini 3, I think
it was like such a such a profound
 
it was like such a such a profound
improvement from a model capability
 
improvement from a model capability
perspective. I think a lot of the
 
perspective. I think a lot of the
narrative was like Google has taken a
 
narrative was like Google has taken a
huge leap forward um and and made that
 
huge leap forward um and and made that
happen. And I think it what was
 
happen. And I think it what was
interesting to see sort of as a as an
 
interesting to see sort of as a as an
ecosystem participant uh is like how not
 
ecosystem participant uh is like how not
how quickly that narrative shifted, but
 
how quickly that narrative shifted, but
just like the next wind of the narrative
 
just like the next wind of the narrative
obviously was like all the agentic
 
obviously was like all the agentic
coding stuff that happened over over the
 
coding stuff that happened over over the
holidays and then into January and
 
holidays and then into January and
beyond.
 
beyond.
Um and that was that was not that long
 
Um and that was that was not that long
ago.
 
ago.
Um and so it's a it is a
 
Um and so it's a it is a
&gt;&gt; Feel like we've been in warp speed ever
 
&gt;&gt; Feel like we've been in warp speed ever
since.
 
since.
&gt;&gt; Yeah, for sure. And but it is it's a
 
&gt;&gt; Yeah, for sure. And but it is it's a
matter reminder of like just how fast
 
matter reminder of like just how fast
things can can change.
 
things can can change.
Um I think the observation is is not is
 
Um I think the observation is is not is
not unreasonable. I do think the what's
 
not unreasonable. I do think the what's
happening behind the scenes for us is
 
happening behind the scenes for us is
like trying to push the frontiers as
 
like trying to push the frontiers as
fast as possible on coding.
 
fast as possible on coding.
Um and so I think antigravity actually
 
Um and so I think antigravity actually
like is an important part of that. I
 
like is an important part of that. I
think one of the takeaways is that it's
 
think one of the takeaways is that it's
actually really hard to make a great
 
actually really hard to make a great
coding model for this like um for this
 
coding model for this like um for this
developer use case of like really long
 
developer use case of like really long
running sweet
 
running sweet
work if you don't actually have a
 
work if you don't actually have a
product that does that. And so I think
 
product that does that. And so I think
like Google realized that. That's why
 
like Google realized that. That's why
this sort of like windsurf uh deal
 
this sort of like windsurf uh deal
happened. It's why those folks came over
 
happened. It's why those folks came over
and then ultimately built antigravity
 
and then ultimately built antigravity
and sort of we've been using internally
 
and sort of we've been using internally
actually and Sundar showed this at IO.
 
actually and Sundar showed this at IO.
Uh just like the graph of growth of
 
Uh just like the graph of growth of
token consumption inside of Google. Um
 
token consumption inside of Google. Um
so you sort of like you need that engine
 
so you sort of like you need that engine
to spin and sort of the meta comment
 
to spin and sort of the meta comment
again is like the engine is spinning. It
 
again is like the engine is spinning. It
takes time uh in order to like actually
 
takes time uh in order to like actually
make model progress.
 
make model progress.
Um but I'm super confident. I think the
 
Um but I'm super confident. I think the
the folks the group of folks who we have
 
the folks the group of folks who we have
working on code is like uh I describe it
 
working on code is like uh I describe it
as like the Avengers of AI internally.
 
as like the Avengers of AI internally.
Um and so like it really is like the
 
Um and so like it really is like the
some of the best people inside of Google
 
some of the best people inside of Google
trying to push the rock up the hill on
 
trying to push the rock up the hill on
this stuff and it taking it super
 
this stuff and it taking it super
seriously and trying to push. And I
 
seriously and trying to push. And I
think three flash um
 
think three flash um
you know, notwithstanding like some of
 
you know, notwithstanding like some of
the conversation about like the price
 
the conversation about like the price
and stuff like that like is sort of a a
 
and stuff like that like is sort of a a
step towards actually starting to bring
 
step towards actually starting to bring
a lot of these capabilities
 
a lot of these capabilities
um and like the fruits of that labor
 
um and like the fruits of that labor
paying off. Like it's a flash model
 
paying off. Like it's a flash model
that's better than any pro model we've
 
that's better than any pro model we've
ever really released from a coding
 
ever really released from a coding
standpoint. Um and the pro models were
 
standpoint. Um and the pro models were
really good before. So there's another
 
really good before. So there's another
thread of this
 
thread of this
also which is like everyone forgets that
 
also which is like everyone forgets that
there's like pre-training windows and I
 
there's like pre-training windows and I
wonder like somebody should like track
 
wonder like somebody should like track
this online which would be interesting
 
this online which would be interesting
to see.
 
to see.
&gt;&gt; Meaning like the big run, like what
 
&gt;&gt; Meaning like the big run, like what
clusters have been available and like
 
clusters have been available and like
&gt;&gt; Exactly. The big The big runs are like
 
&gt;&gt; Exactly. The big The big runs are like
are an interesting thread of this and so
 
are an interesting thread of this and so
it like it might look from an external
 
it like it might look from an external
perspective that like oh you're you're
 
perspective that like oh you're you're
super behind in some way and like
 
super behind in some way and like
actually you you miss all the context of
 
actually you you miss all the context of
like where the big runs are and where
 
like where the big runs are and where
the large pre-training runs are.
 
the large pre-training runs are.
Um so I think that that also like
 
Um so I think that that also like
obviously there's
 
obviously there's
pre-training has historically been like
 
pre-training has historically been like
a massive strength for DeepMind like we
 
a massive strength for DeepMind like we
have some of the best people in the
 
have some of the best people in the
world and so excited to see sort of the
 
world and so excited to see sort of the
fruits of that labor and and everything
 
fruits of that labor and and everything
else that's happened. Like 3.5
 
else that's happened. Like 3.5
flash was like all post-training gains
 
flash was like all post-training gains
which is really cool. Um so a huge uh
 
which is really cool. Um so a huge uh
huge testament to the team that the work
 
huge testament to the team that the work
that that team did to actually like make
 
that that team did to actually like make
the level of gains and like surpass the
 
the level of gains and like surpass the
previous pro model um literally just
 
previous pro model um literally just
with post-training which is awesome.
 
with post-training which is awesome.
&gt;&gt; Mhm.
 
&gt;&gt; Mhm.
How religious are you all about dog
 
How religious are you all about dog
fooding internally?
 
fooding internally?
Like are for example are DeepMind folks
 
Like are for example are DeepMind folks
still allowed to use other models or is
 
still allowed to use other models or is
it like you guys are using the Gemini
 
it like you guys are using the Gemini
harness now and we have to make this
 
harness now and we have to make this
really really good?
 
really really good?
&gt;&gt; Yeah, there's I mean I think people it's
 
&gt;&gt; Yeah, there's I mean I think people it's
so healthy to be using other models just
 
so healthy to be using other models just
cuz like it's it's so sometimes hard to
 
cuz like it's it's so sometimes hard to
like actually grok what's happening in
 
like actually grok what's happening in
the ecosystem if you're not so like I
 
the ecosystem if you're not so like I
use all the models I use all the
 
use all the models I use all the
products. Um I think like you know
 
products. Um I think like you know
uh folks across the rest of DeepMind are
 
uh folks across the rest of DeepMind are
doing the same thing. You definitely
 
doing the same thing. You definitely
have to use the Gemini models though. Um
 
have to use the Gemini models though. Um
it's just like great from uh from a
 
it's just like great from uh from a
feedback flywheel perspective and it's
 
feedback flywheel perspective and it's
part of how they get better is like
 
part of how they get better is like
DeepMind has and Google more broadly has
 
DeepMind has and Google more broadly has
like a hundred thousand plus incredible
 
like a hundred thousand plus incredible
engineers who are using the models and
 
engineers who are using the models and
giving feedback and like it should be a
 
giving feedback and like it should be a
competitive advantage for Google because
 
competitive advantage for Google because
we have that scale of sort of
 
we have that scale of sort of
engineering resources and like the depth
 
engineering resources and like the depth
of the talent and can run you know AB
 
of the talent and can run you know AB
tests and live experiments and all that
 
tests and live experiments and all that
stuff. So
 
stuff. So
um
 
um
I think you have to use all the models
 
I think you have to use all the models
but I think for for the majority of
 
but I think for for the majority of
folks it's like Gemini as the daily
 
folks it's like Gemini as the daily
driver which is great.
 
driver which is great.
&gt;&gt; Do you believe in this narrative around
 
&gt;&gt; Do you believe in this narrative around
like a like a soft takeoff of like once
 
like a like a soft takeoff of like once
you have a good enough agentic coding
 
you have a good enough agentic coding
model, then it accelerates the pace of
 
model, then it accelerates the pace of
research progress and like it's a
 
research progress and like it's a
self-reinforcing cycle?
 
self-reinforcing cycle?
&gt;&gt; It seems obvious that that's true, but I
 
&gt;&gt; It seems obvious that that's true, but I
don't I maybe I'm I'm too I've drank in
 
don't I maybe I'm I'm too I've drank in
too much Kool-Aid that that's [laughter]
 
too much Kool-Aid that that's [laughter]
that that's the case.
 
that that's the case.
&gt;&gt; seeing the signs of it yet?
 
&gt;&gt; seeing the signs of it yet?
&gt;&gt; Yeah, I mean I you definitely see some
 
&gt;&gt; Yeah, I mean I you definitely see some
signs of this. I think the signs that
 
signs of this. I think the signs that
are like still early is doing this from
 
are like still early is doing this from
a model perspective. And I think part of
 
a model perspective. And I think part of
the context of that is like the resource
 
the context of that is like the resource
allocation for some of these like larger
 
allocation for some of these like larger
training runs is just like significant.
 
training runs is just like significant.
And so like you you definitely still
 
And so like you you definitely still
have like a human in the driver's seat
 
have like a human in the driver's seat
of making those decisions cuz like
 
of making those decisions cuz like
you're not going to
 
you're not going to
accidentally, you know, take 10,000 TPUs
 
accidentally, you know, take 10,000 TPUs
to go kick off some job that like
 
to go kick off some job that like
actually doesn't make that much sense.
 
actually doesn't make that much sense.
Um, but from a product perspective, you
 
Um, but from a product perspective, you
for sure see it. Like I think we're
 
for sure see it. Like I think we're
seeing this on our team. Like we've
 
seeing this on our team. Like we've
built mobile apps using anti-gravity and
 
built mobile apps using anti-gravity and
like we'll launch them to the world like
 
like we'll launch them to the world like
faster than I think any team at Google
 
faster than I think any team at Google
has ever built a mobile app. Josh's team
 
has ever built a mobile app. Josh's team
did this with the Gemini Mac OS app and
 
did this with the Gemini Mac OS app and
sort of like end-to-end delivered an app
 
sort of like end-to-end delivered an app
sort of faster than any team had ever
 
sort of faster than any team had ever
delivered a Mac app at Google. Um, and
 
delivered a Mac app at Google. Um, and
it's because of it's because of agentic
 
it's because of it's because of agentic
coding. And so it's great from a product
 
coding. And so it's great from a product
perspective.
 
perspective.
&gt;&gt; I think you've said in the past that if
 
&gt;&gt; I think you've said in the past that if
you could have a system that could build
 
you could have a system that could build
anything with code, humans can't compete
 
anything with code, humans can't compete
on the same level and that's narrow
 
on the same level and that's narrow
super intelligence. Do you think we've
 
super intelligence. Do you think we've
reached that point?
 
reached that point?
&gt;&gt; It is interesting. I think
 
&gt;&gt; It is interesting. I think
um
 
um
this like narrow super intelligence
 
this like narrow super intelligence
example is interesting to see how
 
example is interesting to see how
obviously it kind of feels that way for
 
obviously it kind of feels that way for
coding right now where like coding is
 
coding right now where like coding is
like just so good um that it does kind
 
like just so good um that it does kind
of feel like narrow super intelligence.
 
of feel like narrow super intelligence.
I don't know it depends how you actually
 
I don't know it depends how you actually
end up the details of quantifying this.
 
end up the details of quantifying this.
But I think the important thing is like
 
But I think the important thing is like
if to your point earlier, it works
 
if to your point earlier, it works
incredibly well for code. Um,
 
incredibly well for code. Um,
and so
 
and so
it would be great if it did a bunch of
 
it would be great if it did a bunch of
other things, but it's actually just
 
other things, but it's actually just
like so impactful that it can be great
 
like so impactful that it can be great
at code. Um and so I spent a lot of time
 
at code. Um and so I spent a lot of time
just like letting that that fact sort of
 
just like letting that that fact sort of
just like wash over me because I think
 
just like wash over me because I think
it's like obviously building AGI super
 
it's like obviously building AGI super
important and very interesting, but like
 
important and very interesting, but like
building AGI if it sort of like takes
 
building AGI if it sort of like takes
away from the story of like the current
 
away from the story of like the current
present capability of the technology, I
 
present capability of the technology, I
think it's actually like kind of a bad
 
think it's actually like kind of a bad
a bad sort of like trade-off. And so I'm
 
a bad sort of like trade-off. And so I'm
trying to like always hold these two
 
trying to like always hold these two
things in my head equal at the same
 
things in my head equal at the same
time, which is we need to build
 
time, which is we need to build
general-purpose technology, but
 
general-purpose technology, but
obviously it's so impactful to have this
 
obviously it's so impactful to have this
thing.
 
thing.
And it feels like it hasn't taken away
 
And it feels like it hasn't taken away
sort of it's been one of the best
 
sort of it's been one of the best
positive outcomes is that
 
positive outcomes is that
I feel like it hasn't taken away from
 
I feel like it hasn't taken away from
like human developers. Um it really does
 
like human developers. Um it really does
feel like an accelerant of what human
 
feel like an accelerant of what human
develop like I as a human developer feel
 
develop like I as a human developer feel
like I have more agency in the world. I
 
like I have more agency in the world. I
feel like I can tackle this is my
 
feel like I can tackle this is my
personal experience. I feel like I can
 
personal experience. I feel like I can
tackle more ambitious problems. I feel
 
tackle more ambitious problems. I feel
like used to
 
like used to
kick around ideas and they were like
 
kick around ideas and they were like
slightly out of reach um and I would
 
slightly out of reach um and I would
just be like ah wouldn't it be nice.
 
just be like ah wouldn't it be nice.
Um and now I have the opposite problem,
 
Um and now I have the opposite problem,
which is I'm I'm kicking around an idea
 
which is I'm I'm kicking around an idea
and I'm like I could probably make this
 
and I'm like I could probably make this
even more ambitious and and sort of it
 
even more ambitious and and sort of it
does it adds a different layer of sort
 
does it adds a different layer of sort
of um
 
of um
responsibility or like a some a
 
responsibility or like a some a
different layer of burden actually
 
different layer of burden actually
because I'm like oh I can't just like do
 
because I'm like oh I can't just like do
the the sort of MVP of this. Like I
 
the the sort of MVP of this. Like I
actually need to like go 10 steps
 
actually need to like go 10 steps
further because the technology enables
 
further because the technology enables
me and like resetting my my level of
 
me and like resetting my my level of
ambition I think is something that I
 
ambition I think is something that I
I've also spent a bunch of time thinking
 
I've also spent a bunch of time thinking
about. But I think that will happen in
 
about. But I think that will happen in
other these like vertical super
 
other these like vertical super
intelligence domains
 
intelligence domains
um
 
um
which will be interesting and it feels
 
which will be interesting and it feels
like we're going to get a bunch of those
 
like we're going to get a bunch of those
before we've like solved like it's
 
before we've like solved like it's
almost like jagged like jagged super
 
almost like jagged like jagged super
intelligence I think is what we'll end
 
intelligence I think is what we'll end
up with.
 
up with.
&gt;&gt; What verticals do you think we'll get
 
&gt;&gt; What verticals do you think we'll get
super intelligence at next?
 
super intelligence at next?
&gt;&gt; That's a great question. I do spend a
 
&gt;&gt; That's a great question. I do spend a
lot of my time, too much time probably,
 
lot of my time, too much time probably,
thinking about coding these days. So,
 
thinking about coding these days. So,
I'll think for a second of like the
 
I'll think for a second of like the
other
 
other
the other domains.
 
the other domains.
Um
 
Um
I think part of this is like things that
 
I think part of this is like things that
have like better verifiability,
 
have like better verifiability,
obviously, are like the ones where
 
obviously, are like the ones where
you'll you'll see the gains happen more
 
you'll you'll see the gains happen more
quickly.
 
quickly.
Um so, like things with like math and
 
Um so, like things with like math and
finance. Actually, like science could be
 
finance. Actually, like science could be
a really interesting one. Like, it would
 
a really interesting one. Like, it would
be fascinating to see like some of these
 
be fascinating to see like some of these
domains where
 
domains where
there's some level of verifiability like
 
there's some level of verifiability like
actually like really start to take off.
 
actually like really start to take off.
Um
 
Um
which would be cool and I also think
 
which would be cool and I also think
like an important thing in this like
 
like an important thing in this like
broader narrative about just like what a
 
broader narrative about just like what a
what impact AI is having on the world.
 
what impact AI is having on the world.
Like, you almost like want that to be
 
Like, you almost like want that to be
the case in the sequencing of like
 
the case in the sequencing of like
things that work. You want you a lot of
 
things that work. You want you a lot of
these like really, really good,
 
these like really, really good,
impactful, positive things for the world
 
impactful, positive things for the world
to happen
 
to happen
um as early on as humanly possible so
 
um as early on as humanly possible so
that like folks understand what the
 
that like folks understand what the
potential positive impact of the
 
potential positive impact of the
technology is. So, I think science could
 
technology is. So, I think science could
be a really interesting one. Yeah,
 
be a really interesting one. Yeah,
there's obviously there's all the stuff
 
there's obviously there's all the stuff
happening right now with like math
 
happening right now with like math
proofs and stuff like that, which I'm
 
proofs and stuff like that, which I'm
not a mathematician, so it's it's
 
not a mathematician, so it's it's
somewhat over my head, but
 
somewhat over my head, but
um
 
um
&gt;&gt; I saw a great tweet the other day. Uh
 
&gt;&gt; I saw a great tweet the other day. Uh
why did they have so many have so many
 
why did they have so many have so many
problems?
 
problems?
&gt;&gt; Exac- that's a that's a good one. I like
 
&gt;&gt; Exac- that's a that's a good one. I like
that. That is a that's a good like
 
that. That is a that's a good like
t-shirt.
 
t-shirt.
&gt;&gt; Um so funny. Okay, I but speaking of
 
&gt;&gt; Um so funny. Okay, I but speaking of
Twitter, I went through your Twitter
 
Twitter, I went through your Twitter
before this, so I'm going to read back
 
before this, so I'm going to read back
another tweet at you. The good thing
 
another tweet at you. The good thing
about Twitter is there's a public record
 
about Twitter is there's a public record
of all your predictions, so
 
of all your predictions, so
&gt;&gt; need to turn on that auto tweet deleting
 
&gt;&gt; need to turn on that auto tweet deleting
[laughter] feature or whatever it was.
 
[laughter] feature or whatever it was.
&gt;&gt; Um last October, you tweeted, "Everyone
 
&gt;&gt; Um last October, you tweeted, "Everyone
is going to be able to vibe code video
 
is going to be able to vibe code video
games by the end of 2025."
 
games by the end of 2025."
&gt;&gt; Yeah.
 
&gt;&gt; Yeah.
&gt;&gt; Did that end up being true?
 
&gt;&gt; Did that end up being true?
&gt;&gt; It feels close and I think there's I
 
&gt;&gt; It feels close and I think there's I
mean
 
mean
it obviously not AAA games. Like, you're
 
it obviously not AAA games. Like, you're
not building a you know, the next Call
 
not building a you know, the next Call
of Duty or GTA yet. Um
 
of Duty or GTA yet. Um
but I think it's it feels
 
but I think it's it feels
closer [snorts] than it's ever been.
 
closer [snorts] than it's ever been.
Um
 
Um
and
 
and
I think a lot actually a lot of the
 
I think a lot actually a lot of the
interesting bit about video games is you
 
interesting bit about video games is you
actually need to end up building a lot
 
actually need to end up building a lot
of this like other stuff. Like models
 
of this like other stuff. Like models
and we were talking off camera before
 
and we were talking off camera before
this like 3.js is a great example of
 
this like 3.js is a great example of
this. Like 3.js makes a lot of things
 
this. Like 3.js makes a lot of things
possible that weren't before, but
 
possible that weren't before, but
there's still all these like rough edges
 
there's still all these like rough edges
that like just a coding agent doesn't
 
that like just a coding agent doesn't
solve. And so you need like, you know,
 
solve. And so you need like, you know,
sprite generation and like the models
 
sprite generation and like the models
aren't very good at doing that natively.
 
aren't very good at doing that natively.
And so you need like some orchestration
 
And so you need like some orchestration
layer and tooling in order to make that
 
layer and tooling in order to make that
happen. There's a bunch of other things
 
happen. There's a bunch of other things
like that that like are core to like the
 
like that that like are core to like the
gaming video game experience
 
gaming video game experience
that need to have a high degree of
 
that need to have a high degree of
reliability that I think it feels like
 
reliability that I think it feels like
it's within reach, but actually like
 
it's within reach, but actually like
requires a lot of like product
 
requires a lot of like product
scaffolding work in order to create
 
scaffolding work in order to create
experiences that are like reusable and
 
experiences that are like reusable and
replayable and sort of like have the
 
replayable and sort of like have the
level of depth and requires a little bit
 
level of depth and requires a little bit
of taste in there.
 
of taste in there.
Um
 
Um
&gt;&gt; Do you see people making a lot of video
 
&gt;&gt; Do you see people making a lot of video
games inside AI studio and the other
 
games inside AI studio and the other
developer surfaces that you have?
 
developer surfaces that you have?
&gt;&gt; Yeah, and so this was actually based on
 
&gt;&gt; Yeah, and so this was actually based on
like us looking at the early data and
 
like us looking at the early data and
there was something like in AI studio at
 
there was something like in AI studio at
the time it was like 20% of all apps
 
the time it was like 20% of all apps
that folks were making were actually
 
that folks were making were actually
games. Like people were trying to build
 
games. Like people were trying to build
games. A lot of it
 
games. A lot of it
&gt;&gt; Is that the most popular category?
 
&gt;&gt; Is that the most popular category?
&gt;&gt; It's not the most popular category
 
&gt;&gt; It's not the most popular category
anymore just cuz I think like the the
 
anymore just cuz I think like the the
ecosystem has shifted and like the user
 
ecosystem has shifted and like the user
base has has shifted, but it is a lot of
 
base has has shifted, but it is a lot of
a lot of games. Um
 
a lot of games. Um
&gt;&gt; What is the most popular category?
 
&gt;&gt; What is the most popular category?
&gt;&gt; I think it was like it's like 20% like
 
&gt;&gt; I think it was like it's like 20% like
finance related stuff, 20%
 
finance related stuff, 20%
&gt;&gt; like counting their money that much.
 
&gt;&gt; like counting their money that much.
&gt;&gt; People like I think it's it's something
 
&gt;&gt; People like I think it's it's something
around crypto actually. I think it's
 
around crypto actually. I think it's
what people are doing a lot of stuff
 
what people are doing a lot of stuff
with uh with finance. A lot of like
 
with uh with finance. A lot of like
personal productivity things and a lot
 
personal productivity things and a lot
of gen media stuff actually because
 
of gen media stuff actually because
obviously the Google suite of gen media
 
obviously the Google suite of gen media
stuff has Yeah, has done a great job.
 
stuff has Yeah, has done a great job.
Um
 
Um
But I also think GDM has sort of like a
 
But I also think GDM has sort of like a
obviously Demis cares a ton about games
 
obviously Demis cares a ton about games
and sort of like started his career in
 
and sort of like started his career in
doing AI stuff because of games.
 
doing AI stuff because of games.
Um and so I think we'll we'll have some
 
Um and so I think we'll we'll have some
interesting swings at this and
 
interesting swings at this and
um our team actually in in Kaggle, which
 
um our team actually in in Kaggle, which
is sort of a bunch of the AI
 
is sort of a bunch of the AI
benchmarking stuff we do in GDM, sort of
 
benchmarking stuff we do in GDM, sort of
works with GDM to build this uh game
 
works with GDM to build this uh game
arena, which is uh sort of our way of
 
arena, which is uh sort of our way of
sort of like testing
 
sort of like testing
progress towards AGI, like using games
 
progress towards AGI, like using games
as a proxy, which again is like very
 
as a proxy, which again is like very
deeply rooted in in GDM's uh history.
 
deeply rooted in in GDM's uh history.
So.
 
So.
&gt;&gt; How close do you think we are to, you
 
&gt;&gt; How close do you think we are to, you
know, rando off the street with a good
 
know, rando off the street with a good
idea can vibe code a really fun playable
 
idea can vibe code a really fun playable
game?
 
game?
&gt;&gt; I want to say this year. I actually I
 
&gt;&gt; I want to say this year. I actually I
think it's I think the model capability
 
think it's I think the model capability
makes it possible. I think this is where
 
makes it possible. I think this is where
like I've gotten excited on the product
 
like I've gotten excited on the product
side and what you know, we were again we
 
side and what you know, we were again we
were also talking off camera about sort
 
were also talking off camera about sort
of like the startups in this ecosystem
 
of like the startups in this ecosystem
because
 
because
um it feels like it's possible. It
 
um it feels like it's possible. It
doesn't feel like there's a gap in model
 
doesn't feel like there's a gap in model
quality. It feels like there's a gap in
 
quality. It feels like there's a gap in
like you someone who knows what it takes
 
like you someone who knows what it takes
to build a great game actually like
 
to build a great game actually like
putting the scaffolding together in the
 
putting the scaffolding together in the
right way to make that possible. I think
 
right way to make that possible. I think
there are folks who are doing this right
 
there are folks who are doing this right
now and so um some of it is like a
 
now and so um some of it is like a
discoverability and awareness thing that
 
discoverability and awareness thing that
like people just don't even know that
 
like people just don't even know that
they can do that. Um and some of it is
 
they can do that. Um and some of it is
just like
 
just like
maybe certain categories of model
 
maybe certain categories of model
capabilities are just like slightly off
 
capabilities are just like slightly off
and we're like, you know, weeks or
 
and we're like, you know, weeks or
months away from like that chasm being
 
months away from like that chasm being
crossed and then it just like working
 
crossed and then it just like working
for most people.
 
for most people.
&gt;&gt; And so this is a good segue into when
 
&gt;&gt; And so this is a good segue into when
I'll ask you about world models next,
 
I'll ask you about world models next,
but do you think vibe code of video
 
but do you think vibe code of video
games is more likely um
 
games is more likely um
going to be, you know, game engine plus
 
going to be, you know, game engine plus
coding agents based or do you think it's
 
coding agents based or do you think it's
more likely to be world model based?
 
more likely to be world model based?
&gt;&gt; Yeah, I think the what will end up
 
&gt;&gt; Yeah, I think the what will end up
happening is the definition of world
 
happening is the definition of world
models will blur, which we should talk
 
models will blur, which we should talk
which we should talk about with Omni. Um
 
which we should talk about with Omni. Um
and
 
and
it will still
 
it will still
I think the like coding agents will look
 
I think the like coding agents will look
like some sort of world model type
 
like some sort of world model type
system.
 
system.
Um but you actually do need
 
Um but you actually do need
to make world models useful for like
 
to make world models useful for like
real things, you need like scaffolding.
 
real things, you need like scaffolding.
Um and so I think there's again there's
 
Um and so I think there's again there's
actually a bunch of interesting startups
 
actually a bunch of interesting startups
like doing work like figuring out what
 
like doing work like figuring out what
is the scaffolding for world models so
 
is the scaffolding for world models so
that you can take them from these like
 
that you can take them from these like
very open-ended inherent design of world
 
very open-ended inherent design of world
models very open-ended spaces and like
 
models very open-ended spaces and like
do it in a tangible way so that it's
 
do it in a tangible way so that it's
like grounded in a use case that like
 
like grounded in a use case that like
you could use in a reoccurring way. And
 
you could use in a reoccurring way. And
that could be somebody maybe will figure
 
that could be somebody maybe will figure
out the scaffolding for world models to
 
out the scaffolding for world models to
make games possible but like the
 
make games possible but like the
inherent nature of world models right
 
inherent nature of world models right
now I think make it so that it's like
 
now I think make it so that it's like
actually not well suited for
 
actually not well suited for
like games in their current form but the
 
like games in their current form but the
progress has been crazy so who knows
 
progress has been crazy so who knows
maybe in like two years the the versions
 
maybe in like two years the the versions
will be able to but at least in the
 
will be able to but at least in the
short term it's like coding agent plus
 
short term it's like coding agent plus
some sort of game engine I think is like
 
some sort of game engine I think is like
where you'll see way more alpha from a a
 
where you'll see way more alpha from a a
games perspective.
 
games perspective.
&gt;&gt; That makes sense. Okay so you said the
 
&gt;&gt; That makes sense. Okay so you said the
definitions of world models are blurry.
 
definitions of world models are blurry.
Can we unpack that?
 
Can we unpack that?
&gt;&gt; Yeah I mean I think like Omni is a is an
 
&gt;&gt; Yeah I mean I think like Omni is a is an
example of this you know we launched
 
example of this you know we launched
this at IO you can sort of taken any
 
this at IO you can sort of taken any
input create any output
 
input create any output
um and I think Demis sort of like framed
 
um and I think Demis sort of like framed
it to the world
 
it to the world
uh rightfully so as as a world model
 
uh rightfully so as as a world model
because of just like the level of
 
because of just like the level of
understanding that it has of the world.
 
understanding that it has of the world.
I think that like technically looks
 
I think that like technically looks
different than
 
different than
um and I'm I'm not an architecture
 
um and I'm I'm not an architecture
expert on like the way that they we've
 
expert on like the way that they we've
done world models before but it is
 
done world models before but it is
different from an architectural
 
different from an architectural
standpoint than what's happened in the
 
standpoint than what's happened in the
past
 
past
um
 
um
which I think is positive because it's
 
which I think is positive because it's
getting closer to like some of the ways
 
getting closer to like some of the ways
in which it might actually be more
 
in which it might actually be more
scalable
 
scalable
and historically like it's been like
 
and historically like it's been like
super not scalable. It's like very very
 
super not scalable. It's like very very
expensive to run
 
expensive to run
&gt;&gt; Yeah.
 
&gt;&gt; Yeah.
&gt;&gt; traditional like online world models.
 
&gt;&gt; traditional like online world models.
&gt;&gt; Genie being like yeah okay so if you
 
&gt;&gt; Genie being like yeah okay so if you
think of traditional world models as
 
think of traditional world models as
being like an action conditions video
 
being like an action conditions video
model almost
 
model almost
&gt;&gt; Yeah.
 
&gt;&gt; Yeah.
&gt;&gt; then like
 
&gt;&gt; then like
right now what we're when we when we say
 
right now what we're when we when we say
world model what we actually mean is
 
world model what we actually mean is
a model that has some understanding of
 
a model that has some understanding of
the world as opposed to being strictly
 
the world as opposed to being strictly
technically a action condition video
 
technically a action condition video
model.
 
model.
&gt;&gt; Yeah and and so the interesting thing
 
&gt;&gt; Yeah and and so the interesting thing
though is like it has understanding of
 
though is like it has understanding of
the world but then it also has that like
 
the world but then it also has that like
really great and that's where like the
 
really great and that's where like the
line is blurry to me where it's like it
 
line is blurry to me where it's like it
can do a lot of those same use case It's
 
can do a lot of those same use case It's
not real-time right now, but like it can
 
not real-time right now, but like it can
do a lot of those same use cases that
 
do a lot of those same use cases that
you would describe or like
 
you would describe or like
visually could create with that same
 
visually could create with that same
exact world model, which I think is
 
exact world model, which I think is
what's most interesting to me. So, I do
 
what's most interesting to me. So, I do
feel like this like world model video
 
feel like this like world model video
model thing is going to is going to
 
model thing is going to is going to
change and play out in a in a different
 
change and play out in a in a different
way than was obvious before.
 
way than was obvious before.
&gt;&gt; And how does it work under the hood?
 
&gt;&gt; And how does it work under the hood?
Like whatever you're able to share? Like
 
Like whatever you're able to share? Like
is it Gemini plus video models? Is it
 
is it Gemini plus video models? Is it
something different entirely?
 
something different entirely?
&gt;&gt; It is It is a single model, which I
 
&gt;&gt; It is It is a single model, which I
think is the important part. Like this
 
think is the important part. Like this
was actually part of the original desire
 
was actually part of the original desire
was like
 
was like
you were training like eight different
 
you were training like eight different
models to do all of those things
 
models to do all of those things
historically. It's like you have a text
 
historically. It's like you have a text
model with the baseline Gemini model.
 
model with the baseline Gemini model.
You have audio, you have music models
 
You have audio, you have music models
with Lyria, you have Nano Banana, you
 
with Lyria, you have Nano Banana, you
have VO video models, you have a We have
 
have VO video models, you have a We have
a whole suite of audio models and like
 
a whole suite of audio models and like
it would be great for us, our customers,
 
it would be great for us, our customers,
um if you just had a single model to do
 
um if you just had a single model to do
all those things. So, it is like a a new
 
all those things. So, it is like a a new
setup that sort of makes that possible.
 
setup that sort of makes that possible.
Um it's not like routing to a bunch of
 
Um it's not like routing to a bunch of
different models, which like we You
 
different models, which like we You
could have imagined we could have done
 
could have imagined we could have done
something like that actually before and
 
something like that actually before and
done like a Gemini Omni model, but this
 
done like a Gemini Omni model, but this
is like a true Omni model. Um and it's
 
is like a true Omni model. Um and it's
starting with like the the use case that
 
starting with like the the use case that
works the best right now, which is the
 
works the best right now, which is the
why it's the one that's available. Um is
 
why it's the one that's available. Um is
this like video editing capability. Um
 
this like video editing capability. Um
the Technically, it's like functional
 
the Technically, it's like functional
with the other things. It's just like
 
with the other things. It's just like
the quality isn't isn't like perfect um
 
the quality isn't isn't like perfect um
and is not state-of-the-art. So, we we
 
and is not state-of-the-art. So, we we
haven't rolled that out yet. Um it's
 
haven't rolled that out yet. Um it's
also just like the first
 
also just like the first
crank of the model turn on Omni. It's
 
crank of the model turn on Omni. It's
the Omni Flash model, the first
 
the Omni Flash model, the first
iteration.
 
iteration.
Um and so, we'll have like much, much
 
Um and so, we'll have like much, much
more capable, uh powerful versions,
 
more capable, uh powerful versions,
which will be which will be exciting to
 
which will be which will be exciting to
see.
 
see.
&gt;&gt; Mhm.
 
&gt;&gt; Mhm.
So, we could edit this set so it looks
 
So, we could edit this set so it looks
like we're
 
like we're
&gt;&gt; Yes. Yeah, yeah. We I I want this we
 
&gt;&gt; Yes. Yeah, yeah. We I I want this we
again we were talking off camera like we
 
again we were talking off camera like we
should do that for the intro because I
 
should do that for the intro because I
think it just like makes all this stuff
 
think it just like makes all this stuff
more capable. And I've seen these
 
more capable. And I've seen these
examples of like such subtle nuance that
 
examples of like such subtle nuance that
like make me appreciate that it's like
 
like make me appreciate that it's like
the world understanding playing out. I
 
the world understanding playing out. I
was I was giving a talk um
 
was I was giving a talk um
and was on stage with with my friend
 
and was on stage with with my friend
Tulsi who leads the model team who I
 
Tulsi who leads the model team who I
don't know if you've ever had on before
 
don't know if you've ever had on before
but she's amazing. I love Tulsi.
 
but she's amazing. I love Tulsi.
Um and in I had mentioned to someone in
 
Um and in I had mentioned to someone in
the crowd to like edit the video and
 
the crowd to like edit the video and
they had literally like took the picture
 
they had literally like took the picture
edited it with Omni in real time and
 
edited it with Omni in real time and
this like dog came on the stage uh and
 
this like dog came on the stage uh and
like the other in the edited version the
 
like the other in the edited version the
other guests sort of like looked down
 
other guests sort of like looked down
and see the dog they like chuckle a
 
and see the dog they like chuckle a
little bit. This is while I'm like
 
little bit. This is while I'm like
opining about whatever
 
opining about whatever
&gt;&gt; They were laughing at your jokes.
 
&gt;&gt; They were laughing at your jokes.
&gt;&gt; Yeah, that it was not my jokes. They
 
&gt;&gt; Yeah, that it was not my jokes. They
they [laughter] laugh at the dog coming
 
they [laughter] laugh at the dog coming
up. It jumps onto my lap. I sort of like
 
up. It jumps onto my lap. I sort of like
acknowledge the dog. I keep talking. I'm
 
acknowledge the dog. I keep talking. I'm
like petting it or whatever. And just
 
like petting it or whatever. And just
like there's like so much subtle subtle
 
like there's like so much subtle subtle
tea and getting that right and the model
 
tea and getting that right and the model
crushed it. And it's just it it is very
 
crushed it. And it's just it it is very
interesting and like still trying to
 
interesting and like still trying to
like absorb and digest like what that
 
like absorb and digest like what that
means for you know, the way we make
 
means for you know, the way we make
content and all these other things.
 
content and all these other things.
&gt;&gt; That's so interesting.
 
&gt;&gt; That's so interesting.
&gt;&gt; Yeah.
 
&gt;&gt; Yeah.
&gt;&gt; I'm I'm the biggest bull on generative
 
&gt;&gt; I'm I'm the biggest bull on generative
media and what it means and I mean one
 
media and what it means and I mean one
of the things we've thought about for
 
of the things we've thought about for
our podcast is the visuals matter as
 
our podcast is the visuals matter as
much as the content.
 
much as the content.
&gt;&gt; For sure.
 
&gt;&gt; For sure.
&gt;&gt; Um that's how you catch people's
 
&gt;&gt; Um that's how you catch people's
attention in the first place, right? And
 
attention in the first place, right? And
and so okay, I'm excited to I'm excited
 
and so okay, I'm excited to I'm excited
to play with Omni.
 
to play with Omni.
&gt;&gt; I'm excited too and I think the and and
 
&gt;&gt; I'm excited too and I think the and and
I think you probably feel this way as
 
I think you probably feel this way as
somebody who makes content but I've
 
somebody who makes content but I've
historically like been like very for
 
historically like been like very for
myself personally like I don't use AI to
 
myself personally like I don't use AI to
make any of content that I produce like
 
make any of content that I produce like
it's all my words, it's always my voice,
 
it's all my words, it's always my voice,
it's always my image and picture showing
 
it's always my image and picture showing
up. Like I just I I feel like there's
 
up. Like I just I I feel like there's
just like so much alpha and
 
just like so much alpha and
authenticity. And so like I would much
 
authenticity. And so like I would much
rather it be me than some AI version of
 
rather it be me than some AI version of
me. What I like so much about Omni is
 
me. What I like so much about Omni is
that it's like not changing me. Um it is
 
that it's like not changing me. Um it is
like changing a bunch of these other
 
like changing a bunch of these other
bits which are not me. Like I didn't
 
bits which are not me. Like I didn't
choose any of the like set around us or
 
choose any of the like set around us or
the the coffee table. It's like so our
 
the the coffee table. It's like so our
our words can stay the same and like you
 
our words can stay the same and like you
can change these bits that are like not
 
can change these bits that are like not
personal um and do something more
 
personal um and do something more
interesting with them which I think is
 
interesting with them which I think is
really really cool and feels
 
really really cool and feels
it feels like the version of what I want
 
it feels like the version of what I want
sort of like Gen media to be which is
 
sort of like Gen media to be which is
like not a bunch of like AI avatars. Uh
 
like not a bunch of like AI avatars. Uh
it's like
 
it's like
&gt;&gt; island videos?
 
&gt;&gt; island videos?
&gt;&gt; Exactly. Truly. Like it really is like
 
&gt;&gt; Exactly. Truly. Like it really is like
it's the original content. It's the
 
it's the original content. It's the
person. It's like the personhood is
 
person. It's like the personhood is
there. It's just
 
there. It's just
different and amplified.
 
different and amplified.
&gt;&gt; Super interesting. Okay, I'm excited to
 
&gt;&gt; Super interesting. Okay, I'm excited to
play with it.
 
play with it.
&gt;&gt; Yeah, we should we should
 
&gt;&gt; Yeah, we should we should
send some prompts right after this and
 
send some prompts right after this and
try some things.
 
try some things.
&gt;&gt; mind the fruit videos though. I'm I'm
 
&gt;&gt; mind the fruit videos though. I'm I'm
I'm happy for a world [laughter] of of
 
I'm happy for a world [laughter] of of
both.
 
both.
Um on the coding side, you launched the
 
Um on the coding side, you launched the
ability in AI studio for people to write
 
ability in AI studio for people to write
code Android apps.
 
code Android apps.
&gt;&gt; Yeah, yeah.
 
&gt;&gt; Yeah, yeah.
&gt;&gt; Um I'd love to you know hear how that's
 
&gt;&gt; Um I'd love to you know hear how that's
going so far and and where you plan to
 
going so far and and where you plan to
take that.
 
take that.
&gt;&gt; Yeah, it's super exciting. I think one
 
&gt;&gt; Yeah, it's super exciting. I think one
of the strategic things for AI studio
 
of the strategic things for AI studio
and actually this is based on like a lot
 
and actually this is based on like a lot
of the feedback from the ecosystem and
 
of the feedback from the ecosystem and
actually from developers, from others is
 
actually from developers, from others is
like so many Google products. Um there's
 
like so many Google products. Um there's
so many different like ways in which you
 
so many different like ways in which you
like touch Google through all these
 
like touch Google through all these
different journeys of building a startup
 
different journeys of building a startup
or bringing idea to your life. And so
 
or bringing idea to your life. And so
um we have this like first class
 
um we have this like first class
principle of like how do we bring
 
principle of like how do we bring
things into AI studio that make it so
 
things into AI studio that make it so
that you are exposed to other parts of
 
that you are exposed to other parts of
the Google ecosystem without having to
 
the Google ecosystem without having to
like go through nine different UIs
 
like go through nine different UIs
across Google. Um and so Androids are
 
across Google. Um and so Androids are
like a great example um not only of that
 
like a great example um not only of that
but also of
 
but also of
enabling people who wouldn't have
 
enabling people who wouldn't have
otherwise built an Android app. And so I
 
otherwise built an Android app. And so I
literally built my first Android app in
 
literally built my first Android app in
AI studio. Um very cool to see. It's uh
 
AI studio. Um very cool to see. It's uh
&gt;&gt; What is it?
 
&gt;&gt; What is it?
&gt;&gt; Yeah, I I just did like a a plant not a
 
&gt;&gt; Yeah, I I just did like a a plant not a
crypto app. Just a a plant one. I was
 
crypto app. Just a a plant one. I was
planting trees in my backyard.
 
planting trees in my backyard.
&gt;&gt; app. That's cool.
 
&gt;&gt; app. That's cool.
&gt;&gt; Yeah, and so it was just like playing
 
&gt;&gt; Yeah, and so it was just like playing
around with the a gardening app as I as
 
around with the a gardening app as I as
I was kicking the tires.
 
I was kicking the tires.
Um I haven't had my like breakthrough
 
Um I haven't had my like breakthrough
idea yet of what I want for a mobile
 
idea yet of what I want for a mobile
app, but I'm going to I'm going to come
 
app, but I'm going to I'm going to come
up with something and see go compete on
 
up with something and see go compete on
the App Store.
 
the App Store.
&gt;&gt; Have you seen anything by coded like
 
&gt;&gt; Have you seen anything by coded like
really flying in the App Store yet?
 
really flying in the App Store yet?
&gt;&gt; That's a good It'd actually be
 
&gt;&gt; That's a good It'd actually be
interesting to like see some analysis. I
 
interesting to like see some analysis. I
don't know I'm sure it's like
 
don't know I'm sure it's like
accelerating a lot of things on the App
 
accelerating a lot of things on the App
Store, but I don't know how much. Like I
 
Store, but I don't know how much. Like I
don't know anyone like personally who's
 
don't know anyone like personally who's
who's done that.
 
who's done that.
&gt;&gt; Yeah.
 
&gt;&gt; Yeah.
&gt;&gt; It is interesting and I was going to
 
&gt;&gt; It is interesting and I was going to
make the observation too that I think
 
make the observation too that I think
the last time I checked the numbers we
 
the last time I checked the numbers we
were viewing it this morning, it was
 
were viewing it this morning, it was
like 350,000
 
like 350,000
Android apps built in AI Studio since
 
Android apps built in AI Studio since
last week, which is crazy.
 
last week, which is crazy.
Um
 
Um
and like excitingly it's like 350,000
 
and like excitingly it's like 350,000
apps that like probably no one was going
 
apps that like probably no one was going
to build before. A lot of these are
 
to build before. A lot of these are
personal, too. And so this is where I
 
personal, too. And so this is where I
think this like maybe Gen Y is like
 
think this like maybe Gen Y is like
farther out there, but I think like the
 
farther out there, but I think like the
idea of you building software
 
idea of you building software
to solve your personal problem is like
 
to solve your personal problem is like
very real right now. And like people are
 
very real right now. And like people are
doing that. It's like one of the most
 
doing that. It's like one of the most
common use cases of a lot of these
 
common use cases of a lot of these
products.
 
products.
Um and being able to like unlock a bunch
 
Um and being able to like unlock a bunch
of the native capabilities of the phone
 
of the native capabilities of the phone
I think is also really interesting cuz
 
I think is also really interesting cuz
you just have so much context that's
 
you just have so much context that's
like in different places.
 
like in different places.
Um
 
Um
so I'm I'm getting very excited about
 
so I'm I'm getting very excited about
sort of that opportunity and uh Android
 
sort of that opportunity and uh Android
feels like it's becoming the the
 
feels like it's becoming the the
platform for builders.
 
platform for builders.
&gt;&gt; Does it matter that something is an app
 
&gt;&gt; Does it matter that something is an app
versus just like the web is so powerful
 
versus just like the web is so powerful
now?
 
now?
&gt;&gt; The yeah, that is It's also very
 
&gt;&gt; The yeah, that is It's also very
interesting to see that play out. Web is
 
interesting to see that play out. Web is
definitely powerful. There are certain
 
definitely powerful. There are certain
things that the operating systems have
 
things that the operating systems have
that like you just can't unlock. Um like
 
that like you just can't unlock. Um like
lots of like native richness that
 
lots of like native richness that
actually like make experiences feel so
 
actually like make experiences feel so
much richer. I think about this for like
 
much richer. I think about this for like
text messaging actually that like the
 
text messaging actually that like the
text messaging experience in all of the
 
text messaging experience in all of the
in all the main operating systems feel
 
in all the main operating systems feel
way richer to me than like any AI chat
 
way richer to me than like any AI chat
app that I've ever used. Like if I could
 
app that I've ever used. Like if I could
just talk to AI in whatever texting app
 
just talk to AI in whatever texting app
I use, like I would be way happier than
 
I use, like I would be way happier than
having to go to some other app.
 
having to go to some other app.
Um because I think we're also just like
 
Um because I think we're also just like
conditioned on like the operating
 
conditioned on like the operating
systems, so.
 
systems, so.
&gt;&gt; Yeah, makes sense. Okay, I want to ask
 
&gt;&gt; Yeah, makes sense. Okay, I want to ask
about the model eats the harness or the
 
about the model eats the harness or the
model eats the scaffolding. What are
 
model eats the scaffolding. What are
your thoughts?
 
your thoughts?
&gt;&gt; Yeah, I think it's true and I think part
 
&gt;&gt; Yeah, I think it's true and I think part
of this is like
 
of this is like
what we
 
what we
have historically thought of as the
 
have historically thought of as the
model is not the model anymore. Like
 
model is not the model anymore. Like
when you I think like two years ago when
 
when you I think like two years ago when
LLMs were popular, it was like the model
 
LLMs were popular, it was like the model
was like actually just a set of weights.
 
was like actually just a set of weights.
Um it was a set of weights and it was
 
Um it was a set of weights and it was
like really like how can you like as
 
like really like how can you like as
simple as possible send tokens in and
 
simple as possible send tokens in and
get tokens out. And I think we've just
 
get tokens out. And I think we've just
like progressively step by step by step.
 
like progressively step by step by step.
We still call it the model, we still
 
We still call it the model, we still
call it you know Gemini 3.5, you still
 
call it you know Gemini 3.5, you still
call it GPT whatever and and Claude
 
call it GPT whatever and and Claude
whatever, but like
 
whatever, but like
it's actually not just the weights
 
it's actually not just the weights
anymore. It's like an entire expre-
 
anymore. It's like an entire expre-
expanding sprawling system that's built
 
expanding sprawling system that's built
around the weights um that's sort of
 
around the weights um that's sort of
like enable a lot of these like next
 
like enable a lot of these like next
generation experiences from agentic tool
 
generation experiences from agentic tool
calling to tool you know like all these
 
calling to tool you know like all these
hosted tools, search, code execution,
 
hosted tools, search, code execution,
etc.
 
etc.
Um you know the models are now being
 
Um you know the models are now being
spun up in containers and sort of have
 
spun up in containers and sort of have
an agent harness and all that stuff. So,
 
an agent harness and all that stuff. So,
the scaffolding is like often times a
 
the scaffolding is like often times a
couple of steps ahead of like where the
 
couple of steps ahead of like where the
what is like baked directly into the
 
what is like baked directly into the
model. And then what ends up happening
 
model. And then what ends up happening
is like the model eats that scaffolding
 
is like the model eats that scaffolding
and it becomes part of like the native
 
and it becomes part of like the native
model system. And there's still value in
 
model system. And there's still value in
having sort of
 
having sort of
the external scaffolding in certain
 
the external scaffolding in certain
cases and like search maybe is an
 
cases and like search maybe is an
example of this. Like there's lots of
 
example of this. Like there's lots of
folks who use different search providers
 
folks who use different search providers
and there's different like use cases
 
and there's different like use cases
that you want. And so like sure, maybe
 
that you want. And so like sure, maybe
the model can natively use search, but
 
the model can natively use search, but
you also want something else. Code
 
you also want something else. Code
execution is another example of that. Um
 
execution is another example of that. Um
but it does feel like
 
but it does feel like
like maybe the agent harness is like the
 
like maybe the agent harness is like the
quintessential example of this right now
 
quintessential example of this right now
where like everyone's like ah we got to
 
where like everyone's like ah we got to
go build a harness and like the harness
 
go build a harness and like the harness
is where the alpha is, and like I think
 
is where the alpha is, and like I think
that perhaps won't be true at least in
 
that perhaps won't be true at least in
the way that we think of the harness
 
the way that we think of the harness
today in 12 months. I think the models
 
today in 12 months. I think the models
will have sort of just like digested a
 
will have sort of just like digested a
bunch of that. It'll be upstreamed into
 
bunch of that. It'll be upstreamed into
the model, um and the alpha will be
 
the model, um and the alpha will be
somewhere else now. It won't be in sort
 
somewhere else now. It won't be in sort
of trying to spin your own harness cuz
 
of trying to spin your own harness cuz
the model just like does it natively.
 
the model just like does it natively.
&gt;&gt; But I thought that the part of the
 
&gt;&gt; But I thought that the part of the
reason why people are building their own
 
reason why people are building their own
harnesses is because if you use a
 
harnesses is because if you use a
harness from any given model provider,
 
harness from any given model provider,
you're locked in, right? So, a lot of
 
you're locked in, right? So, a lot of
the application companies want
 
the application companies want
flexibility, which is why they're
 
flexibility, which is why they're
building their own harnesses.
 
building their own harnesses.
&gt;&gt; Yeah, and I think that's part of the
 
&gt;&gt; Yeah, and I think that's part of the
scaffolding story is like that starts
 
scaffolding story is like that starts
out perhaps true, but then as the model
 
out perhaps true, but then as the model
capability improves, like it it becomes
 
capability improves, like it it becomes
less true over time actually. I think
 
less true over time actually. I think
the model the like you you don't have a
 
the model the like you you don't have a
generalized model if it can't use
 
generalized model if it can't use
another harness. And so, it is it is
 
another harness. And so, it is it is
important to deny I mentioned this uh in
 
important to deny I mentioned this uh in
another conversation with someone a few
 
another conversation with someone a few
weeks ago, but we need something like
 
weeks ago, but we need something like
harness bench, which is like actually
 
harness bench, which is like actually
measuring like how good are all these
 
measuring like how good are all these
different models at adapting to all the
 
different models at adapting to all the
different harnesses. I feel like that
 
different harnesses. I feel like that
seems like a reasonable thing we should
 
seems like a reasonable thing we should
we should measure as an ecosystem. Um
 
we should measure as an ecosystem. Um
and I'd be curious to see like what
 
and I'd be curious to see like what
models are actually best, but
 
models are actually best, but
I think over time you expect they they'd
 
I think over time you expect they they'd
be able to use every harness. Um unless
 
be able to use every harness. Um unless
you're like completely out of
 
you're like completely out of
distribution, which in that case like
 
distribution, which in that case like
you're still going to be completely out
 
you're still going to be completely out
of distribution even if you're using
 
of distribution even if you're using
your own harness. So, not sure it
 
your own harness. So, not sure it
matters much.
 
matters much.
&gt;&gt; Fair enough. What about the application
 
&gt;&gt; Fair enough. What about the application
layer? How do you think about where
 
layer? How do you think about where
independent companies uh can, you know,
 
independent companies uh can, you know,
have a hope of surviving when the model
 
have a hope of surviving when the model
eats the harness and eats, you know, the
 
eats the harness and eats, you know, the
stuff around it?
 
stuff around it?
&gt;&gt; Yeah, it feels like there's so Yeah, it
 
&gt;&gt; Yeah, it feels like there's so Yeah, it
is an interesting story that like both
 
is an interesting story that like both
of these things feel true. Both on one
 
of these things feel true. Both on one
hand I everywhere I look, I'm like
 
hand I everywhere I look, I'm like
there's never been more opportunity to
 
there's never been more opportunity to
go and build something. At the same
 
go and build something. At the same
time, obviously the models are doing
 
time, obviously the models are doing
more than they've ever done before. Um I
 
more than they've ever done before. Um I
think there's like, you know, there's
 
think there's like, you know, there's
that threat of capability overhang,
 
that threat of capability overhang,
which I think there's a huge amount of
 
which I think there's a huge amount of
alpha in. There's the threat of the
 
alpha in. There's the threat of the
model companies are like going after
 
model companies are like going after
these like very general problems um and
 
these like very general problems um and
there's just like so much
 
there's just like so much
value in these like verticalized
 
value in these like verticalized
domains. If you have expertise in that
 
domains. If you have expertise in that
domain, you sort of like know the
 
domain, you sort of like know the
customers, you know the ecosystem, like
 
customers, you know the ecosystem, like
it's just you can really like run laps
 
it's just you can really like run laps
around even the best model labs because
 
around even the best model labs because
like focus is the like superpower of
 
like focus is the like superpower of
startups. Like if you can focus, you can
 
startups. Like if you can focus, you can
do anything
 
do anything
and if you look at all of the companies
 
and if you look at all of the companies
that are big or doing lots of stuff like
 
that are big or doing lots of stuff like
there's just not a lot of focus and for
 
there's just not a lot of focus and for
some for some reasons like rightfully so
 
some for some reasons like rightfully so
because yeah, maybe I'm I'm overly
 
because yeah, maybe I'm I'm overly
justifying, you know, Google strategy be
 
justifying, you know, Google strategy be
like we just have a lot of products. We
 
like we just have a lot of products. We
have a lot of users. We have a lot of
 
have a lot of users. We have a lot of
different things going on and so like we
 
different things going on and so like we
actually can't focus in one domain. We
 
actually can't focus in one domain. We
have an obligation to do a bunch of
 
have an obligation to do a bunch of
things as a big company.
 
things as a big company.
I think that's not true for startups and
 
I think that's not true for startups and
so I think like 24 months ago we were
 
so I think like 24 months ago we were
all asking ourselves like oh, wow, it
 
all asking ourselves like oh, wow, it
seems like the it seems like the
 
seems like the it seems like the
opportunity space is shifting and maybe
 
opportunity space is shifting and maybe
it's it's possible one of the outcomes
 
it's it's possible one of the outcomes
is there's less opportunity for startups
 
is there's less opportunity for startups
in the future. That feels like so far in
 
in the future. That feels like so far in
a way not what has ended up playing out
 
a way not what has ended up playing out
which is really positive. If anything it
 
which is really positive. If anything it
feels like there's just even more
 
feels like there's just even more
opportunity than there was. Like now
 
opportunity than there was. Like now
coding has helped you like close the gap
 
coding has helped you like close the gap
on like larger companies that have like
 
on like larger companies that have like
established code bases and all this
 
established code bases and all this
other stuff because you can just like
 
other stuff because you can just like
run way faster and write software
 
run way faster and write software
quicker.
 
quicker.
The agentic like primitive is like a new
 
The agentic like primitive is like a new
category that you can sort of build
 
category that you can sort of build
products around that like actually in a
 
products around that like actually in a
lot of cases to the conversation about
 
lot of cases to the conversation about
like the risks involved with building.
 
like the risks involved with building.
Like there's risk involved and so like
 
Like there's risk involved and so like
what's your like the risk appetite of
 
what's your like the risk appetite of
different companies is different. And so
 
different companies is different. And so
if you're willing to take more risk in
 
if you're willing to take more risk in
some domains like you can win a user
 
some domains like you can win a user
cohort who's like interested in also
 
cohort who's like interested in also
taking risk. There's so much
 
taking risk. There's so much
opportunity.
 
opportunity.
&gt;&gt; Awesome. I'd love to talk about Google
 
&gt;&gt; Awesome. I'd love to talk about Google
DeepMind's culture and I'm curious what
 
DeepMind's culture and I'm curious what
does it feel like to be inside GDM right
 
does it feel like to be inside GDM right
now? You know, we we had Demis at AI
 
now? You know, we we had Demis at AI
Sense. He was so inspiring. I've heard
 
Sense. He was so inspiring. I've heard
Sergey's back. I've you guys have Noam
 
Sergey's back. I've you guys have Noam
Shazeer back. Like
 
Shazeer back. Like
walk me through what it's like to be at
 
walk me through what it's like to be at
GDM right now.
 
GDM right now.
&gt;&gt; It's incredible. I do try to take it all
 
&gt;&gt; It's incredible. I do try to take it all
in because it is like a it's like a
 
in because it is like a it's like a
moment. I I try to reflect as much as
 
moment. I I try to reflect as much as
possible in the in the chaos of all the
 
possible in the in the chaos of all the
things that are happening just because
 
things that are happening just because
there's like so much cool stuff going
 
there's like so much cool stuff going
on. Um
 
on. Um
GDM's culture is interesting and like
 
GDM's culture is interesting and like
maybe three observations. One, back to
 
maybe three observations. One, back to
this thread of like focus, we're doing a
 
this thread of like focus, we're doing a
lot of things. And so I think you see
 
lot of things. And so I think you see
sort of
 
sort of
I I think about this a lot. Like from a
 
I I think about this a lot. Like from a
portfolio perspective, I think we have
 
portfolio perspective, I think we have
like one of the strongest portfolios
 
like one of the strongest portfolios
which is really exciting. But you do see
 
which is really exciting. But you do see
these moments where like another lab or
 
these moments where like another lab or
another company, whatever it is, will
 
another company, whatever it is, will
like pull ahead in a certain area where
 
like pull ahead in a certain area where
like we under invested, just like hadn't
 
like we under invested, just like hadn't
been focused enough in that domain.
 
been focused enough in that domain.
Um
 
Um
and it's cool to see like the the way we
 
and it's cool to see like the the way we
go about trying to like close that gap.
 
go about trying to like close that gap.
I very much I very much appreciate it.
 
I very much I very much appreciate it.
Um I think I've I've watched the Demis
 
Um I think I've I've watched the Demis
Thinking Game documentary a few times.
 
Thinking Game documentary a few times.
Um and like you see sort of like a lot
 
Um and like you see sort of like a lot
of like details of that like original
 
of like details of that like original
culture and just like the way that
 
culture and just like the way that
strikes work and all this stuff which is
 
strikes work and all this stuff which is
actually really similar today is like
 
actually really similar today is like
you just get a bunch of smart people
 
you just get a bunch of smart people
together and like go solve the problem.
 
together and like go solve the problem.
Um and I I love that and it's like very
 
Um and I I love that and it's like very
cool
 
cool
um
 
um
to to be a part of. Another one is this
 
to to be a part of. Another one is this
I think you see the culture permeate
 
I think you see the culture permeate
from like who the leaders are. Um and as
 
from like who the leaders are. Um and as
I maybe
 
I maybe
uh uh
 
uh uh
this isn't like a a perfect
 
this isn't like a a perfect
characterization of the ecosystem, but
 
characterization of the ecosystem, but
like Demis is a Nobel Prize scientist um
 
like Demis is a Nobel Prize scientist um
and like the sort of OG of a lot of this
 
and like the sort of OG of a lot of this
stuff. And sort of you feel that in the
 
stuff. And sort of you feel that in the
DeepMind culture. I think like Sam is
 
DeepMind culture. I think like Sam is
like the you know, maybe one of the
 
like the you know, maybe one of the
world's best businessman ever. And like
 
world's best businessman ever. And like
you sort of see that in the OpenAI
 
you sort of see that in the OpenAI
culture and the way that they go about
 
culture and the way that they go about
the world. I don't have a strong sense
 
the world. I don't have a strong sense
of who Dario is. Um but like I think
 
of who Dario is. Um but like I think
Anthropic is a very interesting place
 
Anthropic is a very interesting place
and you sort of I at least as an
 
and you sort of I at least as an
external observer like there he seems
 
external observer like there he seems
like an interesting guy and so
 
like an interesting guy and so
uh somewhat esoteric and so that seems
 
uh somewhat esoteric and so that seems
like they're sort of like that in the
 
like they're sort of like that in the
DNA in the culture of the company. You
 
DNA in the culture of the company. You
know, all the other labs are interesting
 
know, all the other labs are interesting
um
 
um
but I like this like very scientific
 
but I like this like very scientific
approach to the world um and the way
 
approach to the world um and the way
that like Demis looks at like
 
that like Demis looks at like
the reason he's doing this and the
 
the reason he's doing this and the
reason they started this mission was
 
reason they started this mission was
like literally to like solve disease and
 
like literally to like solve disease and
all these things and it's like so easy
 
all these things and it's like so easy
to get and again I'm always trying to
 
to get and again I'm always trying to
pull myself out of the moment but like
 
pull myself out of the moment but like
it's so easy to get lost in this like
 
it's so easy to get lost in this like
competitive race of who's
 
competitive race of who's
pushing a number higher on sweet bench
 
pushing a number higher on sweet bench
or whatever it is. It's very easy to
 
or whatever it is. It's very easy to
lose sight lose sight of like the reason
 
lose sight lose sight of like the reason
we're doing that is so that like we're
 
we're doing that is so that like we're
can solve problems that humans actually
 
can solve problems that humans actually
have and there's a
 
have and there's a
uh my my favorite quote from all of
 
uh my my favorite quote from all of
Silicon Valley is something like, you
 
Silicon Valley is something like, you
know, we can't let other people make the
 
know, we can't let other people make the
world a better place more than we can
 
world a better place more than we can
which is like what this moment feels
 
which is like what this moment feels
like
 
like
&gt;&gt; Like the Gavin Belson
 
&gt;&gt; Like the Gavin Belson
&gt;&gt; The Gavin Belson [laughter] quote and I
 
&gt;&gt; The Gavin Belson [laughter] quote and I
think about that all the time and it's
 
think about that all the time and it's
like we're all fighting over who can
 
like we're all fighting over who can
make the world better more than the
 
make the world better more than the
other person which is like at when you
 
other person which is like at when you
frame it like that it seems really goofy
 
frame it like that it seems really goofy
to me um
 
to me um
and so it's very much not zero sum um
 
and so it's very much not zero sum um
and I think that's like a
 
and I think that's like a
a way of looking at the world. I think
 
a way of looking at the world. I think
the last thing about DeepMind's culture
 
the last thing about DeepMind's culture
is like we're very we're it's sort of
 
is like we're very we're it's sort of
the engine room of Google uh which I
 
the engine room of Google uh which I
think is like literally the Twitter bio
 
think is like literally the Twitter bio
now of the the DeepMind Twitter account
 
now of the the DeepMind Twitter account
which I love um
 
which I love um
&gt;&gt; You man the DeepMind Twitter account?
 
&gt;&gt; You man the DeepMind Twitter account?
&gt;&gt; I don't. I I don't want any
 
&gt;&gt; I don't. I I don't want any
responsibility manning other people's
 
responsibility manning other people's
accounts online too much uh too much
 
accounts online too much uh too much
responsibility to do that but it does
 
responsibility to do that but it does
feel like that too. So it's like on one
 
feel like that too. So it's like on one
hand you have sort of like the
 
hand you have sort of like the
deep-rooted lab culture and the other
 
deep-rooted lab culture and the other
hand you have sort of like all of these
 
hand you have sort of like all of these
partners across the Google ecosystem
 
partners across the Google ecosystem
that we're collaborating with everybody
 
that we're collaborating with everybody
from Android that we talked about
 
from Android that we talked about
earlier to Google Cloud to you know,
 
earlier to Google Cloud to you know,
Gmail to workspace etc. etc. and so it's
 
Gmail to workspace etc. etc. and so it's
an interesting blend of like
 
an interesting blend of like
I think there's lots of research work
 
I think there's lots of research work
happening, but like there's tons of
 
happening, but like there's tons of
applied work that's happening to like
 
applied work that's happening to like
actually like work with some of the like
 
actually like work with some of the like
the forefront customers. Like deploying
 
the forefront customers. Like deploying
Gemini to billion user products is a
 
Gemini to billion user products is a
problem that like only two companies in
 
problem that like only two companies in
the world have.
 
the world have.
And we have 13 of those products. And
 
And we have 13 of those products. And
like we the you know, Google goes
 
like we the you know, Google goes
through this all the time now. And it's
 
through this all the time now. And it's
such an interesting place to like see
 
such an interesting place to like see
that happen and see the innovation that
 
that happen and see the innovation that
takes place in order to make that
 
takes place in order to make that
actually possible. And I feel like it's
 
actually possible. And I feel like it's
you can only do that inside of inside of
 
you can only do that inside of inside of
Google, which is really cool.
 
Google, which is really cool.
&gt;&gt; Beautifully said.
 
&gt;&gt; Beautifully said.
Did they Did they give them a lot of
 
Did they Did they give them a lot of
heartburn when you joined and were
 
heartburn when you joined and were
tweeting a lot?
 
tweeting a lot?
&gt;&gt; That's a good question.
 
&gt;&gt; That's a good question.
&gt;&gt; Did you have to get sign-off from
 
&gt;&gt; Did you have to get sign-off from
from comms?
 
from comms?
&gt;&gt; I'm very one of the
 
&gt;&gt; I'm very one of the
the silver linings to my Google
 
the silver linings to my Google
experience has been just like how great
 
experience has been just like how great
that group of like folks across
 
that group of like folks across
marketing and comms are to to work with.
 
marketing and comms are to to work with.
And I think like I you know, their job
 
And I think like I you know, their job
is protect Google, make sure we tell the
 
is protect Google, make sure we tell the
right story, make sure a bunch of bad
 
right story, make sure a bunch of bad
things don't happen. And so, I have a a
 
things don't happen. And so, I have a a
ton of appreciation and partnership with
 
ton of appreciation and partnership with
them. But it's been an incredible
 
them. But it's been an incredible
experience to like be able to go try to
 
experience to like be able to go try to
tell the story that resonates with
 
tell the story that resonates with
developers
 
developers
in a way that feels authentic and not
 
in a way that feels authentic and not
have a huge amount of you know,
 
have a huge amount of you know,
I don't you know, I don't have to get my
 
I don't you know, I don't have to get my
tweets approved all the time and all
 
tweets approved all the time and all
this stuff. Like it's very very positive
 
this stuff. Like it's very very positive
culture. And I think hopefully I I'm
 
culture. And I think hopefully I I'm
always trying to walk the line of not
 
always trying to walk the line of not
not burning the the trust and goodwill
 
not burning the the trust and goodwill
that that I've accumulated with those
 
that that I've accumulated with those
folks. But it's been super positive cuz
 
folks. But it's been super positive cuz
ultimately I think it's like it's really
 
ultimately I think it's like it's really
hard for Google to tell this like
 
hard for Google to tell this like
authentic story. It's just they're just
 
authentic story. It's just they're just
like it's a big company. There's a lot
 
like it's a big company. There's a lot
of people. There's a lot of opinions.
 
of people. There's a lot of opinions.
And so, you take the like magic of
 
And so, you take the like magic of
Google and you water it down through
 
Google and you water it down through
like a lot of people and a lot of
 
like a lot of people and a lot of
process. And you actually
 
process. And you actually
&gt;&gt; Yeah.
 
&gt;&gt; Yeah.
&gt;&gt; You you miss the beautiful story, which
 
&gt;&gt; You you miss the beautiful story, which
is like Google's doing the most
 
is like Google's doing the most
interesting technology in the world and
 
interesting technology in the world and
like helping our users with some of the
 
like helping our users with some of the
hardest problems in the world and
 
hardest problems in the world and
it feels it's a privilege to like get to
 
it feels it's a privilege to like get to
help tell that story. So, it's it's a
 
help tell that story. So, it's it's a
lot of fun. I enjoy it.
 
lot of fun. I enjoy it.
&gt;&gt; I love what you're doing. I love what
 
&gt;&gt; I love what you're doing. I love what
Josh is doing and you guys have put a
 
Josh is doing and you guys have put a
really kind of sincere human touch on
 
really kind of sincere human touch on
as you put it the most important problem
 
as you put it the most important problem
of our time. So.
 
of our time. So.
&gt;&gt; Thank you.
 
&gt;&gt; Thank you.
&gt;&gt; Uh well, wonderful Logan. Thank you so
 
&gt;&gt; Uh well, wonderful Logan. Thank you so
much for joining me today. This is a
 
much for joining me today. This is a
very far-ranging conversation everything
 
very far-ranging conversation everything
from agents and coding to world models
 
from agents and coding to world models
and harnesses and DM culture and you
 
and harnesses and DM culture and you
know lots lots of nuggets here. Thank
 
know lots lots of nuggets here. Thank
you for for joining me today.
 
you for for joining me today.
&gt;&gt; This is a ton of fun. Thank you for
 
&gt;&gt; This is a ton of fun. Thank you for
having me and I'm excited to see what
 
having me and I'm excited to see what
the folks cook up where we've been
 
the folks cook up where we've been
sitting this whole time maybe in front
 
sitting this whole time maybe in front
of us.
 
of us.
&gt;&gt; And maybe they'll be a dog.
 
&gt;&gt; And maybe they'll be a dog.
&gt;&gt; A dog something.
 
&gt;&gt; A dog something.
&gt;&gt; come true.
 
&gt;&gt; come true.
&gt;&gt; [laughter]
 
&gt;&gt; [laughter]
&gt;&gt; I love it.
 
&gt;&gt; I love it.
&gt;&gt; Awesome. Thanks Logan.
 
&gt;&gt; Awesome. Thanks Logan.
&gt;&gt; Of course.
 
&gt;&gt; [music]
 
[music]
 
[music]
