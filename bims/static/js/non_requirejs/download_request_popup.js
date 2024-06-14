function showDownloadPopup(resource_type, resource_name, callback, auto_approved = true, on_hidden = null) {
  const $downloadPopup = $('#download-popup');
  if(resource_type === 'CSV'){
    $downloadPopup.find('#data-format').show()
  } else {
    $downloadPopup.find('#data-format').hide()
  }
  $downloadPopup.find('#download-popup-title').html(resource_name);
  $downloadPopup.modal('show');
  $('#download-notes').val('');

  const $submitDownloadPopup = $downloadPopup.find('.submit-download');
  const $downloadPurpose = $('#download-purpose');
  const url = '/api/download-request/';

  let urlParams = new URLSearchParams(window.location.href.replace('/taxon', '/&taxon'))
  let taxon_id = urlParams.get('taxon');
  let site_id = urlParams.get('siteId');
  let survey_id = urlParams.get('survey');

  $submitDownloadPopup.on('click', function () {
    $submitDownloadPopup.prop('disabled', true);
    if (resource_type === 'CSV') {
      resource_type = $('#download-format').val()
    }
    let postData = {
      purpose: $downloadPurpose.val(),
      dashboard_url: window.location.href,
      resource_type: resource_type,
      resource_name: resource_name,
      site_id: site_id,
      survey_id: survey_id,
      taxon_id: taxon_id,
      notes: $('#download-notes').val(),
      auto_approved: auto_approved ? 'True' : 'False',
    };

    $.ajax({
      url: url,
      headers: {"X-CSRFToken": csrfmiddlewaretoken},
      type: 'POST',
      data: postData,
      success: function (data) {
        callback(data['download_request_id']);
        setTimeout(function () {
          $downloadPopup.modal('hide');
          $submitDownloadPopup.prop('disabled', false);
        }, 500)
      }, error: function (jqXHR, textStatus, errorThrown) {
        let errorMessage = "Error submitting download request.";
        if (jqXHR.responseJSON && jqXHR.responseJSON.error) {
          errorMessage += " " + jqXHR.responseJSON.error;
        } else if (textStatus) {
          errorMessage += " " + textStatus;
        }
        alert(errorMessage);
        $downloadPopup.modal('hide');
        $submitDownloadPopup.prop('disabled', false);
      }
    });
  });

  // Remove events
  $downloadPopup.on('hidden.bs.modal', function () {
    $submitDownloadPopup.off('click');
    $downloadPopup.off('hidden.bs.modal');
    if (on_hidden) {
      on_hidden();
    }
  })
}
