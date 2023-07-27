document.querySelector('#form_send_data').addEventListener('submit', async (event) => {
    event.preventDefault();
    const url = event.target.action;
    const formData = new FormData(event.target);
    try {
      const response = await fetch(url, {
        method: 'POST',
        body: formData
      });
      if (response.ok) {
        const data = await response.json();
        if (data.success) {
          console.log('Успех')
          console.log(data)
          document.querySelector('.b_title--send_form').textContent = 'Данные успешно отпралены'
          document.querySelector('#form_send_data').reset();
          document.querySelector('#form_send_data').style.display = "none";
        } else if (data.error) {
          console.log('Провал')
          console.log(data)
          document.querySelector('.b_title--send_form').textContent = 'Что-то пошло не так, перезагрузите страницу и попробуйте ещё раз'
          document.querySelector('#form_send_data').reset();
          document.querySelector('#form_send_data').style.display = "none";
        }
      } else {
        throw new Error(`Ошибка HTTP: ${response.status}`);
      }
    } catch (error) {
      console.error(error);
    }
  });
