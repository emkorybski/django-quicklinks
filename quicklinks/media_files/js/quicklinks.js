
// ENTRY ROUTE

window.LinkRouter = Backbone.Router.extend({

    routes: {
        "":'index'
    },
    fetch_collection: function(callback){

        this.processCollection = new GroupCollection();
        this.processCollection.fetch({
            error:function () {

                 },
            success:function () {
                callback();
                }
        });

    },
    index: function(){
        var self = this;

        //TODO append a new element with id quicklinks_wrapper to the body of the existing page - hidden by default
        $('body').append('<div id="quicklinks_wrapper"></div>');

        this.fetch_collection(function () {
            self.groupcollectionView = new GroupCollectionView({collection: self.processCollection, el : $('#quicklinks_wrapper')});
            self.groupcollectionView.render();
        });
    }
});


// MODELS & COLLECTIONS

var Link = Backbone.Model.extend({
    defaults: {
        title: '',
        url:''
    }
});


var LinkCollection= Backbone.Collection.extend({
    model: Link
});



var Group = Backbone.Model.extend({
    defaults: {
        title:'',
        order_int:''
    },
    initialize: function(){
        this.set('links', new LinkCollection(this.get('links')));
    }
});

//
// JSON response from Django app populates this collection
//
var GroupCollection= Backbone.Collection.extend({
    model: Group,
    comparator: function(group){
        return group.get("order_int");
    },
    url:"/quicklinks/quicklinks/"
});

var GroupView = Backbone.View.extend({
    tagName:'li',
    template: _.template('<strong><%= order_int %>.' + gettext('<%= title %>') + ' tab</strong>'),  //each group will be displayed in this div,,
    render: function(){
        $(this.el).html(this.template(this.model.toJSON()));
        var linkcollectionView = new LinkCollectionView({collection: this.model.get('links') });
        $(this.el).append(linkcollectionView.render().el);
        return this
    }

});


// MAIN view for the collection that grabs up JSON response
var GroupCollectionView = Backbone.View.extend({
    tagName:'div',
   // template: _.template('<div></div>'),  //each group will be displayed in this div,,
    events: {
        "click button" : "slideout",
        "click button.hide_column" : "slidein"
    },
    slideout: function(){

                $(this.groups_ul).css({'height':$(window).height() - 210, 'width':250}).animate({

                    marginLeft:-3

                }).show();

                 $('#quicklinks_button').addClass('hide_column').html("Hide Links");
            },


    slidein: function(){

        //$(this.groups_ul).css({'height':$(window).height() - 210}).animate({
                 $(this.groups_ul).animate({

                 marginLeft:-283

            });

            $('#quicklinks_button.hide_column').removeClass('hide_column').html("Show Links");
    },

    render: function(){
        var self = this;
        //$(this.el).html(this.template());

        if(self.collection.size() > 0)
        {
            $(self.el).html('<div><h3>' + gettext('Quick Links') +'</h3><button id="quicklinks_button" class="btn">' + gettext('Show Links') + '</button></div>');
            this.groups_ul = $('<ul></ul>');
            $(this.el).append(this.groups_ul);
            $(this.groups_ul).hide();
            self.collection.each(function(group){ // handles each Group model

                var groupView = new GroupView({model:group});

                $(self.groups_ul).append(groupView.render().el);

            });
            return this;
        }else{
            return '';
        }
    }

});

var LinkView = Backbone.View.extend({
    tagName:'li',
    template: _.template('<a href="<%= url %>">' + gettext('<%= title %>') + '</a>'),  //each group will be displayed in this div,,
    render: function(){
        var self = this;
        $(this.el).html(this.template(this.model.toJSON()));
        return this;
    }

});

var LinkCollectionView = Backbone.View.extend({
    model:Link,
    tagName:'ul',
    render: function(){
        var self = this;

        self.collection.each(function(link){ // handles each Link model

            var linkView = new LinkView({model:link});
            $(self.el).append(linkView.render().el);

        });
        return this;
    }

});


// INIT IN THE ROUTES

var viewportWidth = $(window).width();

var allowedWidth = viewportWidth - 988;


if(allowedWidth > 500){

    var router = new window.LinkRouter();
    //We won't use the normal Backbone.history.start here as there may be other backbone apps on the page
    //Backbone.history.start();
    //router.navigate('', {trigger:true});
    router.index();
}
