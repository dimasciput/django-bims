define(['jquery', 'backbone', 'models/search_result', 'views/search_result', 'shared'], function ($, Backbone, SearchModel, SearchResultView, Shared) {
    return Backbone.Collection.extend({
        model: SearchModel,
        url: "",
        searchUrl: "/api/search/",
        viewCollection: [],
        searchPanel: null,
        searchValue: '',
        isFuzzySearch: false,
        modelId: function (attrs) {
            return attrs.record_type + "-" + attrs.id;
        },
        search: function (searchPanel, parameters) {
            this.searchValue = parameters['search'];
            this.collectorValue = parameters['collector'];
            this.categoryValue = parameters['category'];
            this.yearFrom = parameters['yearFrom'];
            this.yearTo = parameters['yearTo'];
            this.months = parameters['months'];
            this.boundary = parameters['boundary'];
            this.userBoundary = parameters['userBoundary'];
            this.referenceCategory = parameters['referenceCategory'];

            this.url = this.searchUrl +
                '?search=' + this.searchValue +
                '&collector=' + this.collectorValue +
                '&category=' + this.categoryValue +
                '&yearFrom=' + this.yearFrom +
                '&yearTo=' + this.yearTo +
                '&months=' + this.months +
                '&boundary=' + this.boundary +
                '&userBoundary=' + this.userBoundary +
                '&referenceCategory=' + this.referenceCategory;
            this.searchPanel = searchPanel;
            this.searchPanel.showSearchLoading();
        },
        hideAll: function (e) {
            if ($(e.target).data('visibility')) {
                $(e.target).find('.filter-icon-arrow').addClass('fa-angle-down');
                $(e.target).find('.filter-icon-arrow').removeClass('fa-angle-up');
                $(e.target).nextAll().hide();
                $(e.target).data('visibility', false)
            } else {
                $(e.target).find('.filter-icon-arrow').removeClass('fa-angle-down');
                $(e.target).find('.filter-icon-arrow').addClass('fa-angle-up');
                $(e.target).nextAll().show();
                $(e.target).data('visibility', true)
            }

        },
        parse: function (response) {
            var result = response['records'];
            result = result.concat(response['sites']);
            this.isFuzzySearch = response['fuzzy_search'];
            return result
        },
        renderCollection: function () {
            var self = this;
            var searchResultTitle = this.searchValue;
            if (this.isFuzzySearch) {
                searchResultTitle = 'similar to ' + searchResultTitle;
            }
            this.searchPanel.updatesearchPanelTitle(searchResultTitle);
            if (this.models.length === 1) {
                if (this.models[0]['attributes'].hasOwnProperty('results')) {
                    self.searchPanel.fillPanelHtml(this.models[0]['attributes']['results']);
                    return false;
                }
            }

            var $searchResultsWrapper = $('<div></div>');
            $searchResultsWrapper.append(
                '<div class="search-results-wrapper">' +
                '<div class="search-results-total" data-visibility="true"> SITES (<span id="site-list-number"></span>) <i class="fa fa-angle-down pull-right filter-icon-arrow"></i></div>' +
                '<div id="site-list" class="search-results-section"></div>' +
                '</div>');
            $searchResultsWrapper.append(
                '<div class="search-results-wrapper">' +
                '<div class="search-results-total" data-visibility="true"> TAXA (<span id="taxa-list-number"></span>) <i class="fa fa-angle-down pull-right filter-icon-arrow"></i></div>' +
                '<div id="taxa-list" class="search-results-section"></div>' +
                '</div>');

            self.searchPanel.fillPanelHtml($searchResultsWrapper);

            $.each(this.viewCollection, function (index, view) {
                view.destroy();
            });
            this.viewCollection = [];

            var biologicalCount = 0;
            var siteCount = 0;
            var speciesListName = [];
            $.each(this.models, function (index, model) {
                var searchResultView = new SearchResultView({
                    model: model
                });
                self.viewCollection.push(searchResultView);

                // update count
                if (searchResultView.getResultType() == 'taxa') {
                    biologicalCount += 1;
                    speciesListName.push(searchResultView.model.get('common_name'));
                } else if (searchResultView.getResultType() == 'site') {
                    siteCount += 1
                }
            });
            $('#taxa-list-number').html(biologicalCount);
            $('#site-list-number').html(siteCount);
            $searchResultsWrapper.find('.search-results-total').click(self.hideAll);
            $searchResultsWrapper.find('.search-results-total').click();
            Shared.Dispatcher.trigger('siteDetail:updateCurrentSpeciesSearchResult', speciesListName);
        }
    })
});
