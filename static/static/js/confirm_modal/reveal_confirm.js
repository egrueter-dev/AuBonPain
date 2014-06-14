/**
 * Created by campbell.chri on 5/20/14.
 * Assisted by : https://github.com/agoragames/confirm-with-reveal
 */


function confirm_modal(title, message, yesCallback, noCallback) {

        modal = $("<div data-reveal class='reveal-modal small'>\n  <h4 data-confirm-title class='page-title'><span></span></h4>\n  <p data-confirm-message></p>\n  <div class='right'>\n    <a data-confirm-cancel class='button secondary'></a>\n <a data-confirm class='button alert'></a>\n  </div>\n</div>");

        modal.find('[data-confirm-title] span').html(title);
        modal.find('[data-confirm-message]').html(message);
        modal.find('[data-confirm-cancel]').html('Cancel').on('click', function() {
            modal.foundation('reveal', 'close');
            noCallback();
        });
        modal.find('[data-confirm]').html('Confirm').on('click', function() {
            yesCallback();
            modal.foundation('reveal', 'close');
        });

        modal.appendTo($('body')).foundation().foundation('reveal', 'open').on('closed.fndtn.reveal', function(e) {
            return modal.remove();
        });
    }